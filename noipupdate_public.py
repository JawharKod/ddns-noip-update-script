import requests
import base64
import socket

def get_current_public_ip():

    try:
        return requests.get('https://api.ipify.org').text
    except requests.RequestException as e:
        return f"Error obtaining public IP: {e}"

def get_noip_hostname_ip(hostname):

    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def update_noip_hostname(username, password, hostname, agent_name, current_ip):


    # Endpoint for updating the No-IP hostname
    url = "https://dynupdate.no-ip.com/nic/update"

    # Prepare the Base64 encoded authentication
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Set the custom User-Agent
    user_agent = f"{agent_name}/1.0 JK"

    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'User-Agent': user_agent
    }

    # Prepare the parameters for the request
    params = {'hostname': hostname, 'myip': current_ip}

    # Make the request to No-IP
    try:
        response = requests.get(url, headers=headers, params=params)
        return response.text
    except requests.RequestException as e:
        return f"Error updating No-IP hostname: {e}"

# Replace with your details
username = "YOUR_NOIP_EMAIL"
password = "YOUR_NOIP_PASSWORD"
hostname = "YOUR_NOIP_HOSTNAME"
agent_name = "YOUR_AGENT_NAME"  

# Get the current public IP and the IP associated with the No-IP hostname
current_ip = get_current_public_ip()
noip_ip = get_noip_hostname_ip(hostname)

# Check if the IPs are different and update if they are
if current_ip != noip_ip:
    result = update_noip_hostname(username, password, hostname, agent_name, current_ip)
    print(result)
else:
    print("No update needed. Current IP matches No-IP hostname IP.")
