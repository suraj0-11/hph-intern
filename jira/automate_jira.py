import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
url = "https://suraj-krisp.atlassian.net/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
jira_email = os.getenv("JIRA_EMAIL")
jira_api_token = os.getenv("JIRA_API_TOKEN")
if not jira_email or not jira_api_token:
    raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set.")
description_adf = {
    "version": 1,
    "type": "doc",
    "content": [
        {
            "type": "heading",
            "attrs": {"level": 1},
            "content": [{"type": "text", "text": "Test Results"}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Test Information"}]
        },
        {
            "type": "table",
            "attrs": {"isNumberColumnEnabled": False, "layout": "default"},
            "content": [
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Status:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Failed", "marks": [{"type": "textColor", "attrs": {"color": "#FF0000"}}]}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Name:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Local login"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Response Status:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "400"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Response Time:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "0.003482"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Request URL:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "http://localhost:1437/api/auth/local"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "HTTP Method:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "POST"}]}]}
                    ]
                }
            ]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Test Description"}]
        },
        {
            "type": "paragraph",
            "content": [{"type": "text", "text": "Test login with SQL Injection attempt in email."}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Request JSON"}]
        },
        {
            "type": "codeBlock",
            "attrs": {"language": "json"},
            "content": [{"type": "text", "text": '{\n  "password": "Welcome@123",\n  "identifier": "devendramulewa171@gmail.com\'--"\n}'}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Response JSON"}]
        },
        {
            "type": "codeBlock",
            "attrs": {"language": "json"},
            "content": [{"type": "text", "text": '{\n  "data": null,\n  "error": {\n    "name": "ValidationError",\n    "status": 400,\n    "message": "Invalid identifier or password"\n  }\n}'}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Assertions"}]
        },
        {
            "type": "codeBlock",
            "attrs": {"language": "json"},
            "content": [{"type": "text", "text": '{\n  "assert value": 400,\n  "propertie_name": "status_code",\n  "assert_condition": "=="\n}\n{\n  "assert value": "Invalid identifier or password",\n  "propertie_name": "body.message",\n  "assert_condition": "contains"\n}'}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Failures"}]
        },
        {
            "type": "codeBlock",
            "attrs": {"language": "json"},
            "content": [{"type": "text", "text": '{\n  "actual": "Invalid identifier or password",\n  "expected": "identifier is not valid",\n  "property": "body.message"\n}'}]
        },
        {
            "type": "heading",
            "attrs": {"level": 2},
            "content": [{"type": "text", "text": "Response Headers"}]
        },
        {
            "type": "table",
            "attrs": {"isNumberColumnEnabled": False, "layout": "default"},
            "content": [
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Date:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Wed, 09 Oct 2024 11:26:59 GMT"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Vary:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Origin"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Connection:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "keep-alive"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Keep-Alive:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "timeout=5"}]}]}
                    ]
                },
                {
                    "type": "tableRow",
                    "content": [
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Content-Type:"}]}]},
                        {"type": "tableCell", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "application/json; charset=utf-8"}]}]}
                    ]
                }
            ]
        }
    ]
}
payload = json.dumps({
    "fields": {
        "project": {
            "key": "BYT"
        },
        "summary": "Login Test Failure: SQL Injection attempt",
        "description": description_adf,
        "issuetype": {
            "name": "Bug"
        }
    }
})
response = requests.post(
    url,
    data=payload,
    headers=headers,
    auth=(jira_email, jira_api_token)
)
if response.status_code == 201:
    print("Issue created successfully.")
else:
    print("Failed to create issue:", response.status_code, response.text)
