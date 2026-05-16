import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"



# ----------------------------------------
# Authentication (session cookie)
# ----------------------------------------
def get_session():
    url = f"{vmanage_host}/j_security_check"
    payload = {"j_username": username, "j_password": password}

    session = requests.session()
    response = session.post(url, data=payload, verify=False)

    # If login fails, vManage returns HTML login page
    if response.status_code != 200 or "html" in response.text.lower():
        print("Login failed! Check credentials.")
        return None

    return session


# ----------------------------------------
# Get BFD session information
# ----------------------------------------
def get_bfd_info(session):
    url = f"{vmanage_host}/dataservice/device/bfd/sessions"
    response = session.get(url, verify=False)

    if response.status_code != 200:
        print("Failed to fetch BFD data")
        return []

    print(response.json().get("data", []))

# ----------------------------------------
# Filter DOWN BFD tunnels
# ----------------------------------------
def get_down_bfd_tunnels(bfd_list):
    down = []
    for session in bfd_list:
        if session.get("state") != "up":
            down.append({
                "system_ip": session.get("system-ip"),
                "peer_system_ip": session.get("peer-system-ip"),
                "site_id": session.get("site-id"),
                "color": session.get("color"),
                "state": session.get("state"),
                "src_if": session.get("src-interface")
            })
    return down


# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    session = get_session()
      if not session:
        exit()

    bfd_data = get_bfd_info(session)
    down_bfd = get_down_bfd_tunnels(bfd_data)

    print("\n=== DOWN BFD TUNNELS ===\n")
    if not down_bfd:
        print("All BFD tunnels are UP")
    else:
        for t in down_bfd:
            print(
                f"{t['system_ip']} → {t['peer_system_ip']} | "
                f"Site: {t['site_id']} | Color: {t['color']} | "
                f"State: {t['state']} | Interface: {t['src_if']}"
            )
