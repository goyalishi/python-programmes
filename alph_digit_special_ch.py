x=input("Enter the character")
if(x>='a' and x<='z') or(x>='A' and x<='Z'):
    print("entered character is alphabet.")

elif x>='0' and x<='9':
    print("entered character is a digit.")

else:
    print("entered character is a special character.")