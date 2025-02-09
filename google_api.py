import config
import json
import requests
import model

def post_alert(alert):
    project = alert.project
    url = config.webhook_url[project]
    print("===========URL=============")
    print(url)
    print("\n\n\n\n")
    payload = (
        '{ "text":"'
        +'New '
        + alert.file_type
        +' have been uploaded for '
        + alert.project +' - Episode ' + alert.episode
        + '"}'
    )
    #       New stems have been uploaded for Horton - Episode 119
    print("=======PAYLOAD========")
    print(payload)
    print("\n\n\n\n")
    response = requests.post(
        url=url,
        json=json.loads(payload),
        headers={"Content-Type": "application/json"}
    )
    print(response)

if __name__ == "__main__":
    alert = model.fileName(
        project     = "HOR",
        episode     = "119",
        cue_nr      = "1M01",
        file_type   = "stems"
    )
    post_alert(alert)