# Warchest
 
Hello, this is Warchest-Lite developed by Adrià Espejo

All the documentation used is in the Documentation folder with an added UML Diagram of the whole architecture implemented

All the source code is in the src Folder

Within the src folder we can see all the classes of all entities in our game plus a folder 'db' that acts as a database in a JSON format. RecordManager.py manages this JSON database.

The Game class is the root of all, you can play executing Game.py. No external libraries are needed, so no need for pip install-ing anything.

The Board class is where all the logic of the board takes place and is queried. The Board gets filled with instances of Piece

Piece is a superclass for the different kind of Pieces (Archer, Crossbowman, Knight, Mercenary and Royal) for each piece is stored the team or clan which it belongs and the logic of the moves.

Player class is who acts on every turn and does every action that is stated in Warchest documentation.

RecordManager is a miniclass that manages a JSON files with a specific structure of (name, points, date). When a game is finished the points of each individual get stored and is sorted accordingly.



