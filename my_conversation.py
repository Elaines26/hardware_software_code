def conversation() :
    print("do you like coding in python? Answer yes or no")
    answer = input()
    x = answer.strip()
    if x.lower() == "yes" :
        print("That's good - the united states needs more coders !!")
    elif x.lower() == "no" :
        print("perhaps you will change your mind")
        print("goodbye")
    else:
        print("I don't understand")
        print("Goodbye ;)")

def main():
    print("welcome to my conversation program" )
    conversation()
    print("Thanks for chatting with me" )

if __name__ == "__main__":
    main()
