# Simple switch-case example using match-case (Python 3.10+)

value = input("Enter a number between 1 to 3: ")

match value:
    case "1":
        print("You selected One.")
    case "2":
        print("You selected Two.")
    case "3":
        print("You selected Three.")
    case _:
        print("Invalid selection.")
