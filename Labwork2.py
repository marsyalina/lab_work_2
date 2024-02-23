'''
    Program purpose: To ask user to input data on the reservation hotel
    Programmer: NOOR MARSYALINA
    Date: 23 February 2024
'''
print("WELCOME TO BIGTUMMY HOTEL")

single = 100.00
double = 150.00
suite = 250.00
total = 0

while True:
    room_type = input("Choose your room (Single, Double, Suite): ").lower()
    number_type = int(input("Enter your number of rooms to reserve: "))

    if room_type == "suite" and number_type <= 3:
        print(f"Error: Minimum to stay for a suite is 3 nights above.")
        continue

    if room_type == 'single':
        total = single * number_type
        if number_type > 7:
            print("Awesome! You get a free breakfast voucher.")

    elif room_type == 'double':
        total = double * number_type
        if number_type > 7:
            print("Sorry! You do not get a free breakfast voucher.")

    elif room_type == 'suite':
        total = suite * number_type
        if number_type > 7:
            print("Sorry! You do not get a free breakfast voucher.")

    if number_type > 5:
        total_discount = total * 0.1
        total = total_discount

    print("Type of room: ", room_type)
    print("Number of rooms to reserve: ", number_type)
    print("The total cost :",total)
    break


