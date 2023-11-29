# No-IP Dynamic DNS Update Script

## Overview
This Python script offers a simple and reliable way to update your No-IP dynamic DNS hostname with your current public IP address. It's particularly useful for users whose routers do not support DDNS functionality or those who encounter issues with the official No-IP client, especially on Windows.

The script is also an ideal solution for implementation on low-power devices like Raspberry Pi or Orange Pi, making it a versatile tool for various home network setups.

## Background
The motivation for creating this script was to enable remote monitoring of a 3D printer from outside the office. Without built-in DDNS support in the router and difficulties in using the official No-IP client for Windows, this script serves as a custom solution to ensure reliable remote access.

## Features
- **Automatic IP Detection**: Detects your current public IP address.
- **Efficient Updates**: Checks if the current IP differs from the IP associated with your No-IP hostname and updates only if necessary.
- **Easy to Schedule**: Can be set up to run at regular intervals and on system startup, especially useful for headless setups like Raspberry Pi or Orange Pi.
- **Simple Configuration**: Requires minimal setup - just configure with your No-IP account details.

## Requirements
- Python 3
- `requests` library (Install using `pip install requests`)

## Usage
1. Clone the repository or download the script.
2. Open the script in a text editor and replace `your_noip_username`, `your_noip_password`, `your_noip_hostname.bounceme.net`, and `YourClientName` with your actual No-IP account details and desired user agent information.
3. Run the script manually or set it up to run periodically using a scheduler (like cron jobs on Linux or Task Scheduler on Windows).

## Setting Up a Scheduler
### On Raspberry Pi (Linux)
1. Open crontab: `crontab -e`
2. Add a line: `*/30 * * * * python /path/to/noipupdate.py` to run it every 30 minutes.

### On Windows
1. Use the Task Scheduler to run the script at startup and every 30 minutes.

## License
[MIT License](LICENSE)
