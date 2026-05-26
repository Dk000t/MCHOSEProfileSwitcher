# MCHOSEProfileSwitcher

These scripts, written in Python and automated with Selenium, automatically apply a performance profile (including motion sync, polling rate, DPI, etc.) when launching a Steam game on Linux, and switch to a power-saving profile when closing it.

## Instructions

### Install chromium, python and python-selenium:
```bash
yay -S chromium python python-selenium
```
### Get the Vendor ID and Product ID of your mouse from:
```bash
lsusb
```
### Create an udev rule:
```bash
nano /etc/udev/rules.d/99-mouse-mchose.rules
```
### Paste the following line into the file, making sure to change your specific mouse Vendor ID and Product ID in the appropriate fields:
```bash
KERNEL=="hidraw*", ATTRS{idVendor}=="3837", ATTRS{idProduct}=="100b", MODE="0666", TAG+="uaccess"
```
### Reload udev rules:
```bash
udevadm control --reload && udevadm trigger
```
### Start Chromium from the terminal in the specified user directory:
```bash
chromium --user-data-dir=$HOME/.config/chromium_profile
```
### Open the MCHOSE webdriver website, pair your mouse and create two profiles, one called "Performance" and one called "Powersave":
```bash
www.mchose.com.cn
```
### Copy the URL you see in the address bar for your mouse and edit it in your scripts (example from MCHOSE A7 V2 ULTRA):
```bash
URL = "https://www.mchose.com.cn/#/detail?deviceName=MCHOSE+A7+V2+Ultra"
```
### Add to Steam Game Commands (change the directory based on where your scripts are):
```bash
python3 ~/Scripts/mouse.py Performance %command%; python3 ~/Scripts/mouse.py Powersave
```
