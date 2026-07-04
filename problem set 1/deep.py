x = str(input("What is the meaning of life? ")).lower()

if x == "42":
    print("yes")
elif x == "forty two":
    print("yes")
elif x == "forty-two":
    print("yes")
else:
    print("no")