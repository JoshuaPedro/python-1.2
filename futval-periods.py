# futval-periods.py
# by Joshua Pedro. November 20th, 2018
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a x-year investment.")

    principal = int(input("Enter the principal balance: "))
    periods = int(input("how many times intrest is compounded anually?: "))
    apr = float(input("Enter the annual interest rate: "))
    balance = principal
    for i in range (10 * periods) :
        balance=balance * (1 + apr/periods)
    print("The value in",periods * 10, "periods is:", balance)
main()
