def intersect(set1, set2):
    result = set()
    for element in set1:
        if element in set2:
            result.add(element)
    return result


def union(set1, set2):
    result = set()
    for element in set1:
        result.add(element)
    for element in set2:
        result.add(element)
    return result


def differenceU(set1, setU):
    result = set()
    for element in setU:
        if element not in set1:
            result.add(element)
    return result


