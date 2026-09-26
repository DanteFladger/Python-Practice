# Program Structure 
## The main() Function
    Placing the if statement in our program checks whether the program is being run independently as the primary module or as a library in another scrip.

## Comments
    In Python, comments are more with "#" to explain code at vaious points in the code. Comments are note executed as code and are used for documentation. There are two types of comments: 
### Inline
    Inline comments should be used when you have a short comment that you would line to include afer a line of code.
        Ex.  
            minutes = secounds / 60 # calculating minutes from secounds
### Block 
    Block comments are used when you have multiple lines of comments that you'd like to include with your code. 
    (Unlike most languages that have special syntex for multiple lines of comments, Python required "#" on consecutive single lines.)
        Ex. def calculate_minutes(seconds):
                # This function calculates the time in minutes.
                # From given seconds.
                minutes = seconds / 60
                return minutes 

## Input and Output
### Input
    Python has a built-in function called input() that takes in the user's input.
        Ex.
            input('What is your name?')
    
    Inputs can be stored as variables to be used later
        Ex. 
            name = input('What is you name?')
### Output
    Python has a built-in function called print() that displays output.
        Ex.
            print(name) 

    - "+" | Used to concatenate variables and strings in print() statements as long as your variables are strings.
        Ex.
            print(name + " )
    
# What are Variables?
Variables are used to name, store and reference data.

## Decaring a Variable
    - You can declare a variable using the following syntax. This line of code stores the string 'Grace' in the variable "name".
       
        Ex.
            name='Grace'. (Print(name) --> Grace)
    
    - You can change value stored in the varibale by using the same syntax by assigning the variable to the new value 
       
        Ex. 
            name = 'Ari' (Print(name) --> Arie)

    - You can store other darta types in a variable, not just strings. For example, storing a number would look like this:
        Ex. 
            Temperature = 97.5

    - You can also store resultes of expressions as a variable:
        
        Ex. 
            sum_of_two_numbers = 4 + 2
        
# Data Types
In This section, we will cover the following basic data types in Python:
    - Integer
    - Float
    - Boolean
    - String

## Integer
ints store integer values. We can specify that the variable is a integer by using a whole number or we can use int() to cast numerical variables as an integer:
### Literal:
    Untilized when you know the value while writing the code
        Ex. 
            reties = 3
            retures +