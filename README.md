# Python Tips

## Install Python Quietly
* Reference: [Installing Without UI](https://docs.python.org/3/using/windows.html#installing-without-ui)
```
# Example
python3_installer.exe /quiet DefaultJustForMeTargetDir=C:\python3 Include_launcher=0 SimpleInstall=1 
```


## Virtualenv
* Reference: [Virtualenv CLI](https://virtualenv.pypa.io/en/latest/cli_interface.html#cli-flags)
```
# Example
# create virtualenv in the .venv directory
python -m venv .venv

# on Windows
.venv\Scripts\activate

# on Linux
source .venv/bin/activate
```
