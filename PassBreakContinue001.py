def passloop(): ## Nothing gets executed when "pass" is placed under a condition
    names = ['Dante', 'Destiny', 'Jaelyn', 'Corenda', 'Bean']

    for name in names:
        if 'd' in name.lower():
            pass
        else: 
            print(name)


def breakloop(letter="z"): ## If a certaion condition is met, the loop stops iterating and breaks at that point
    print("breakloop start")
    names = ['Dante', 'Destiny', 'Jaelyn', 'Corenda', 'Bean']

    
    for name in names:
        if letter in name.lower():
            break
        print(name)
    else:
        print("No names with a "+ letter +" found")
            

def continueloop(): ## Skips over an iteration if the condition is met and goes onto the next iteration.
     names = ['Dante', 'Destiny', 'Jaelyn', 'Ms.Corenda', 'Bean']

     for name in names:
         if 'm' in name.lower():
             continue
         else:
             print(name)


def main():
    letter = input("Please enter a letter: ")
    breakloop(letter)
    ## continueloop()
    ## passloop()


if __name__ == "__main__":
    main()