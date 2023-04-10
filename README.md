</head>
<body>
	<h1>WifiDakkat2.0.py README</h1>
	<p>This script is a Python program designed to extract Wi-Fi profiles and IP address information from a Windows computer and send it to a specified URL using the Requests library. The program also writes the extracted information to a local file named "passwords.txt".</p>
	<h2>Prerequisites</h2>
	<ul>
		<li>Python 3 installed on the computer</li>
		<li> This script is built using Python and requires the following libraries to be installed:
			-subprocess
			-os
			-sys
			-requests</li>
	</ul>
	<h2>Usage</h2>
	<p>1. Open the command prompt or terminal</p>
	<p>2. Navigate to the directory containing the script using the "cd" command</p>
	<p>3. Type "python WifiDakkat2.0.py" to run the script</p>
	<p>4. The script will create a file named "passwords.txt" in the same directory and write the extracted information to it</p>
	<p>5. The script will also send the file to a specified URL using the Requests library</p>
	<h2>Creating an executable file</h2>
	<p>To create an executable file, navigate to the directory containing the script using the command prompt or terminal and type "pyinstaller --onefile WifiDakkat2.0.py". This will create an executable file in the "dist" directory.</p>
	<h2>Credits</h2>
	<p>This script was created by Nafiul Ahmed.</p>
</body>
</html>
