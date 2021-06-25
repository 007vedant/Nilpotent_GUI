Developer: Vedant Raghuwanshi(118EE0705)

Project: Check if the matrix is Nilpotent

Course: Advanced Control System (EE2002)


Overview:

1.The project contains three main directories viz. build, src and dist. All the source code for project is present inside the src directory. Each of the src files can be run as an individual script or the entire Graphical User Interface(GUI) can be launched via main.py script. The dist directory also contain an MSI-installer setup for the project.

2.The build directory contains the executable(.exe) and all the associated runtime files. The path to the executable is build -> exe.win-amd64-3.9 -> App.exe. The application can be launched by opening App.exe file.

3.The app is cross-platform, although for a few UNIX systems, may require appropriate modifications inside setup.py to build again.

4. If the app does not open by launching App.exe file (Python packaging issues), you can install it from the setup inside 'dist' directory.


Instructions for using the App:

1. Launch the GUI by opening the App.exe file.
2. Enter the size of your input matrix inside the box and click 'Run'.
3. A window will popup with a matrix of the given size, with all the default values as inf.
4. Click on each cell, enter the number you want to input in that cell and press 'Enter' to fix it inside the cell.
5. After you've entered all the numbers for the matrix, press 'Space'.
6. A window will popup with the message about the kind of matrix.


NOTE:
1. The App supports complex numbers, which should be input as Python requires them to be. Do not add whitespace between any operands while entering the numbers.
   Correct Examples: 1+2j, -1-2j, 1.0-2.0j, 0j, 1.11+3.2j

2. The App does not support 'BackSpace', press 'Delete' to remove the entire number.
3. Press 'Enter' after typing the number to register it inside the cell, else it'll take the default 'inf' value.
4. Since calculations are not possible with 'inf' values, replace all the cells with your input values or else the App will throw an error via a popup window with message that 'inf' values are not accepted.


