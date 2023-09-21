# Get Jira Status

Get status of your tasks in JIRA in fancy way

This is a simple python script to get the status of a Jira ticket.

## Usage

Generate an API key in Jira using [link](https://id.atlassian.com/manage-profile/security/api-tokens)

Set `.env` file with the following variables:

```env
JIRA_API_KEY=<JIRA_API_TOKEN>
JIRA_API=https://yourworkspace.atlassian.net/rest/api/2/search
JIRA_USERS=John Smith,Adam Coal,Jeremy Island # USE YOUR TEAM'S JIRA USERS
UPDATED_AT=-5d # USE YOUR TIMEFRAME. SO IT WILL COLLECT TICKETS WHICH STATUS UPDATED IN THE LAST 5 DAYS
```

Package use Docker and `make` so it should be easy to run

```bash
make run
```

After successful you can check `output` folder for the result `output.html` file

Then just copy its content and paste it to your Google Sheet document

Have a good day! 🙂👋

## Development

Go to isolated environment, install dependencies and run the script

```bash
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
python3 get_status.py
```

To exit from isolated environment just run

```bash
deactivate
```

Run `./venv_start.sh` just for start already created virtual environment
