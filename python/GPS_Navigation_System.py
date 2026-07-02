# GPS Navigation System (Backtracking)

back = []
forward = []
current = "Home"

while True:
    print("\nCurrent Place:", current)
    print("1. Visit New Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        place = input("Enter Place: ")
        back.append(current)
        current = place
        forward.clear()

    elif choice == 2:
        if len(back) == 0:
            print("No Previous Place")
        else:
            forward.append(current)
            current = back.pop()

    elif choice == 3:
        if len(forward) == 0:
            print("No Forward Place")
        else:
            back.append(current)
            current = forward.pop()

    elif choice == 4:
        break

    else:
        print("Invalid Choice")