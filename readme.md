# NEW FILE ALERT IN GOOGLE CHAT 🚨

This program, when ran, gives an alert in different Google Workspaces when certain new files have been uploaded to the central repository (locally stored). 

Script is to be triggered every couple of minutes by an external program.


## Features

- Recursive search of a root directory
- Locally kept history of known files to improve performance
- Customizable showcodes 

## Install requirements:

`pip install -r ./requirements.txt`

## Set up your Google Spaces and showcodes

- Make a file called `config.py`
    - Make a variable called `root_dir` and fill in the root directory of where your search can start
    - Make a dictionary called `webhook_url` with as key the showcode and value the URL for your webhook
   ```python
   root_dir="PATH\TO\MY\SHARE"
   webhook_url = {
       'FOO':'http://webhookurl.com/FOO',
       'BAZ':'http://webhookurl.com/BAZ',
       'QUX': 'http://webhookurl.com/QUX'
   }
   ```
- In `showcodes.py`, add the translations for all showcodes
  ```python
  {
      'FOO':'Foo Bar'
      'BAZ':'Baz Buz'
      'QUX':'Qux Quux'
  }
  ```
- Make sure the showcodes in both files match


## TODO

- Make a central storage for showcode translations and webhook URL's ==> DB?
- Optimize performance
- Interface for configuring parameters
- ✔️Build regex into glob search 
- ✔️Streaming from file instead of loading to memory
