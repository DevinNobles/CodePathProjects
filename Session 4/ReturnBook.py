lib = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}


def returnbook(title, library):
    if title not in library:
        library[title] = 1
    else:
        library[title] += 1
    
    print(library)


returnbook('Black Pan', lib)

