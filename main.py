import os
import glob
import model
import history
import config
import google_api

fileList = []

for path in glob.glob(config.root_dir+"/**/*", recursive=True):
    
    # Check of bestand al bekend is
    if path in history.getList():
        continue
    
    # Ontleed bestandsnaam en locatie op de schijf
    location, filename = os.path.split(path)
    filename_elements = filename.split('_')
    location_elements = os.path.normpath(location).split(os.path.sep)    
    
    # Voeg toe aan lijst 
    fileList.append(
        model.fileName(
            project     =   filename_elements[0],
            episode     =   filename_elements[1],
            file_type   =   filename_elements[2],
        )
    )
alerts = []
for file in fileList:
    if file not in alerts:
        alerts.append(file)

# Maak alert in google chat
google_api.alert(project, episode, file_type)

# Voeg toe aan historie
history.add(path)
