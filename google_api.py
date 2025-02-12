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
        + ", cue "
        + alert.cue_nr
        + ' 🚨"}'
    )

    #      🚨 New stems have been uploaded for Horton - Episode 119, cue 1M02 🚨

    response = requests.post(
        url=url, json=json.loads(payload), headers={"Content-Type": "application/json"}
    )
    if response.status_code == '200':
        print(f"Alert sent for: {project}-{alert.episode}-{alert.cue_nr} ({alert.file_type})" )
    else:
        print("Something went wrong sending alert for: ", alert.filePath, "\n", response)


if __name__ == "__main__":
    alert = model.fileName(
        project="HOR", episode="119", cue_nr="1M01", file_type="stems"
    )
    post_alert(alert)
