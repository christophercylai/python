r"""
This script keeps the computer awake by pressing right ctrl key every SEC seconds
Put this script in $USERPROFILE\Downloads for easy access

To setup using PowerShell:
> cd $env:USERPROFILE\Downloads
> python -m venv .venv
> .venv\Scripts\activate
> pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org pyautogui
> python redbull.py
"""
import pyautogui
from time import sleep

SEC = 180
pyautogui.FAILSAFE = False

while True:
    sleep(SEC)
    pyautogui.press('ctrlright')
