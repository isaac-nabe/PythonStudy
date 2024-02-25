def main():

    # c = Speed of light as m/s
    c = 3 * pow(10, 8)

    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Calculate the energy
    energy = mass * pow(c, 2)

    # Print the equivalent energy measured in Joules
    print("The equivalent number of Joules is:", int(energy))

main()
