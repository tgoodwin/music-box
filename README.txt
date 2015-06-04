Music Grid
by Tim Goodwin
2013

The Music Grid program creates ambient sound textures based on an x-y arrangement of user selected notes. 
The Grid is 16x16, where the y-axis represents two scales of the ionian mode. Each row on the grid is assigned to a note. 
The x-axis can be thought of as one measure of music where each column is a 16th note subdivision. The program repeats this measure until the user signals the program to stop.

Upon initialization, the user uses a mouse or trackpad to select squares by clicking on them. The user can unselect squares by clicking on a selected square. 
Once the user has chosen a selection of squares and presses any key, the program will begin to interpret the user's selection into sound. 
The program starts at the left most column and scans through it from top to bottom to see if the column contains any selected squares. If there are squares selected in the column, the program will play each note assigned to each selected square simultaneously. 
The program then moves to the next column and repeats the process for every column. 
Once the program finishes scanning the last column, it will move back to the first column and repeat the process until the user presses any key, at which point the grid will be cleared of all selected notes and audio playback will stop. 

Common sources of error with this program:
Make sure the folder 'samples' is contained within the same directory as the program file.
Make sure pygame and python are installed and running properly on your machine. 
Make sure your computer can play audio through internal or external speakers and that the volume is not set to zero. 

Music Grid and all audio samples are copyrighted by Tim Goodwin - timg.goodwin@gmail.com
