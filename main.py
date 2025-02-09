import os
import glob
import model
import history
import config
import google_api
import showcodes

fileList = []

for path in glob.glob(config.root_dir+"/**/*.*", recursive=True):

    # Check of bestand al bekend is
    try:
        if path in history.getList():
            continue
    except:
        print("No history found, creating new one...")
    
    # Voeg toe aan historie
    history.add(path)

    # Ontleed bestandsnaam en locatie op de schijf
    location, filename = os.path.split(path)
    try:
        filename_elements = filename.split('_')
        location_elements = os.path.normpath(location).split(os.path.sep)    
        print("Filename Elements: ", filename_elements)
        print("Location Elements: ", location_elements)

        #Check of "01" ergens in de path zit (actief project), en check of de showcode bekend is
        if not(any("01" in word for word in location_elements)) or filename_elements[0] not in showcodes.code.keys():
            continue


        # Type bestand bepalen
        print("Nu in bestandsbepaling")
        for element in location_elements:
            match element:
                case '04_STEMS':
                    file_type = "stems"
                case 'CUES FOR PREVIEW':
                    file_type = "cue for preview"
                case _:
                    file_type = "unknown filetype"

        print("File Type: ", file_type)
        # Voeg toe aan lijst 
        fileList.append(
            model.fileName(
                showcode    =   filename_elements[0],
                episode     =   filename_elements[1],
                cue_nr      =   filename_elements[2],
                file_type   =   file_type

            )
        )
    except:
        print("File not elligable for alert: " + filename)
    

print("File List: ", fileList)
# Maak alerts aan
alerts = []
for file in fileList:
    if file not in alerts:
        alerts.append(file)


# Verstuur alerts via google api 
for alert in alerts:
    google_api.post_alert(alert)
