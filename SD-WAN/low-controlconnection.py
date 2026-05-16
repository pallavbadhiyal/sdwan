import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"


# -------------------------------
#  Authenticate and get session
# -------------------------------
def get_session():
    url = f"{vmanage_host}/j_security_check"
    payload = {"j_username": username, "j_password": password}

    session = requests.session()
    response = session.post(url, data=payload, verify=False)

    if response.status_code != 200 or "html" in response.text.lower():
        print("Login failed!")
        return None
    return session


# ------------------------------------------
#  Get control connection stats per device
#  (/device/control/connection?state=up/down)
# ------------------------------------------
def get_control_connection_count(session):
    url = f"{vmanage_host}/dataservice/device/control/connections"
    response = session.get(url, verify=False)

    if response.status_code != 200:
        print("Failed to fetch connection data")
        return []

    return response.json().get("data", [])



# ---------------------------------------------------
#  Get device configuration (expected control peers)
# ---------------------------------------------------
def get_expected_control_peers(session):
    url = f"{vmanage_host}/dataservice/device"
    response = session.get(url, verify=False)

    if response.status_code != 200:
        print("Failed to fetch device list")
        return []

    return response.json().get("data", [])


# -------------------------------------------------------
#  Compare actual UP connections vs configured connections
# -------------------------------------------------------
def find_low_control_connections(expected_list, actual_list):

    low_devices = []

    # Build a map for actual UP control connections
    actual_map = {}
    for entry in actual_list:
        sys_ip = entry.get("system-ip")
        if sys_ip:
            actual_map[sys_ip] = entry.get("controlConnectionsUp", 0)

    # Parse expected control connections from device list
    for device in expected_list:
        sys_ip = device.get("system-ip")

        expected = device.get("controlConnections", 0)  # configured
        actual = actual_map.get(sys_ip, 0)               # actual UP

        if actual < expected:
            low_devices.append({
                "hostname": device.get("host-name"),
                "system_ip": sys_ip,
                "device_model": device.get("device-model"),
                "expected_control_connections": expected,
                "actual_up_connections": actual
            })

    return low_devices


# -------------------------
#  MAIN SECTION
# -------------------------
if __name__ == "__main__":
    session = get_session()
    
    if not session:
        exit()

    expected_list = get_expected_control_peers(session)
    actual_list = get_control_connection_count(session)

    low_devices = find_low_control_connections(expected_list, actual_list)

    print("\n=== DEVICES WITH LOW CONTROL CONNECTIONS ===")
    if not low_devices:
        print("All devices have correct number of control connections.")
    else:
        for d in low_devices:
            print(
                f"{d['hostname']} | {d['system_ip']} | "
                f"Model: {d['device_model']} | "
                f"Expected: {d['expected_control_connections']} | "
                f"UP: {d['actual_up_connections']}"
            )
