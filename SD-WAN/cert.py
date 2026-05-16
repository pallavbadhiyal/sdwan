import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"


# -------------------------------
# Authentication
# -------------------------------
def get_session():
    login_url = f"{vmanage_host}/j_security_check"
    payload = {"j_username": username, "j_password": password}

    session = requests.session()
    response = session.post(login_url, data=payload, verify=False)

    if response.status_code != 200 or "html" in response.text.lower():
        print("Login failed! Check credentials.")
        return None

    return session


# -------------------------------
# Get certificate details
# -------------------------------
def get_certificate_info(session):
    # url = f"{vmanage_host}/dataservice/certificate/device"
    url = f"{vmanage_host}/dataservice/certificate/vedge/list"
    # url = f"{vmanage_host}/dataservice/certificate/status"
    response = session.get(url, verify=False)

    if response.status_code != 200:
        print("Failed to fetch certificate data")
        return []

    return response.json().get("data", [])


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    session = get_session()
    if not session:
        exit()

    cert_data = get_certificate_info(session)

    print("\n=== SD-WAN DEVICE CERTIFICATE EXPIRY ===\n")
    for d in cert_data:
        # print(d)
        print(
            f"{d.get('host-name')} | "
            f"{d.get('system-ip')} | "
            f"Expiry: {d.get('expirationStatus')} | "
            f"Expiry Date: {d.get('expirationDate')} | "
            f"status: {d.get('certInstallStatus')}"
        )
