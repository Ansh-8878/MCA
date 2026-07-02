# Spam Detector (Linear Search)

spam_list = ["abc@gmail.com", "spam@yahoo.com", "fake@gmail.com", "test@spam.com"]

email = input("Enter Email ID: ")

found = False

for i in spam_list:
    if i == email:
        found = True
        break

if found:
    print("Spam Email Found")
else:
    print("Not a Spam Email")