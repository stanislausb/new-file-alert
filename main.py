import os
import glob
import model
import history
import config
import google_api

fileList = []

for path in glob.glob(config.root_dir+"/**/*", recursive=True):
    
    # Check of bestand al bekend is
    if path in history.getList() or not(path.startswith("01.")):
        continue
    
    # Ontleed bestandsnaam en locatie op de schijf
    location, filename = os.path.split(path)
    filename_elements = filename.split('_')
    location_elements = os.path.normpath(location).split(os.path.sep)    
    
    # Type bestand bepalen
    for element in location_elements:
        match element:
            case '04_STEMS':
                file_type = "Stems"
            case 'CUES FOR PREVIEW':
                file_type = "cue for preview"

    # Voeg toe aan lijst 
    fileList.append(
        model.fileName(
            project     =   filename_elements[0],
            episode     =   filename_elements[1],
            cue_nr      =   filename_elements[2],
            file_type   =   file_type
            
        )
    )

    # Voeg toe aan historie
    history.add(path)

# Maak alerts aan
alerts = []
for file in fileList:
    if file not in alerts:
        alerts.append(file)

# Verstuur alerts via google api 
for alert in alerts:
    google_api.alert(alert)
