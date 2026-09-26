def main():
    resources = ["web-01","db-01","cache-01","vnet-01","vm-01"]

    for resource in resources: ## resources attaches to items in resources and iterates through for all items in the list print reource on each iteration 
        print((resource))

def rangeloop(): ## Iterates throught the range starting at 0 and ending one before the number input
    for i in range(6): # Will print 0-5 (0, 1, 2, 3, 4, 5)
             print(i)

def nestedloop(): ## Nested loop: Printing all name that appear in the list of lists
    teams = [['Dante', 'Destiny'], ['Jaelyn', 'Corenda'], ['Daniel', 'Tori']]

    for team in teams:
      for name in team:
        print(name)

def whileloop(): # While loop runs and prints "i" as long as the value "i" is less than 6
        i = 1
        while i < 6:
            print(i)
            i += 1

if __name__ == "__main__":
    ## main()
    ## rangeloop()
    ## nestedloop()
    whileloop()