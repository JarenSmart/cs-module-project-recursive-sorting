# INCLUSIVE VERSION
# def countdown(n):
#     """ Prints out all numbers from n to zero (inclusive)"""
#     for i in range(n, -1, -1):
#         print(i)


# countdown(4)

# -----------------
# What is a recursive function?
# - A function that calls itself
# - Has a stopping point

# RECURSIVE VERSION
def countdown(n):
    print(n)

    if n == 0:
        return

    countdown(n-1)


countdown(4)


def double_countdown(n):
    print(n)

    if n == 0:
        return

    double_countdown(n-1)
    double_countdown(n-1)


double_countdown(3)
