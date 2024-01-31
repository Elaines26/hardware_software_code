def intro_msg():
    print("I can reverse a string")
    print("If you give me 'apple' I will return 'elppa'")
    print("I can even do an entire sentence")
    return input("type something and see: ")

def reverse_word(characters):
    reverse_string = ''
    for charcater in characters:
        reverse_string  = character + reverse_string
        return reverse_string

def main():
    word = intro_msg()
    word = reverse_word(word)
    print('below is your string in reverse: \n{}'.format(word))

if__main__ == "__main__":
main()
