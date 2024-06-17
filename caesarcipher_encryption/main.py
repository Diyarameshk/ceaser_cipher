import string
letters = string.ascii_lowercase
#print(letters)
def ceaser(text,mode,key):
    final_text = ' '
    if mode == "decode":
        key = key * -1
    for character in text:
        if character in letters:
            index = letters.find(character)
            new_index = (index + key)%26
            final_text += letters[new_index]
        else:
            final_text += character
    print(f"{mode}d text is {final_text}")

while True:
    mode = input("Enter mode of input(encode or decode): ")
    text = input("enter text: ")
    key = int(input("enter key to input: "))
    ceaser(text,mode,key)
    user_res = input("do you want to continue:")
    if user_res == "no":
        break
