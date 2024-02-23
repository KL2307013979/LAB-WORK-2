#Name: Muhamad Azfar Bin Mohamad Fauzi
#ID Student: AM2307013979
#Assignment: LAB WORK 2

def hotelReserve():
    print("--------------------------------------")
    print("    Welcome to the Hotel Hilarious    ")
    print("--------------------------------------")
    print("       Single - RM100 per night       ")
    print("       Double - RM150 per night       ")
    print("       Single - RM250 per night       ")
    print("--------------------------------------")

    #declare variable
    room_rates = {'Single': 100, 'Double': 150, 'Suite': 250}
    discountThreshold = 5
    discountPercent = 0.10

    roomType = input("Select type of room (Single, Double, Suite): ").capitalize()
    room = int(input("Enter the number of rooms to reserve: "))
    night = int(input("Enter the number of nights to stay: "))

    if roomType not in room_rates or room <= 0 or night <= 0:
        print("Invalid input. Please enter valid information.")
        return

    if roomType == 'Suite' and night < 3:
        print("Reservations for Suites necessitate a minimum booking duration of 3 nights.")
        print("         Thank you for visitig          ")
        return

    #calculation
    total_cost = room_rates[roomType] * room * night
    if room > discountThreshold:
        total_cost *= (1 - discountPercent)

    if roomType == 'Single' and night > 7:
        print("Congratulations! You get a complimentary breakfast voucher.")

    print(f"Total cost for your reservation: RM{total_cost:.2f}")

# Call the function
hotelReserve()
