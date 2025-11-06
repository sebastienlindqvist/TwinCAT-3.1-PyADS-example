# TwinCAT-3.1-PyADS-example
>[!Note] 
>- **This repo is not officially Beckhoff**
>- **pyADS is a third-party product and not supported by Beckhoff**
- This is a basic example of using PyADS with to communicate with a TwinCAT 3 XAR.

## Prerequisites
- TwinCAT project with a variable called `nCounter` in `Main` running and has port 851 open.

### OS related issues
#### - Windows as ADS client
- Will require `TwinCAT XAE` installed in order to run pyADS on a Windows machine.

#### - TwinCAT RT/Linux to itself.
- Will need to add a route manually added to `StaticRoutes.xml`
- It can be found here: `/etc/TwinCAT/3.1/Target/StaticRoutes.xml`

Below is an example of the StaticRoutes.xml
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
- The Name is the same as the Address due to not having a DNS server which can associate a Hostname to an IP address.
- This will be the same IP address if you're running this locally on the TwinCAT RT/Linux.
- However, the NetID (short for AmsNetID) in the `StaticRoutes.xml` needs to be differnt to the AmsNetID for TwinCAT XAR runtime on the TwinCAT RT/Linux.

## ⚙️ Installation
- Install packages with pip
  ```shell
  pip install -r requirements.txt
  ```
## 🗝️️ Usage
1. Have TwinCAT 3.1 project running with variable `nCounter` in `Main (PRG)`
2. Rename the `com_comfig(Example).yaml` to `com_comfig.yaml`.
2. Fill `com_comfig.yaml` with the necessary information.
3. Run the python program from `Command line/prompt` with:
```shell
python .\TwinCAT_Add_Route.py --read testVar PLCTYPE_INT
```
- It then should read the current value of `nCounter`
- for more information, run:
```shell
python .\TwinCAT_Add_Route.py --help
```
5. Alternatively, you import this into your own program or edit the `def main()` section of the program.