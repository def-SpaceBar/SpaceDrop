# SpaceDrop
My first Python Dropper.

The script currently need to run as Admin because adding a folder to the Excluded folders requires Admin privileges.
When I will find a method to bypass this I will update the script.

In order to download, execute and achieve persistence the script does the following things:

- Registry edits to set new Execution Policy to PS Scripts
- Add the %temp% environment variable to the excluded paths from Defender
- Drop the files by opening a shell by executing "shell32.dll" and run powershell encoded command under it.
- Auto Start-Up using Registry edits. At startup "conhost.exe" will run the payload from the target folder.
- Go over the script to know more :)
- MORE COMING SOON.
