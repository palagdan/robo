##  2023 Daniil Palagin

# Robot AI

## Table of contents

* [Project Description](#Project-Description)
* [Modes](#modes)
* [Installation](#installation)
* [Settings](#settings)
* [Usage](#usage)
* [Guide for creating map](#guide-for-creating-map)
## Project Description
We have a maze and in it are placed the mazes. 
To do this, we have a group of robots that have the task of collecting the mazes. 
Each robot carries only one maze. 
Somewhere on the map is the collection point for the wandering robots.
We would like to collect as many mazes as possible in the shortest time.

## Modes
* **Information Mode**: In this mode, all robots have access to the positions of all mazes on the grid. 
This means that they know the location of each maze without the need for communication or exploration.
* **Cooperation Mode**: In Cooperation Mode, the robots do not know the positions of the mazes initially. 
Instead, they rely on a common database to communicate and share information about the explored cells and mazes.
As they explore the grid, they update the common database with the discovered information, allowing other robots to benefit from it.
* **Mute Mode**: In Mute Mode, the robots also do not have prior knowledge of the maze positions. 
However, in this mode, they do not communicate with each other. Instead, each robot maintains its own
individual database of explored cells and mazes. They rely solely on their own exploration to build their 
databases without sharing or receiving information from other robots.


## Installation
To run this program, you will need to have the Pygame library installed in your Python environment. </br>
[1] Install Pygame by running the following command:
```console
$ pip install pygame
```
## Settings
* **Maps**: The /maps directory serves as the location for storing the maps. 
This directory holds the files that represent the grid mazes.
* **Adding a new map**: To add a new map, you need to create a new .txt file that contains the grid maze representation. 
This file should be added to the /maps directory, allowing the program to recognize it as a new map.
* **Fonts**: The /fonts directory server as the location for storing the fonts.

## Usage
To run program use this command in the terminal:
```console
$ python3 main.py
```
To run test use this command in the terminal:
```console
$ pytest tests/
```

## Guide for creating map
### Symbols:
- X - Walls
- R - Robot
- M - mazes
- 0 - collecting point <br>
- " " - path
### Rules: 
- Ensure that every path on the map is accessible, with no impeding deadends. Example of bad maze:
```text
XXXXXXXXXXX
X R     M X
X      XXXX
X   0  X  X
XXXXXXXXXXX
```
Correct maze:
```text
XXXXXXXXXXX
X R     M X
X      XXXX
X   0     X
XXXXXXXXXXX
```
