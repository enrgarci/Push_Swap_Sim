# Push_Swap_Sim

Push sawp sim is a fast made python simulator for the 42 project Push_Swap rules.

## Rules
You have 2 stacks, you receive the input on A, B is empty.
You must get the sorted input in A, input is a list of non repeating positive or negative numbers in the least amount of moves.

### Moves:

sa: Swaps the top elements of A.      
sb: Swaps the top elements of B.  
ss: sa + sb.  

pa: Push.Moves the top element of B to A.  
pb: Push.Moves the top element of A to B.  

ra. Rotate. All A elements of a move 1 up. First element moves to bottom [1,2,3 -> 2,3,1].  
rb. Rotate. All B elements of a move 1 up. First element moves to bottom [1,2,3 -> 2,3,1].  
rr. ra + rb

rra. Inverse rotate. All A elements of a move 1 down. last element moves to bottom [1,2,3 -> 3,1,2].  
rrb. Inverse rotate. All B elements of a move 1 down. last element moves to bottom [1,2,3 -> 3,1,2].  
rrr. rra + rrb.  

The goal is to get the sorted input on A using the least amount of moves.   

### Usage:
Run the main.py. Fist pop-up is the stack A. Window has the moves in buttons self explanatory.  

### Notes:   
The goal of this project was to make a small simulator of the rules while using for the first time the PySimpleUI package so the code has a lot to improve.
