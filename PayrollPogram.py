def compute_pay(hours_worked, hourly_rate):
    if hours_worked <= 40:
        return hours_worked * hourly_rate
    else:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        return regular_pay + overtime_pay


def main():
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        if hours_worked < 0 or hourly_rate < 0:
            raise ValueError("Hours worked and hourly rate must be non-negative.")

        total_pay = compute_pay(hours_worked, hourly_rate)
        print(f"Total pay: ${total_pay:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

