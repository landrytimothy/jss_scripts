# jss_scripts
A collection of scripts I use in my JSS workflows. 

## unenroll.py
This script is intended to be tied on to the beginning of a reimage policy. 
You will need to fill in your API credentials and base url in order for the client to interact with the JSS_Server. 

Workflow is documented here: http://timothylandry.com/post/1-click-imaging/

## rename.sh
Renaming script, grabs last 6 digits of the serial number and prepends "OSX-". Intended for use in a DEP workflow prior to AD binding. 
