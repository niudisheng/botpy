import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip = response.json().get('ip')
        return ip
    except Exception as e:
        return f"Error: {e}"

public_ip = get_public_ip()
print(f'Your public IP address is: {public_ip}')