def main():
    #Question prompt to user
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    #Convert user_input to lowercase for case-insensitive comparison & strip whitespace
    user_input = user_input.lower().replace(" ", "")

    # List of correct answers
    """
    I wanted to add morse code as an acceptable answer, but realised the .strip() would make it tricky...
    But found out that if I change correct_answers to include no spaces,
    and make it so user_input replaced " " with "", then I wouldn't need to include the .strip() function...
    Which was making things tricky.

    This also means that, no matter how many spaces you put between letters (on purpose or on accident),
    it'll still return "Yes" - assuming that you've used the 'correct number' of 'correct characters' in the 'correct order'.
    """
    correct_answers = ["42", "forty-two", "fortytwo", "fourtytwo", "fourty-two", "....-..---", "....- ..---"]

    # Check if the answer is in the list of correct answers
    if user_input in correct_answers:
         print("Yes")

    else:
         print("No")

main()
