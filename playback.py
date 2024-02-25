def main():
    #input prompt
    input_speech = input("Tell me something!")

    #replace ' ' with '...'
    output_speech = input_speech.replace(" ", "...")

    #print text with spaces replaced with '...'
    print(output_speech)

main()
