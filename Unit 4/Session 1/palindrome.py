def first_palindrome(words):
    pallys = []
    for word in words:

        b = word[::-1]

        if word == b:

            pallys.append(word)

    return pallys


dawgs = ["abc","car","ada","racecar","cool"]


print(first_palindrome(dawgs))