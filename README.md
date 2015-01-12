# tb3util
Backup and convert your Roland TB-3 patches to MIDI and vice versa.

WARNING: Be sure to take a backup of your TB-3 patches before you use TB3Util. The codebase is still very much in development and may have bugs which could result in patches getting messed up.

Currently this project is just a command line utility. If command line scares you, check back a bit later.
I plan on making mananaging this process much more streamlined and potentially with a GUI.

Current functionality is able to import and export from the TB-3 with a few Caveats:

1. You can't pick and choose specific patches you want to change (Coming Soon)
Instead you must export all 64 patches from the TB-3 into a folder and replace those patches. 
2. When converting from PRM to MIDI, information about the last beat is lost. When you convert back to PRM from MIDI it will play everything you convert.

Dependencies: 

1. Python 2.7
2. python-midi

Example Usage:

A. Backup patches from TB-3 to MIDI files: python tb3cli.py prm G:/backup midi C:/Users/MyUsername/Desktop/midifolder

B. Restore patches from your MIDI folder to the TB-3: python tb3cli.py midi C:/Users/MyUsername/Desktop/midifolder prm G:/backup
