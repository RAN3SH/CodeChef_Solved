def is_valid_email(email):
    if "@" in email and "." in email:
        at_the_rate_index = email.index("@")
        dot_index = email.rindex(".")
        if at_the_rate_index < dot_index and dot_index != len(email) - 1:
            return True
    return False
    

def is_valid_experience(exp):
    if exp.isdigit():
        years = int(exp)
        if years >= 0:
            return True
    return False


def add_application():
    print("\n--- Add Job Application ---")

    name = input("Enter Name: ")
    if not name.strip():
        print("Name cannot be empty.")
        return False

    email = input("Enter Email: ")
    if not is_valid_email(email):
        print("Invalid email format.")
        return False

    job = input("Enter Job Role: ")
    if not job.strip():
        print("Job Role cannot be empty.")
        return False

    experience = input("Enter Experience(in years): ")
    if not is_valid_experience(experience):
        print("Experience must be a non-negative number")
        return False
    
    with open("applications.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Job Role: {job}\n")
        file.write(f"Experience: {experience} years\n")
        file.write("\n") 

    print("\nApplication Added Successfully!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Job Role: {job}")
    print(f"Experience: {experience} years")
    print()
    return True


def main():
    while True:
        print("========== Job Application Tracker ==========")
        print("1. Add Job Application")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_application()
        elif choice == '2':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
