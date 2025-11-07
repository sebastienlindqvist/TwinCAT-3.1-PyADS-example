# TwinCAT 3.1 PyADS example
>[!Note] 
>- **This repo is not officially Beckhoff**
>- **pyADS is a third-party product and not supported by Beckhoff**
- This is a basic example of using the python library called PyADS to communicate with a TwinCAT 3.1 XAR.
- This specific method of implementation places all variables within a YAML file seperate from the main python program to make it easier for adding, removing and altering varaibles.
- In addition, the ability to read and write to variables by parsing in arguments with values. 

## 🗂️ Prerequisites
- This example code will require a pre-existing TwinCAT 3.1 project with a variable called `nCounter` in `Main` running and has port 851 open.

### 🪛 OS related requirements:
---
- If you're running this python example from a Windows OS.
- `TwinCAT 3.1 XAE` will need to be installed as PyADS needs necessary `.dll` files.
---
- Running this python example from a Linux distro should not have any issues.
- The necessary drivers required are installed when installing `PyADS` with `pip`.
- The most likely issue would be route not being added to the `StaticRoutes.xml` on the `TwinCAT 3.1 XAR` target.
---
- If the `TwinCAT 3.1 XAR` target is `TwinCAT RT Linux`.
- You will need to add a route manually added to `StaticRoutes.xml`.
- It can be found here: `/etc/TwinCAT/3.1/Target/StaticRoutes.xml`.

Below is an example of the StaticRoutes.xml:
```xml
<?xml version="1.0"?> 
<TcConfig xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.beckhoff.com/>        <RemoteConnections>
                <Route>
                        <Name>192.168.0.1</Name>
                        <Address>192.168.0.1</Address>
                        <NetId>192.168.0.1.1.1</NetId>
                        <Type>TCP_IP</Type>
                </Route>
        </RemoteConnections>
</TcConfig>
```
- The `Name` is the same as the `Address` due to not having a DNS server which can associate a Hostname to an IP address.
- If you're running this python program directly on the `TwinCAT RT Linux` as well.
- This route will have the same IP address as the `TwinCAT RT Linux XAR` itself.
- However, the `NetID` (short for `AmsNetID`) in the `StaticRoutes.xml` needs to be differnt to the `AmsNetID` for TwinCAT XAR runtime on the TwinCAT RT/Linux.

## ⚙️ Installation
- Install packages with pip
```shell
pip install -r requirements.txt
```
## 🗝️️ Usage
1. Have TwinCAT 3.1 project running with variable `nCounter` on type `INT` declared in `Main (PRG)`.
2. Rename the `com_comfig(Example).yaml` to `com_comfig.yaml`.
3. Fill `com_comfig.yaml` with the necessary information.
4. Run the python program from `Command line/prompt` with:
```shell
python .\TwinCAT_Add_Route.py --read testVar PLCTYPE_INT
```
- It then should read the current value of `nCounter`
- for more information, run:
```shell
python .\TwinCAT_Add_Route.py --help
```
5. Alternatively, you import this into your own program or edit the `def main()` section of the program.