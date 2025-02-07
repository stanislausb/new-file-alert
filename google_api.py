import config
import json
import requests

def post_alert(alert):
    url = config.webhook_url
    payload = (
        '{ "text":"'
        +'New '
        + file_type
        +' has been uploaded for '
        + project +' - Episode ' + episode
        + '"}'
    )
    response = requests.post(
        url=url,
        json=json.loads(payload),
        headers={"Content-Type": "application/json"}
    )
    print(response)