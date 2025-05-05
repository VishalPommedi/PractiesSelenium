# Learning the API testing with the Python programming language
"""
Below, I created a class called "JiraAPITesting". In that class, created a function called "getParticularProjectId"
to get a particular project Id from list of companies. To call the "getParticularProjectId" we need to pass two parameters.
1. End point
2. Project Name
"""

from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import requests
import os

# load the environment variables into current file
load_dotenv()

class JiraAPITesting:
    def __init__(self):
        self.baseUrl = os.getenv("Jira_Base_URL")
        self.emailId = os.getenv("Jira_email")
        self.apiKey = os.getenv("Jira_API_Key")

    def getParticularProjectId(self, endPoint, projectName):

        projectId = None
        headers = {
            "Accept" : "application/json"
        }
        Auth = HTTPBasicAuth(self.emailId, self.apiKey)
        response = requests.get(f'{self.baseUrl}{endPoint}', auth=Auth, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            print('Success!')
            # print("Data: ",response_data)
            for i in response_data:
                if i['name'] == projectName:
                    projectId = i['id']
                    print(f'Project Id: {projectId}')
                    break
            # Below if condition will check the project id wheather None or value
            if projectId:
                print('Found the Project Id!')
            else:
                print('Project Id not found!')    
            return projectId
        else:
            print(response.status_code)
            print(response.json())

    # Below function is used to get all types of issues along with the ids
    def get_all_issues(self, endpoint):
        all_Issues_Types = []
        response = requests.get(f'{self.baseUrl}{endpoint}', auth=HTTPBasicAuth(self.emailId, self.apiKey), headers={"Accept": "application/json"}) 
        res_data = response.json()
        if response.status_code == 200:
            print('success!')
            # print(response.json()) 
            for i in res_data:
                all_Issues_Types.append(i['name'])
            print(all_Issues_Types)                
        else:
            print('error!', response.status_code)
            print(response.json())

    def getIssueswithProjectId(self, endPoint, projectId):
        issues_list = {}
        query = {
            'projectId': projectId
            }
        print(f'{self.baseUrl}{endPoint}')
        response = requests.get(f'{self.baseUrl}{endPoint}', auth=HTTPBasicAuth(self.emailId, self.apiKey), headers={"Accept": "application/json" }, params=query) 
        payload = response.json()
        if response.status_code == 200:
            
            issues_list = {issue.get('name') : issue.get('id') for issue in payload}
            print(issues_list)    
        elif response.status_code == 404:
            print(f'status code: {response.status_code}')
            print(payload["errorMessages"])

        elif response.status_code == 400:
            print(f'status code: {response.status_code}')
            print(response.json()['errorMessages'])
            
                
        else:
            print('Get Issue type based  the project function got failed!')
            print(response.status_code, response.json())           



# emailId = "pommedichintu15980@gmail.com"
# baseUrl = "https://pommedi.atlassian.net"
getRecentProjects_endpoint = "/rest/api/3/project/recent"
getIssuesTypes_endpoint = "/rest/api/3/issuetype"
getIssueTypewithprojectId = "/rest/api/3/issuetype/project"



obj = JiraAPITesting()
projectName = "Learning Postman"
ProjectID = obj.getParticularProjectId(getRecentProjects_endpoint, "Automation test")
print(ProjectID)

obj.get_all_issues(getIssuesTypes_endpoint)
obj.getIssueswithProjectId(getIssueTypewithprojectId, ProjectID)

