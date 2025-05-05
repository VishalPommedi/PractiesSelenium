import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

def test_create_issue_type():
    base_url = os.getenv('Jira_Base_URL')
    end_point = "rest/api/3/issuetype"
    full_url = f'{base_url}{end_point}'
    print(full_url)
    pay_load = {
        "description": "Automation issue type is used to create automation tickets separatly",
        "name": "Automation-2",
        "type": "standard"
    }
    header = {
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }

    email_id = os.getenv('Jira_email')
    api_key = os.getenv('Jira_API_Key')

    auth = HTTPBasicAuth(email_id, api_key)

    request = requests.post(full_url, headers=header, auth=auth, json=pay_load)

    status_code = request.status_code
    output_data = request.json()

    print(f'{status_code}\n{output_data}')

    assert status_code == 201