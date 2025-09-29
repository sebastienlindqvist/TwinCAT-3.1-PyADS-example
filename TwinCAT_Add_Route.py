import pyads
import yaml
from termcolor import colored

TextFile='./com_comfig.yaml'
TextFile2='./variables.yaml'

class ADS_Route():
    def __init__(self):
        super().__init__() 
        self.varialbe_list =[[],[]]
        self.resetableBool = True
        self.USERNAME, self.PASSWORD, self.TARGET_IP, self.AMSNETID, self.LOCAL_AMSNETID, self.LOCAL_IP, self.ROUTE_NAME  = self.Read_ConnectionInfo(TextFile)
        #self.LOCAL_AMSNETID, self.LOCAL_IP = self.Set_LocalAMS()
        self.Add_Route(self.LOCAL_AMSNETID,
                       self.LOCAL_IP,
                       self.TARGET_IP,
                       self.USERNAME,
                       self.PASSWORD,
                       self.ROUTE_NAME)
        self.plc=self.Open_Connection(self.AMSNETID,self.TARGET_IP)

        self.data=self.Read_VariableInfo()

    def Read_ConnectionInfo(self, Filename):
        with open(Filename, "r") as file:
            data = yaml.safe_load(file)
        # Box width
        box_width = 65
        content_width = box_width - 4  # Subtract space for borders (│ and │)
        # Print the top border
        print("\n")
        print("╭─ TwinCAT pyAds" + "─" * (box_width - 19) + "╮")
        # Print a separator
        # Print the header
        header = " This is a demo for connecting to TwinCAT XAR via pyAds "
        print("│" + header.center(content_width) + "│")

        print("├" + "─" * (box_width - 4) + "┤")
        # Helper function to print each line with proper padding
        def print_line(key, value):
            line = f"{key}: {value}"  # Construct the key-value pair
            # Ensure it fits exactly in the content_width
            print("│" + line.ljust(content_width) + "│")
        # Add each line
        print_line("Route Name", repr(data["route_name"]))
        print_line("Local AmsNetID", repr(data["sender_ams"]))
        print_line("Local IP", repr(data["local_ip"]))
        print_line("PLC AmsNetID", repr(data["remote_ads"]))
        print_line("PLC IP adress", repr(data["plc_ip"]))
        print_line("Username", repr(data["Username"]))
        print_line("Password", repr(data["Password"]))

        # Print the bottom border
        print("╰" + "─" * (box_width - 4) + "╯")
        return data["Username"], data["Password"], data["plc_ip"], data["remote_ads"], data["sender_ams"], data["local_ip"], data["route_name"]
    
    def Add_Route(self, SENDER_AMS, HOSTNAME, PLC_IP, USERNAME, PASSWORD, ROUTE_NAME):
        print("\n- Adding Route to ePC/IPC")
        print("-----------------------------------------------")
        pyads.open_port()
        pyads.set_local_address(SENDER_AMS)
        try:
            pyads.add_route_to_plc(SENDER_AMS, 
                                HOSTNAME, 
                                PLC_IP, 
                                USERNAME, 
                                PASSWORD, 
                                route_name=ROUTE_NAME
                                )
        except:
            print("Error occured when adding route")
            print("Check text file has correct information")
            print("Check Device Manager of target IPC to see if route has been made or already exists")
        pyads.close_port()

    def Open_Connection(self, TARGET_AMS_ID, TARGET_PC_IP):
        print("\n- Opening connection to ePC/IPC")
        print("-----------------------------------------------")
        try:
            plc = pyads.Connection(TARGET_AMS_ID, pyads.PORT_TC3PLC1, TARGET_PC_IP)
            plc.open()
            print ("Connection opened")
        except:
            print ("Error occured when opening connection")
        return plc
    
    def Read_Variable(self, variable, valueType=pyads.PLCTYPE_BOOL ,arrayIndex=None):
        if arrayIndex == None:
            return self.plc.read_by_name("", valueType, handle=self.data[variable]["plc"])
        else:
            return self.plc.read_by_name('', valueType, handle=self.data[variable]["plc"][arrayIndex])
    
    def Read_Structure(self, variable, valueType=pyads.PLCTYPE_BOOL ,arrayIndex=6):
        list = []
        for i in range(arrayIndex):
            list.append(self.plc.read_by_name("", valueType, handle=self.data[variable]["plc"][i]))
        return list


    def Write_Variable(self, variable, value, valueType=pyads.PLCTYPE_BOOL ,arrayIndex=None):
        #self.plc.write_by_name("", value, pyads.PLCTYPE_INT, handle=variable)
        if arrayIndex == None:
            self.plc.write_by_name("", value, valueType, handle=self.data[variable]["plc"])
        else:
            self.plc.write_by_name("", value, valueType, handle=self.data[variable]["plc"][arrayIndex])

    def GetHandle(self,variable):
        #print(variable)
        return self.plc.get_handle(variable)

    def Read_VariableInfo(self):
        with open(TextFile2, "r") as file:
            data = yaml.safe_load(file)

        try: # this FOR loop replaces the locally saved variable names (e.g. Main.nTest) to their handles which dramatically improves performance
            for key, value in data.items():
                if isinstance(value, dict) and 'plc' in value:
                    if not isinstance(value['plc'], list):  # Single value
                        #print(f"Single value - {key}: {value['plc']}")
                        try:
                            value['plc'] = self.GetHandle(value['plc'])
                        except:
                            print(f"Error getting handle for {key}: {value['plc']}")
                            value['plc'] = None
                    else:  # List value
                        #print(f"List - {key}:")
                        for i, item in enumerate(value['plc'], 1):
                            try:
                                value['plc'][i-1] = self.GetHandle(item)
                            except:
                                print(f"Error getting handle for {key} index {i}: {item}")
                                value['plc'][i-1] = None
                            #print(f"    Joint {i}: {item}")
            return data
        except Exception as e:
            print(f"------------------------------------------------------- \n")
            print(f"Error processing the dictionary: {e} \n")
            print(f"returning None \n")
            print(f"------------------------------------------------------- \n")
            return None


def main():
    testObject=ADS_Route()
    print(testObject.data["testVar"]["plc"]) # this will get the handle at the beginning of the connection to allow fast retreival of data later on.

    print(testObject.Read_Variable("testVar", pyads.PLCTYPE_INT)) # this will get the value from the XAR

    testObject.Write_Variable("testVar", "3", pyads.PLCTYPE_INT)

    print(testObject.Read_Variable("testVar", pyads.PLCTYPE_INT))
    pass

if __name__ == "__main__":
    main()