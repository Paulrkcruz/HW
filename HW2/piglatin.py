# Paul Cruz
# CS5001
# HW 2
# Problem 1
# piglatin.py

# PURPOSE
# Translates a word to pig latin. The word must contain only letters. If the
# word starts with a vowel, the suffix "ay" will be added to the end.
# Otherwise, the consonant cluster at the start of the word is moved to the end
# then the suffix "ay" is added.
# SIGNATURE
# pig_latin_translator :: String => String
# EXAMPLES
# pig_latin_translator("pig") => "igpay"
# pig_latin_translator("123") => "Invalid word!"
# pig_latin_translator("apple") => "appleay"
def pig_latin_translator(input_word):

    vowel_list = ["a", "e", "i", "o", "u"]
    if input_word.isalpha():
        if input_word[0] in vowel_list:
            input_word += "ay"
            return word
        else:
            for c in input_word:
                if c in vowel_list:
                    wordind = input_word.index(c)
                    input_word = input_word[wordind:] \
                        + input_word[:wordind] + "ay"
                    return input_word
    else:
        print("Invalid word. Try again!")
        quit()


def main():
    input_word = str(input("Enter a word without spaces or numbers: "))
    print(pig_latin_translator(input_word))


main()
