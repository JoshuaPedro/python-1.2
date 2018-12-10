# convert_table.py
# A program to convert Celsius temps to Fahrenheit and inserts it into a table
# by: Joshua Pedro
print ("This is a program that converts fahrenheit")

def main():
    for celsius in [0,10,20,30,40,50,60,70,80,90,100] :
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", celsius, "degrees Celsius."" The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()
