def main():
    score = int(input("What was your score? "))

    if score >= 90:
        print('Super Star!!!!!')
    elif score >=70: 
        print('You Passed')
    else:
        print('You Failed... Better Luck Next Time')

if __name__ == '__main__':
    main()