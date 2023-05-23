def classNamesReader(path):
    names = []
    with open(path, 'r') as fp:
        for line in fp:
            x = line[:-1]
            names.append(x)
    return names
