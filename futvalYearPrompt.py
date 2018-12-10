# futvalYearPrompt.py
# by Joshua Pedro. November 19th, 2018
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a x-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    x=eval(input("years of investment: "))
    for i in range (x) :
        principal = principal * (1 + apr)
    print("The value in 10 years is: ", principal)

main()
