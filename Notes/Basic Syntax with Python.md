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

(Inputs can be stored as variables to be used later)
       
     Ex. 
         name = input('What is you name?')
### Output
Python has a built-in function called print() that displays output.
    
     Ex.
        print(name) 

     "+" | Used to concatenate variables and strings in print() statements as long as your variables are strings.
            
        print(name + " is the coolest!!")
    
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

## Integer
ints store integer values. We can specify that the variable is a integer by using a whole number or we can use int() to cast numerical variables as an integer:

### Literal
Untilized when you know the value while writing the code
       
    Ex. 
        retries = 3 
### Conversion
Untilized when the value arrives at runtime, as a string
        
    Ex.
        retries = int(user_text)

### Notes
- Surrounging whitespace is ignored
- Truncates toward zero; does NOT round
- "True" is treated as 1, "False" is treated as 0
## Float
floats store numerical values with decimal points. "float()" is the built-in function that stores numerical values with their decimal points.
   
    Ex.
        tempertature = "101.3" --> string
        tempertature = float(temperature) --> float
## Boolean
boolean variables hold two values, True or False.
    
    Ex. 
        raining = True
        raining = bool("True")
        (The bool() function will always return "True" unless the variable is empty, 0, None or False)
## String
string variables hold characters and can be created by using single quotes ' or double quotes ". You cn also use the built-in dunction str() to specify that you are storing a string.
    
    Ex. 
        temp = 97.2 --> float
        temp = str(temp) --> string
# Casting
You may sometimes want to specifiy the type of the variable using built-in data types in Python. For example, when storing a numerical value as a strint
    
    Ex. 
        tempature = str(97.5)
        - "str()" : This function sakes a value and converts it into a string 
        - "int()"
        - "float()"
        - "bool()"

# Operations
Operators are used to perform operations on variables in Python
## Arithmetic Operations
|Operator | Name of Operation | Example | Description|
|:---------:|:-------------------:|:---------:|------------|
| +       | Addition          | x + y         |    x plus y        |
| -       | Subtraction       | x - y        |     x minus y       |
| *       | Multiplication    | x * y        |     x multilied by y      |
| **      | Exponentiation    | x ** y        | x raised to the power of y            |
| /       | Division          | x / y        |  x divided by y         |
| //      | Floor Division    | x // y        |  x divided by y, returing integer          |
| %       | Module            | x % y       |  The remainder of x divided by y        |

## Assignment Operations
|Operator | Example | Description|
|:---------:|:-------------------:|--------|
|= | x = y | Assign y to x|
|+=| x += y | Add y to existing value of x|
|-=| x -= y | Subtract y to existing value of x |
|*=| x *= y | Multiple existing value by y |
|/=| x /= y | Divide existing valur by 4 |
|%=| x %= y | Modulo existing calue by y|
## Comparizon Operations
|Operator | Example | Description|
|:---------:|:-------------------:|------------|
|==| x == y | Equal to|
|!=| x != y | Not equal|
|>| x > y | Greater than|
|<| x < y | Less than|
|>=| x >= y | Great than or equal to|
|<=| x <= y | Less than or equal to |
## Logical Operations
|Operator | Example | Description|
|:---------:|:---------:|------------|
|and| x > 2 and y > 1 | If both statements are true, returns True|
|or| x > 3 or y > 5 | If one of the statementes are true, returns True|
|not| not(x > 10 and y > 5)|If used, returns the reverse of the actual result|



