def encode(digit):
    new_string = ''
    for i in digit:
        i = int(i)
        i += 3
        if i >= 10:
            i -= 10
        i = str(i)
        new_string += i
    return new_string


def decode(string):
    # Empty string for decoding
    new_string = ''
    for n in string:
        # iterates through given string and shifts digit back by 3
        n = int(n)
        n -= 3
        if n < 0:
            n += 10
        n = str(n)
        # Adds each digit to decoded string
        new_string += n
    return new_string


if __name__ == '__main__':
    while True:
        print()
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = input("Please enter an option: ")
        if option == "1":
            num = input("Please enter your password to encode: ")
            num = encode(num)
            num2 = num
            print("Your password has been encoded and stored!")
        if option == "2":
            num2 = decode(num2)
            print(f"The encoded password is {num}, and the original password is {num2}")
        if option == "3":
            break

