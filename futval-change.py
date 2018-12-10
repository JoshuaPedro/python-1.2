# futval.py
# by Joshua Pedro. November 19th, 2018
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a x-year investment.")

    investment = eval(input("Enter the amount to invest each year: "))
    x = eval(input("how many years of investment?: "))
    apr = eval(input("Enter the annual interest rate: "))
    sum = 0
    for i in range (x) :
        sum=sum+investment
        sum= sum * (1 + apr)
    print("The value in x years is: ", sum)

main()
