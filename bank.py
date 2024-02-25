def main():
    #Prompts Greeting from user
    Greeting = input("Greeting: ")

    #Makes user's input non-case-sensitive, and non-whitespace-sensitive
    Greeting = Greeting.lower().strip()

    #Checks if greeting includes a "hello" & assigns "$0"
    if Greeting.startswith("hello"):
        print("$0")

    #Checks if greeting includes an 'h" & assigns "$20"
    elif Greeting.startswith("h"):
        print("$20")

    #Any other greetings return a "$100"
    else:
        print("$100")

main()
