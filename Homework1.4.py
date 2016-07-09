# Write a program that displays a table

for number in range(0, 4):
    if number == 0:
        print("a  ", "a^2 ", "a^3 ")

    p1 = (number + 1)
    p2 = p1 * p1
    p3 = p1 ** 3
    print(p1, " ", p2, " ", p3)
