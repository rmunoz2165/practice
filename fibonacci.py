# This code will generate the fibonacci sequence list of numbers based on user input

def fibSequ(n):
    '''
    Generates a fibonacci sequence with the size of n

    '''

    assert n > 0

    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2]) #Adds last two numbers to generate fib. sequ
    for i in range(len(series)):
        series[i] = str(series[i]) #Convert to string

    return(', '.join(series)) #Seperate with commas

def main(): #Wrapper function

    print(fibSequ(int(input('Enter how many numbers you want to go in the fibonacci list:'))))

if __name__ == '__main__':
    main()