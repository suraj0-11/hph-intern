# 🚀 Project Repository as a Intern of Emeelan.com

Welcome to the **Project Repository**, featuring multiple projects that explore various tools and frameworks. Below is a breakdown of each directory with a short description and highlights.

---

## 📂 Project Structure

### 1. **[electron-react-gemini-chatbot](./electron-react-gemini-chatbot)**
   - **Description**: A desktop-based chatbot application built with **Electron** and **React**, powered by **Google Gemini API** for intelligent responses.
   - **Key Features**:
     - ⚡ Cross-platform desktop app using Electron
     - ⚛️ Dynamic user interface with React
     - 🧠 Advanced chatbot functionality using Google Gemini AI

---

### 2. **[hcm_elk](./hcm_elk)**
   - **Description**: A project utilizing the **ELK stack** (Elasticsearch, Logstash, Kibana) for human capital management (HCM) data analytics.
   - **Key Features**:
     - 📊 Data ingestion and transformation with Logstash
     - 🔍 Powerful search and indexing using Elasticsearch
     - 📈 Visual reports and dashboards with Kibana

---

### 3. **[jira](./jira)**
   - **Description**: Automation of tasks and issue tracking using the **Jira API**, with scripts to streamline workflows.
   - **Key Features**:
     - 🤖 Automation of common Jira tasks
     - 📝 API integration for issue tracking and management
     - 🔄 Workflow optimization for project management

---

### 4. **[junkins/jenkins-101](./junkins/jenkins-101)**
   - **Description**: An introduction to **Jenkins**, covering setup, configuration, and CI/CD pipeline creation.
   - **Key Features**:
     - 🛠️ Step-by-step Jenkins setup guide
     - 🚀 CI/CD pipeline examples for automation
     - 🔧 Integration with version control and deployment tools

---

<h1>Jira Issues Automation using Python</h1>

<p>This script automates the creation of Jira issues using the Jira REST API. It is designed to interact with a Jira project and automatically log issue details such as test results, error messages, and more. Below is an explanation of how the code works and a guide to some important features.</p>

<h2>Prerequisites</h2>

<ul>
    <li><strong>Jira account</strong>: Make sure you have an account with the necessary permissions to create issues in your Jira project.</li>
    <li><strong>Jira API Token</strong>: You can generate your API token from your Jira account settings. See <a href="https://confluence.atlassian.com/cloud/api-tokens-938839638.html" target="_blank">Jira API Token Documentation</a>.</li>
    <li><strong>Python 3.x</strong>: Ensure you have Python installed. You can download it from <a href="https://www.python.org/downloads/" target="_blank">Python's official site</a>.</li>
    <li><strong>Requests library</strong>: This is a popular Python library for making HTTP requests.</li>
</ul>

<pre><code>pip install requests
</code></pre>

<ul>
    <li><strong>Dotenv library</strong>: This is used to load environment variables from a <code>.env</code> file.</li>
</ul>

<pre><code>pip install python-dotenv
</code></pre>

<h2>Environment Setup</h2>

<p>Before running the script, you'll need to create a <code>.env</code> file to store your Jira email and API token:</p>

<pre><code>JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
</code></pre>

<p>The script loads these environment variables at the beginning:</p>

<pre><code>from dotenv import load_dotenv
load_dotenv()
</code></pre>

<p>This ensures that sensitive data (like your API token) is not hardcoded in the script.</p>

<h2>Script Breakdown</h2>

<h3>Importing Required Libraries</h3>

<pre><code>import os
import requests
import json
from dotenv import load_dotenv
</code></pre>

<ul>
    <li><strong>os</strong>: Used to load environment variables.</li>
    <li><strong>requests</strong>: Used to make HTTP requests to the Jira API.</li>
    <li><strong>json</strong>: Handles JSON payload creation and parsing.</li>
    <li><strong>dotenv</strong>: Loads environment variables from the <code>.env</code> file.</li>
</ul>

<h3>Jira API Setup</h3>

<pre><code>url = "https://suraj-krisp.atlassian.net/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
</code></pre>

<ul>
    <li><strong>url</strong>: This is the endpoint for creating issues in Jira. It is specific to your Jira account (replace <code>suraj-krisp</code> with your Jira instance).</li>
    <li><strong>headers</strong>: These define the format of the request and the response.</li>
</ul>

<h3>Authentication</h3>

<p>The script uses environment variables for your Jira email and API token:</p>

<pre><code>jira_email = os.getenv("JIRA_EMAIL")
jira_api_token = os.getenv("JIRA_API_TOKEN")
</code></pre>

<p>If these are not set, an error is raised:</p>

<pre><code>if not jira_email or not jira_api_token:
    raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables must be set.")
</code></pre>

<h3>Issue Creation Payload</h3>

<p>The payload contains details of the Jira issue to be created:</p>

<pre><code>payload = json.dumps({
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
</code></pre>

<ul>
    <li><strong>project.key</strong>: This is the project key in Jira where the issue will be created (e.g., <code>BYT</code>).</li>
    <li><strong>summary</strong>: A brief summary of the issue.</li>
    <li><strong>description</strong>: A detailed description of the issue, using the Atlassian Document Format (ADF).</li>
    <li><strong>issuetype</strong>: Specifies the type of the issue, in this case, a "Bug."</li>
</ul>

<h3>Creating the Issue</h3>

<p>The script sends a POST request to the Jira API to create the issue:</p>

<pre><code>response = requests.post(
    url,
    data=payload,
    headers=headers,
    auth=(jira_email, jira_api_token)
)
</code></pre>

<ul>
    <li><strong>auth</strong>: Uses your email and API token to authenticate with Jira.</li>
</ul>

<p>If the request is successful (status code 201), a success message is printed:</p>

<pre><code>if response.status_code == 201:
    print("Issue created successfully.")
else:
    print("Failed to create issue:", response.status_code, response.text)
</code></pre>

<h2>Atlassian Document Format (ADF)</h2>

<p>The <code>description_adf</code> variable uses ADF to format the issue description with headings, tables, and code blocks:</p>

<pre><code>description_adf = {
    "version": 1,
    "type": "doc",
    ...
}
</code></pre>

<p>This section contains a structured format for describing the test results, request/response JSON, and other information.</p>

<p>To learn more about the Atlassian Document Format, visit the <a href="https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/" target="_blank">Atlassian Documentation</a>.</p>

<h2>Example Issue Data</h2>

<p>Here's an example of what the payload looks like:</p>

<ul>
    <li><strong>Project Key</strong>: <code>BYT</code></li>
    <li><strong>Summary</strong>: "Login Test Failure: SQL Injection attempt"</li>
    <li><strong>Test Results</strong>: Includes status, response time, and failure description.</li>
    <li><strong>Request JSON</strong>: Shows the test payload used.</li>
    <li><strong>Response JSON</strong>: Displays the response from the server.</li>
    <li><strong>Assertions</strong>: Compares expected results with actual results.</li>
</ul>

<h2>Useful Links</h2>

<ul>
    <li><a href="https://developer.atlassian.com/cloud/jira/platform/rest/v3/" target="_blank">Jira REST API Documentation</a></li>
    <li><a href="https://docs.python-requests.org/en/latest/" target="_blank">Python Requests Documentation</a></li>
    <li><a href="https://pypi.org/project/python-dotenv/" target="_blank">Using Environment Variables in Python</a></li>
</ul>

<p>Feel free to modify the script according to your project needs. This automation is flexible and can be adapted for various use cases like test automation, bug tracking, and project management.</p>

