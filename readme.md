# NEW FILE ALERT IN GOOGLE CHAT

A script that gives an alert in different Google Workspaces when certain new files have been uploaded. 

Script is to be triggered every couple of minutes by an external program.


## Features

- Recursive search of a root directory
- Locally kept history of known files to improve performance
- Customizable showcodes 

## Install requirements:

`pip install -r ./requirements.txt`

## Set up your Google Spaces and showcodes

- In `config.py`, add your webhook URL to the corresponding showcode (given that every showcode has their own Space
- In `showcodes.py`, add the translations for all showcodes
- Make sure both lists are the same


## TODO

- Make a central storage for showcode translations and webhook URL's ==> DB?
- Optimize performance
- Interface for configuring parameters
