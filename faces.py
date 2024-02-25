#Replace :) with 🙂 and :( with 🙁
def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoticon

def main():
    #Prompt for input
    user_input = input("How are you feeling?")

    #convert emoticon inputs > emoji outputs
    convert(user_input)

    #print converted output
    print(convert(user_input))

#run script
main()
