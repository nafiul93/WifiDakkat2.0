</head>
<body>
	<h1>WifiDakkat2.0</h1>
	<p>A Python script for extracting Wi-Fi passwords and IP address information from a Windows machine and sending them to a specified URL.</p>
	<h2>Instructions</h2>
<ol>
	<li>Make sure Python is installed on your Windows machine.</li>
	<li>Download the script to your machine.</li>
	<li>Open a command prompt or PowerShell window and navigate to the directory where the script is located.</li>
	<li>Run the script using the command <code>python WifiDakkat2.0.py</code>.</li>
	<li>The script will create a file called <code>passwords.txt</code> in the same directory as the script.</li>
	<li>The script will extract the Wi-Fi passwords and IP address information from your Windows machine and write them to the <code>passwords.txt</code> file.</li>
	<li>The script will send the <code>passwords.txt</code> file to the specified URL using the HTTP POST method.</li>
</ol>

<h2>Code Explanation</h2>
<p>The script uses the following Python modules:</p>
<ul>
	<li><code>subprocess</code> for running Windows commands from Python.</li>
	<li><code>os</code> for interacting with the file system.</li>
	<li><code>sys</code> for system-specific parameters and functions.</li>
	<li><code>requests</code> for sending HTTP requests.</li>
</ul>

<p>The script performs the following steps:</p>
<ol>
	<li>Sets a URL for where the extracted information will be sent.</li>
	<li>Creates a <code>passwords.txt</code> file to write the extracted Wi-Fi passwords and IP address information to.</li>
	<li>Executes a Windows command to extract the Wi-Fi profiles from the system.</li>
	<li>Extracts the Wi-Fi passwords and SSIDs from the extracted Wi-Fi profiles.</li>
	<li>Gets the IP address information using the <code>ipconfig</code> command.</li>
	<li>Writes the Wi-Fi passwords and IP address information to the <code>passwords.txt</code> file.</li>
	<li>Sends the <code>passwords.txt</code> file to the specified URL using the HTTP POST method.</li>
</ol>

<h2>Usage</h2>
<p>To make an executable from the script:</p>
<ol>
	<li>Open a command prompt or PowerShell window and navigate to the directory where the script is located.</li>
	<li>Run the command <code>pyinstaller --onefile WifiDakkat2.0.py</code>.</li>
	<li>The executable will be created in a new <code>dist</code> folder.</li>
</ol>

<h2>Disclaimer</h2>
<p>This script is for educational purposes only. Use at your own risk.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="https://github.com/nafiul93/WifiDakkat2.0/blob/main/license.txt">LICENSE</a> file for details.</p>

<h2>Authors</h2>
<ul>
	<li>Naful Ahmed</li>
