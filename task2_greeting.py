# Task 2: Create a Personalized Greeting

def main():
    try:
        # Take user input
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()

        # Validate input
        if not first_name or not last_name:
            print("First name and last name cannot be empty.")
            return

        # Concatenate full name
        full_name = first_name + " " + last_name

        # Print greeting
        print(f"\nHello, {full_name}! Welcome to the Python program.")

    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    main()