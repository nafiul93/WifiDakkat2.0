WiFi Password Stealer
This script is designed to steal the passwords of all the WiFi networks that have been connected to a Windows computer and upload them to a designated URL.

Prerequisites
This script is built using Python and requires the following libraries to be installed:

subprocess
os
sys
requests
Installation
No installation is required. Simply download the script and run it using Python.

Usage
Open the command prompt in the directory where the script is located.
Type python wifi_stealer.py to execute the script.
The script will generate a file named passwords.txt containing all the stolen passwords as well as the IP address information.
The passwords.txt file will be uploaded to the URL specified in the url variable.
Note: The url variable should be set to the URL where you want to upload the passwords.txt file.

How it works
This script uses the netsh command to extract the WiFi profiles on the Windows computer. It then reads the XML files containing the profiles to extract the SSID and password information. It also extracts the IP address information using the ipconfig command. Finally, it saves all this information to a text file named passwords.txt and uploads it to the specified URL using the requests library.

Making an executable file
To create an executable file, use the pyinstaller library. Open the command prompt in the directory where the script is located and type pyinstaller --onefile wifi_stealer.py. This will create an executable file in the dist directory.
