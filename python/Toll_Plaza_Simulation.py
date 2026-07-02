
# Toll Plaza Simulation (Circular Queue)

SIZE = 5
queue = [""] * SIZE
front = -1
rear = -1

while True:
    print("\n1. Vehicle Enter")
    print("2. Vehicle Exit")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        if (rear + 1) % SIZE == front:
            print("Toll Plaza Full")

        else:
            vehicle = input("Enter Vehicle Number: ")

            if front == -1:
                front = rear = 0
            else:
                rear = (rear + 1) % SIZE

            queue[rear] = vehicle

    elif choice == 2:

        if front == -1:
            print("Queue Empty")

        else:
            print("Vehicle Passed:", queue[front])

            if front == rear:
                front = rear = -1
            else:
                front = (front + 1) % SIZE

    elif choice == 3:

        if front == -1:
            print("Queue Empty")

        else:
            i = front
            while True:
                print(queue[i])
                if i == rear:
                    break
                i = (i + 1) % SIZE

    elif choice == 4:
        break

    else:
        print("Invalid Choice")