# Write a program that displays the word 'fun' using the corresponding letters to form a larger letter.

f = "F"
u = "U"
n = "N"
s = " "

line1 = (7 * (f) + 3 * (s) + u + 5 * (s) + u + 3 * (s) + 2 * (n) + 5 * (s) + 2 * (n))
line2 = (2 * (f) + 8 * (s) + u + 5 * (s) + u + 3 * (s) + 3 * (n) + 4 * (s) + 2 * (n))
line3 = (7 * (f) + 3 * (s) + u + 5 * (s) + u + 3 * (s) + 2 * (n) + s + n + 3 * (s) + 2 * (n))
line4 = (2 * (f) + 9 * (s) + u + 3 * (s) + u + 4 * (s) + 2 * (n) + 2 * (s) + n + 2 * (s) + 2 * (n))
line5 = (2 * (f) + 10 * (s) + 3 * (u) + 5 * (s) + 2 * (n) + 4 * (s) + 3 * (n))


def make_art():
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    return


make_art()
