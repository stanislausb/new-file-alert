import config
import json
import requests
import model
import showcodes


def post_alert(alert):
    showcode = alert.showcode
    project = showcodes.code[showcode]
    url = config.webhook_url[showcode]

    payload = (
        '{ "text":"'
        + "🚨 New "
        + alert.file_type
        + " have been uploaded for "
        + project
        + " - Episode "
        + alert.episode
        + ", cue number "
        + alert.cue_nr
        + ' 🚨"}'
    )

    print(payload)
    #      🚨 New stems have been uploaded for Horton - Episode 119, cue number 1M02 🚨

    response = requests.post(
        url=url, json=json.loads(payload), headers={"Content-Type": "application/json"}
    )
    print(response)


if __name__ == "__main__":
    alert = model.fileName(
        project="HOR", episode="119", cue_nr="1M01", file_type="stems"
    )
    post_alert(alert)
