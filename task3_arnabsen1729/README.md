## Task-3
Date: 05-Oct-20

### Problem Statement

**CLI Tic Tac Toe**
CLI based Tic Tac Toe with 2 players. 

### My Approach

Since, there are only two users, and no centralised server, the game logic will reside in each file. So I created a `TicTacToe` class. The class has the following methods:

| METHODS | DESCRIPTION |
|---|---|---|
|  `p1Move()` | Ask Player 1's move and will keep asking untill it gets a valid input |
|  `p2Move()` | Ask Player 2's move and will keep asking untill it gets a valid input |
| `find_winner()` | Will find the winner at the current state of the game and return the value |
| `display_board()` | Display's the board neatly | 
| `isGameOver()` | will decide if the game is over | 

Now, let's discuss how I have decided the logic of the game. I am storing the board in a linear array of 9 elements, initially they have 0 else if p1 made a move it will be +1 else for p2 it will be -1. Now to check we will check if the rows, cols, diagonals and anti-diagonals have +3 or -3 if so then there is a winner else no winner. 

One optimisation instead of going through the entire board every single time, I am looking at the corresponding rows, and cols, and diags of the last move, because only that will decide the game.

For the client and server script its simple socket programming. 


### Sample

[task3](./assets/task3.gif)


### Resources

1. [Task 3 Problem Statement and guide](https://drive.google.com/file/d/1e21ZnkQWjPuKd1RP34fFvJ8d7bWEihC8/view)

Thanks to [@lugnitdgp](https://github.com/lugnitdgp) for their awesome guidance <3 