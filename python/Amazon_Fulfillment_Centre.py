# Amazon Fulfillment Centre (Array)

belt = [""] * 8

while True:
    print("\n1. Add Product")
    print("2. Find Product")
    print("3. Update Product")
    print("4. Check Belt Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        index = int(input("Enter slot (0-7): "))
        if 0 <= index < 8:
            belt[index] = input("Enter product: ")
        else:
            print("Invalid slot")

    elif choice == 2:
        index = int(input("Enter slot (0-7): "))
        if 0 <= index < 8:
            print("Product:", belt[index])
        else:
            print("Invalid slot")

    elif choice == 3:
        index = int(input("Enter slot (0-7): "))
        if 0 <= index < 8:
            belt[index] = input("Enter new product: ")
        else:
            print("Invalid slot")

    elif choice == 4:
        if "" in belt:
            print("Belt is NOT Full")
        else:
            print("Belt is Full")

    elif choice == 5:
        for i in range(8):
            print(i, ":", belt[i])

    elif choice == 6:
        break

    else:
        print("Invalid Choice")