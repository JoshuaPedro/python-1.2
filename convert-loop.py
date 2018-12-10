# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Joshua Pedro
print ("This is a program that converts fahrenheit")

def main():
    y =  eval(input("How many numbers should I convert? "))
    for i in range(y) :
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()
