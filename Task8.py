#Make a new string from given string use 'is' in front of that string
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str
#Main program
string=input("Enter your string: ")
print("New string :",new_string(string))