#make 5 set of numbers from 1 to 50 by 10ths and collect them into a dictionary array then ask user for input of random numbers
#Print all numbers inputed by user to different set of numbers when input turns invalid

num_range = {}
while True:
        input_number = int(input("Please enter any random number ranging from 1 to 50: "))
        if input_number >= 1 and input_number <= 10:
                num_range = {"First_set": input_number}
                continue
        elif input_number >= 11 and input_number <= 20:
                num_range = {"Second_set": input_number}
                continue
        elif input_number >= 21 and input_number <= 30:
                num_range = {"Third_set": input_number}
                continue
        elif input_number >= 31 and input_number <= 40:
                num_range = {"Fourth_set": input_number}
                continue
        elif input_number >= 41 and input_number <= 50:
                num_range = {"Fifth_set": input_number}
                continue
        else:
                break

print(input_number)