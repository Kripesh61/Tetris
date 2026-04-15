What is this game?

This is a Tetris game I built using Python and the Pygame library. It has the classic gameplay of fitting blocks together, but I added a "Bomb" mechanic. Every now and then, a piece will act as a bomb and clear out a 3x3 area around it when it lands. It also includes a high-score system and retro sound effects.

    #  How to Run it (on Mac):

Open your Terminal.

Type cd Desktop/tetris and hit Enter.

Run the game by typing: python3 main.py



   # Controls:

Left/Right Arrows: Move the pieces.

Up Arrow: Rotate the piece.

Down Arrow: Make the piece fall faster.

Space Bar: Hard drop (makes the piece land instantly).


    #  The Files in this Project:

main.py: This is the heart of the game. It runs the "Game Loop," handles the animations, and plays the music.

game_objects.py: This is where all the math happens. It handles the grid, the shapes, and the scoring.

constants.py: I put all my settings here, like the colors (RGB values) and the screen size, so the other files stay clean.

high_score.txt: A simple text file that saves the best score so it doesn't disappear when you close the game.

Sounds: I used bgm.mp3 for the music and .wav files for the "place," "explode," and "game over" sounds.


    # How the Code Works (OOP & Functions):

The "Piece" Class:
I used a class to represent the Tetris blocks. This makes it easy to create new pieces. Each piece "knows" its own position (X and Y), its color, its shape, and whether or not it is a "Bomb" piece.








