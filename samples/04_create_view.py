import json
import os
from dotenv import load_dotenv, find_dotenv
from vastpy import VASTClient

############# MAIN ##############
def main():
    #load_dotenv(find_dotenv())  # Load the .env file.
    load_dotenv()  # Load the .env file.
    # Fetch variables from the .env file.
    API_USERNAME = os.getenv("API_USERNAME")
    API_PASSWORD = os.getenv("API_PASSWORD")
    VMS_IP = os.getenv("VMS_IP")

    client = VASTClient(user=API_USERNAME, password=API_PASSWORD, address=VMS_IP)

    # Create a new View in a specific Tenant
    tenant_name = "tenant-api"
    viewpolicy_name = "policy-api"
    view_name = "view-api"
    view_path = "/view-api"

    tenant_list = client.tenants.get(name=tenant_name)
    if not tenant_list:
        print(f"Tenant {tenant_name} doesn't exist.")
        exit(1)
    print(f"Tenant {tenant_name} found.")
    tenant = tenant_list[0]

    viewpolicy_list = client.viewpolicies.get(name=viewpolicy_name, tenant_id=tenant['id'])
    if not viewpolicy_list:
        print(f"Policy {viewpolicy_name} not found in Tenant {tenant_name}!")
        exit(1)
    print(f"Policy {viewpolicy_name} found in Tenant {tenant_name}!")
    viewpolicy = viewpolicy_list[0]

    view_list = client.views.post(name=view_name, path=view_path, tenant_id=tenant['id'], policy_id=viewpolicy['id'], create_dir=True)
    if view_list:
        print(f"View {view_name} created in Tenant {tenant_name}!")
    print(view_list)



if __name__ == "__main__":
    main()
