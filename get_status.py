from dotenv import dotenv_values
import requests
import os

config = dotenv_values(".env")


def get_status():
    api_key = config['JIRA_API_KEY']
    jira_workspace = config['JIRA_WORKSPACE']
    updated_at = config['UPDATED_AT']
    users = config['JIRA_USERS']
    users_list = users.split(',')
    formatted_users = " OR ".join(
        [f"assignee = '{user.strip()}'" for user in users_list])

    headers = {
        "Authorization": f"Basic {api_key}",
        "Content-Type": "application/json"
    }

    params = {
        "jql": f"({formatted_users}) AND project = COM AND status changed during ({updated_at}, now())",
        "fields": "summary,status,assignee"
    }

    response = requests.get(
        f"{jira_workspace}/rest/api/2/search", headers=headers, params=params)
    data = response.json()

    f = open(os.path.join("output", "output.html"), "w")
    f.write(f"<html>\n")
    f.write(f"<body>\n")

    f.write(f"<table>\n")

    sorted_issues = sorted(
        data["issues"], key=lambda x: x["fields"]["assignee"]["displayName"])

    for issue in sorted_issues:
        id = issue["key"]
        summary = issue["fields"]["summary"]
        status = issue["fields"]["status"]["name"]
        assignee = issue["fields"]["assignee"]["displayName"]
        f.write(
            f"<tr><td><a href='{jira_workspace}/browse/{id}'>{id}</a></td><td>{summary}</td><td>{assignee}</td><td>{status}</td></tr>\n")

    f.write(f"</body>\n")


get_status()
