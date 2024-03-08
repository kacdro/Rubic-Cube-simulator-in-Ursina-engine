# Rubic-Cube-simulator-in-Ursina-engine

Project Objective:

The project's goal was to create a three-dimensional model of a Rubik's Cube. Part of the project involved designing cube movements and additional functionalities such as undoing moves and reviewing gameplay.

Technologies:

The project was implemented in the Python programming language within the PyCharm development environment. It utilized the Ursina engine and functions such as itertools and time to determine animation timing. The cubic cube model was created using Blender software.

Execution:

To run the project, you will need a development environment (e.g., PyCharm). You should add the files Model.obj and ModelKostki.png to the newly created project, which are responsible for the program's graphical appearance. Then you can proceed with compiling the code.

Functionality:

The program initially iterates through the coordinates of successive cube models using the itertools function and overlays the cube model on them. Subsequently, using vectors and inheritance functions, the physics of Rubik's Cube movements are created. Controlling the model is done using the keyboard. Changes in perspective can be made by holding down the right mouse button and simultaneously moving it. By clicking the appropriate buttons, the user can undo cube movements or enable the option to review their moves (in this mode, undoing and adding moves is not possible).


![Zrzut ekranu 2024-03-08 190010](https://github.com/kacdro/Rubic-Cube-simulator-in-Ursina-engine/assets/100469610/5f267ae4-5ac1-42ce-ae35-4ff1dd82c413)



The most important functions of the program include:

- def parent_kid_inherit(): A function for inheriting the position of the cube to determine its position after rotation.

- def input(key): It reads keyboard inputs and triggers the appropriate functions.

- def replay_moves(): A function responsible for reviewing gameplay.

- def is_overview(): A function that displays a message on the screen when the overview mode is activated.

- def reverse(): A function responsible for undoing cube movements.

- def reset_cube(): A function that resets the cube to its initial state.

- def reset_camera(): It restores the camera to its initial position.

