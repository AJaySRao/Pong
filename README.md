# Pong
Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can compete against another player controlling a second paddle on the opposing side.

Modules: turtle, time
font : Retro Gaming

Steps:
1. Create the screen 
   1. screen size : 800X600
   2. bg color: black
   3. used listen and onkey methods
    
2. Create and move a paddle
   1. Paddle class 
   2. make it move along y-axis like up and down
   
3. Create another paddle
4. Create the ball and make it move constantly across the screen
   1. Ball class and make it move
   2. add bounce logic

5. Detect when the ball collides with wall and make it bounce back
6. Detect when there's a collision with the paddle to know when to bounce it back
   1. reset position of the ball when a paddle misses hitting
   2. make it move opp side of the paddle that missed

7. Count the score when the ball misses the paddle
   1. Divide scoreboard for right paddle and left side
   2. Update scoreboard with clear method

8. Create the separator line in between left paddle and right paddle
