#Calculate Tip
def main():
    #Prompt user input for cost in $
    dollars = dollars_to_float(input("How much was the meal? "))

    #Prompt user input for desired tip %
    percent = percent_to_float(input("What percentage would you like to tip? "))

    #cost of meal * tip you want to leave as a percentage, then / 100 = actual tip (see below)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Converts '##.##' from string to a float (calculatable number), removes "$"
    return float(d.replace("$", ""))

def percent_to_float(p):
    # Converts '##%' to float, remove "%", divide by 100 to get tip
    return float(p.replace("%", "")) / 100

main()
