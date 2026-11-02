string = input("Enter your string here: ")



for letter in string:
    print(letter)



string_length = len(string)
print(f"String length is {string_length}")

vowels = 0
consonants = 0
others = 0
numbers = 0
capital = 0
lower = 0


for letter in string:

    if letter in "aeiou":
        vowels += 1

    elif letter in "qwrtypsdfghjklzxcvbnm":
        consonants += 1

    elif letter in "1234567890":
        numbers += 1

    elif letter in "QWERTYUIOPASDFGHJKLZXCVBNM":
        capital +=1

    elif letter in "qwertyuiopasdfghjklzxcvbnm":
        lower +=1

    else:
        others += 1


print(f"There are {vowels} vowels, {consonants} consonants, {numbers} numbers and {others} other characters.")
