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

    # Create a new Tenant
    tenant_name = "tenant-api"
    result = client.tenants.post(name=tenant_name)
    print(result)




if __name__ == "__main__":
    main()
