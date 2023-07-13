# Insert Name of Form
print()
print("Welcome to Tony's Auto Shop: Custom Car Form")
print()


#This question will ask the user what model type they wish to have for their car
#Question 1 (Multiple Choice) 
print("(For multiple choice questions, please enter the letter you wish to be selected)")
print("- Model Type -")
print("1. What Model of Car are you ordering? ")
print("        a. Audi")
print("        b. BMW")
print("        c. Toyota")
print("        d. Honda")
modeltype = input("Please enter choice (a-d): ")


print()
print()
#This question is asking whether the user wants a sunroof or not
#Question 2 (Yes or No)
print("2. Would you like a sunroof?")
sunroof = input("Please enter 'yes' or 'no': ")

print()
print()
#This question is asking whether the user wants built-in bluetooth for their car
#Question 3 (Yes or No)
print("3. Would you like built-in bluetooth?")
bluetooth = input("Please enter 'yes' or 'no': ")

print()
print()
#This question is a short answer, asking the user what color they want their car to be 
#Question 4 (Short Answer)
print("4. What color would you like your car?")
color = input("Please enter desired car color: ")

print()
print()
#This question asks the user which horsepower they want from the options provided
#Question 5 (Multiple Choice)
print("- Horsepower -")
print("5. How much Horsepower do you want in your car?")
print("        a. 250")
print("        b. 500")
print("        c. 750")
print("        d. 1,000")
horsepower = input("Please enter choice (a-d): ")


print()
print()
#This question asks the user whether they want their windows tinted or not
#Question 6 (Yes or No)
print("6. Would you like tinted windows?")
windows = input("Please enter 'yes' or 'no': ")

print()
print()

#This is a final summary of the client's custom car
print("- Summary -")
print(f"Model Option: {modeltype}")
print(f"Sunroof Option: {sunroof}")
print(f"Bluetooth Option: {bluetooth}")
print(f"Desired Color: {color}")
print(f"Horsepower Selection: {horsepower}")
print(f"Tinted Windows: {windows}")



