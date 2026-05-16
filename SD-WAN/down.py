import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"

# ------------------------------------
# Authenticate and get session cookie
# ------------------------------------
def get_session():
    login_url = f"{vmanage_host}/j_security_check"
    payload = {
        "j_username": username,
        "j_password": password
    }

    session = requests.session()
    response = session.post(login_url, data=payload, verify=False)

    if response.status_code != 200 or "html" in response.text.lower():
        print("Login failed! Check credentials.")
        return None

    return session


# ------------------------------------
# Get SD-WAN device list
# ------------------------------------
def get_device_list(session):
    url = f"{vmanage_host}/dataservice/device"
    response = session.get(url, verify=False)

    if response.status_code != 200:
        print("Failed to pull device list!")
        return []

    return response.json()


# ------------------------------------
# Filter DOWN devices
# ------------------------------------
def get_down_devices(devices):
    down = []
    for d in devices:
        if d.get("reachability") != "reachable":  # normal = UP
            down.append({
                "hostname": d.get("host-name"),
                "system_ip": d.get("system-ip"),
                "state": d.get("reachability")
            })
    return down


# ------------------------------------
# Main
# ------------------------------------
if __name__ == "__main__":
    session = get_session()
    if session:
        devices = get_device_list(session)
        down_devices = get_down_devices(devices)

        print("\n=== DOWN SD-WAN DEVICES ===")
        if not down_devices:
            print("All devices are UP")
        else:
            for d in down_devices:
                print(f"{d['hostname']}  |  {d['system_ip']}  |  {d['state']}")