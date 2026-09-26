# if, elif, and else
This section will go over, if, elif, and else, statements. These are known as conditionals, and are used to execute a sequence of code based on the given boolean values. 

## "If" Statments
An "if" statement evaluates wether the given expreession is evaluated as True.
- If True, the code is executed
- If False, the code does not executed
---
     Ex.
        score = 90
            
        if score >= 80:
        print('You pass the course!)

## "else" Statments
Adding an "else" statement after an "if" statement allows for another set of code yo be ran if the if statement evaluates the expression to be False 

    Ex. 
        score = 70
        
        if score >= 80:
            print('You pass the course!')
        else:
            print('You do not pass the course!')

## "elif" Statements
An "elif" statement, which is short for "else if", can be added between an if statement and an else statment to elevate for another condition. The code unter the elif statement will only execure if the preceding if statement evaluates to be False. 

    Ex. 
        score = 70

        if score >= 80:
            print('You did Amazing')
        elif score > 65:
            print('You did okay')
        else:
            print('You'll need to try again')

# Loops
A loop is used to execute code repreatedly in Python. This article will cover how "for" loops and "while" are used

## "for" loops
The "for" loop is used to iterate over items an execute code on each item. It has two keywords, "for" and "in", which are used to describe the element and the objext that is being iterated over, repectively. The indentions after : starts the body of the loop.
    
    Ex. 
        nums = [1,2,3,4,5]

        for num in nums:
            print(num+1)

### "for" loops with range()
The "range()" function cna be used with the for loop to execute a block of code multiple time. The code below iterates betwwen number 0 to 2 nd prints each number.

    Ex.
        for i in range(3):
            print(i)