def main():
    while True:
        try:
            #prompts the user for a fraction
            fraction = input("Fraction: ")

            #split expression & assign into variables (x is numerator, y is denominator)
            x, y = fraction.split("/")

            #Converts values from strings into integers
            numerator = int(x)
            denominator = int(y)

            #check denominator for 0
            if denominator == 0:
                raise ZeroDivisionError
            #check nominator > denominator
            if numerator > denominator:
                raise ValueError

            #calls into_percent with valid values
            into_percent(numerator, denominator)

            #if no issues, break loop
            break

        #handles value errors
        except ValueError:
                print("Please enter a valid fraction.")
        except ZeroDivisionError:
                print("Denominator cannot be 0.")

#converts fraction into rounded percentage
def into_percent(numerator, denominator):

    #calculates percentage
    percent = (numerator / denominator) * 100

    #round to nearest integer
    answer = round(percent)

    if answer <= 1:
        print("E")
    elif answer >= 99:
        print("F")
    else:
        print(f"{answer}%")

main()
