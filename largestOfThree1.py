def main():
    try:
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))
        num3 = int(input("Enter third integer: "))

        # Nested if statements to determine the largest number
        if num1 >= num2:
            if num1 >= num3:
                largest = num1
            else:
                largest = num3
        else:
            if num2 >= num3:
                largest = num2
            else:
                largest = num3

        print(f"The largest number is: {largest}")

    except ValueError:
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()
