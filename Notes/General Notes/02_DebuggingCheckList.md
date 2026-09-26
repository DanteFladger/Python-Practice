# The Debugging Checklist
1. What did I expect?
2. What actually happend?
3. Is ther an error message?
4. Which line failed or behaved wrong?
5. What are the values and types involved?
6. What am I assuming?
7. What's the smallest version that reporduces it?
___
    Ex. 
        Issue: Expected names are not printing
        
| Steps | My Case |
|-----|-------|
|Expected Output| Dante and Destiny|
|Actual Output  |Nothing           |
|Error message| None |
|Where did it fail? | Before the loop, since even the function start produced nothing|
|Assumption| "the function is being called" was false|
|Check| print("breakloop started") proved it|
---
