# input a word or sentence
string = input("plese enter your own string :")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("/n the oringinal string =", string)
print("the reversed string =",string2)
