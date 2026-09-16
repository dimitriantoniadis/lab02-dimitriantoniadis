# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60 
    seconds = total_seconds % 60
    return f"{hours}:{minutes:02}:{seconds:02}"

print(seconds_to_hms(3661))
print(seconds_to_hms(59))
print(seconds_to_hms(7325))


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age <= 5:
        ticket_price = 0.00
    elif age <= 12:
        ticket_price = 5.00
    elif age <= 64:
        ticket_price = 15.00
    else:
        ticket_price = 10.00
    return ticket_price

print(admission_price(3))   # 0.00
print(admission_price(10))  # 5.00
print(admission_price(30))  # 15.00
print(admission_price(70))  # 10.00



def sum_multiples(limit):

    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(sum_multiples(10))  # 23    
print(sum_multiples(20))  # 78
print(sum_multiples(100))  # 2318


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

print(total_of_positives([1, -2, 3]))  # 4
print(total_of_positives([-1, -2, -3]))  # 0
print(total_of_positives([5, 10, -5, 15]))  # 30


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
