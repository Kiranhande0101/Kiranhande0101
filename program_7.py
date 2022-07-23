char=input("enter any character")
if ord(char)>=48 and ord(char)<57 :
    print(f"{char}is a digit")
elif ord(char)>=65 and ord(char)<=99 :
    print(f"{char}is a uppar case")
elif ord(char)>=97 and ord(char)<122 :
    print(f"{char}is a lower case")   
else:
    print(f"{char}is a special character")