# TwinCAT-3.1-PyADS-example
>[!Note] 
>- **This repo is not officially Beckhoff**
>- **pyADS is a third-party product and not supported by Beckhoff**
- This is a basic example of using PyADS with to communicate with a TwinCAT 3 XAR.

## Prerequisites
- TwinCAT project with a variable called `nCounter` in `Main` running and has port 851 open.

## How to run:
1. Rename the `com_comfig(Example).yaml` to `com_comfig.yaml`.
2. Fill `com_comfig.yaml` with the necessary information.
3. Install the `pyads` with `pip`
4. Run the python program
- it then should read the current value of `nCounter`, write to `nCounter` to have a value of 3, then re-reads the value