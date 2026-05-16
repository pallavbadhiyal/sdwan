import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"

session = requests.session()
url = f"{vmanage_host}/j_security_check"
payload = {"j_username": username, "j_password": password}
response = session.post(url, data=payload, verify=False)
session.headers["Content-Type"] = "application/json"
token_url = f"{vmanage_host}/dataservice/client/token"
tok_resp = session.get(url, verify=False)
print(response.status_code,response.text)
if response.status_code == 200:
    session.headers["X-XSRF-TOKEN"] = response.text

url = f"{vmanage_host}/dataservice/device/bfd/sessions"
bfd_resp = session.get(url, verify=False)

print(bfd_resp.status_code)
print(bfd_resp.text)
# bfd = bfd_resp.json().get('data', [])

# # print(bfd)
# print(json.dumps(bfd, indent=4))

#     if response.status_code != 200:
#         print(response.status_code)
#         print("Failed to fetch BFD data")
#         return []

#     print(response.json().get("data", []))

# def get_token(session):


# # ----------------------------------------
# # Filter DOWN BFD tunnels
# # ----------------------------------------
# def get_down_bfd_tunnels(bfd_list):
#     down = []
#     for session in bfd_list:
#         if session.get("state") != "up":
#             down.append({
#                 "system_ip": session.get("system-ip"),
#                 "peer_system_ip": session.get("peer-system-ip"),
#                 "site_id": session.get("site-id"),
#                 "color": session.get("color"),
#                 "state": session.get("state"),
#                 "src_if": session.get("src-interface")
#             })
#     return down


# # ----------------------------------------
# # MAIN
# # ----------------------------------------
# if __name__ == "__main__":
#     session = get_session()
#     get_token(session)
#     if not session:
#         exit()

#     bfd_data = get_bfd_info(session)
#     down_bfd = get_down_bfd_tunnels(bfd_data)

#     print("\n=== DOWN BFD TUNNELS ===\n")
#     if not down_bfd:
#         print("All BFD tunnels are UP")
#     else:
#         for t in down_bfd:
#             print(
#                 f"{t['system_ip']} → {t['peer_system_ip']} | "
#                 f"Site: {t['site_id']} | Color: {t['color']} | "
#                 f"State: {t['state']} | Interface: {t['src_if']}"
#             )
