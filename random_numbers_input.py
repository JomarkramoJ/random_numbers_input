#Dictionary to store all variables
num_range = {
        "First_set": [],
        "Second_set": [],
        "Third_set": [],
        "Fourth_set": [],
        "Fifth_set": [],
}
#Main code
while True:
    try:
        input_number = int(input("Please enter any random number ranging from 1 to 50: "))
        if input_number >= 1 and input_number <= 10:
                num_range["First_set"].append(input_number)
                continue
        elif input_number >= 11 and input_number <= 20:
                num_range["Second_set"].append(input_number)  
                continue
        elif input_number >= 21 and input_number <= 30:
                num_range["Third_set"].append(input_number)
                continue
        elif input_number >= 31 and input_number <= 40:
                num_range["Fourth_set"].append(input_number)
                continue
        elif input_number >= 41 and input_number <= 50:
                num_range["Fifth_set"].append(input_number)
                continue
        else:
                print("Invalid Input")
                break
    except:
           print("Input Error")

#new variable to get all the items inside the dictionary and then print
for set_name, numbers in num_range.items():
    print(set_name + ":", *numbers, sep=", ")