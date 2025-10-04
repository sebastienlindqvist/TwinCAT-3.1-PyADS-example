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

## How to run:
1. Rename the `com_comfig(Example).yaml` to `com_comfig.yaml`.
2. Fill `com_comfig.yaml` with the necessary information.
3. Install the `pyads` with `pip`
4. Run the python program
- It then should read the current value of `nCounter`, write to `nCounter` to have a value of 3, then re-reads the value