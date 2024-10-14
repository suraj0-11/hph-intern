import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://suraj-krisp.atlassian.net/rest/api/3/issue/BYT-6"  # Replace {issue_key} with the actual issue key

# Retrieve credentials from environment variables
jira_email = os.getenv("JIRA_EMAIL")
jira_api_token = os.getenv("JIRA_API_TOKEN")

# Ensure environment variables are set
if not jira_email or not jira_api_token:
    raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set.")

# Replace with the actual issue key you want to delete
issue_key = "BYT-6"  # Replace with the actual issue key you want to delete
delete_url = f"https://suraj-krisp.atlassian.net/rest/api/3/issue/{issue_key}"

# Send DELETE request to Jira API
response = requests.delete(
    delete_url,
    auth=(jira_email, jira_api_token),
    headers={"Accept": "application/json"}
)

# Check the response
if response.status_code == 204:
    print(f"Issue {issue_key} deleted successfully.")
elif response.status_code == 404:
    print(f"Issue {issue_key} not found or you don't have permission to delete it.")
else:
    print(f"Failed to delete the issue. Status Code: {response.status_code}")
    print(response.text)
