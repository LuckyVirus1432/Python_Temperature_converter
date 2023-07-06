# Python funtion to convert Celcius temperature into Fahrenheit.
def toFahrenheit(celc_temp):
    temp = (celc_temp * 1.8) + 32
    return temp

# Python funtion to convert Fahrenheit temperature into Celcius.
def toCelcius(fahr_temp):
    temp = (fahr_temp - 32) * (5/9)
    return temp

if __name__ == "__main__":
    print("*" * 100)
    print(" " * 40 + "Temperature converter" + " " * 40)
    print("*" * 100)
    # Infinite loop => executes until user breaks it through some specified conditions.
    while(True):
        #try-except block to handle exceptions which might occur in the excecution of the following statements.
        try:
            choice = int(input("Choose the converter: \n1) Celcius to Fahrenheit \n2) Fahrenheit to Celcius \n3) Exit \n"))
            if choice == 1:
                celc_temp = float(input("Enter the temperature in Celcius: "))
                print(f"{celc_temp} Celcius = {toFahrenheit(celc_temp)} Fahrenheit")
                print("*" * 100)
            elif choice == 2:
                fahr_temp = float(input("Enter the temperature in Fahrenheit: "))
                print(f"{fahr_temp} Fahrenheit = {toCelcius(fahr_temp)} Celcius")
                print("*" * 100)
            elif choice == 3:
                print("Exiting...")
                print("*" * 100)
                break
            else:
                print("Invalid input..!")
                print("*" * 100)
        except Exception as e:
            print("Error occured: please check the value you entered. It must be numeric.")
            print("*" * 100)
