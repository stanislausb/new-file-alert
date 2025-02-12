import os
import glob
import model
import history
import config
import google_api
import showcodes
import time

fileList = []

for path in glob.glob(config.root_dir + "./01*/**/*.*", recursive=True):

    # Check of bestand al bekend is
    try:
        if history.exists(path):
            continue
    except:
        print("No history found, creating new one..............\n")
        history.fillHistory()
        print("\nDone! Please run the script again to start polling for new files.")
        break

    # Voeg toe aan historie
    history.add(path)

    # Ontleed bestandsnaam en locatie op de schijf
    location, filename = os.path.split(path)
    try:
        filename_elements = filename.split("_")
        location_elements = os.path.normpath(location).split(os.path.sep)
        #print("Filename Elements: ", filename_elements)
        #print("Location Elements: ", location_elements)

        # Check of showcode bekend is
        if filename_elements[0] not in showcodes.code.keys():
            continue

        # Type bestand bepalen
        for element in location_elements:
            match element:
                case "04_STEMS":
                    file_type = "stems"
                case "CUES FOR PREVIEW":
                    file_type = "cue for preview"
                case _:
                    file_type = "unknown filetype"

        print("File Type: ", file_type)
        # Voeg toe aan lijst
        fileList.append(
            model.fileName(
                showcode=filename_elements[0],
                episode=filename_elements[1],
                cue_nr=filename_elements[2],
                file_type=file_type,
                filePath=path
            )
        )
        print("Added file to alert list: " + filename)
    except:
        print("File not elligable for alert: " + filename)


# Maak alerts aan
alerts = []
for file in fileList:
    if file not in alerts:
        alerts.append(file)


# Verstuur alerts via google api
for alert in alerts:
    time.sleep(1)
    google_api.post_alert(alert)
    
