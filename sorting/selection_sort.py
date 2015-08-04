def is_smallest(li, l):

    smallest = l[0]
    for i in l:
        if i <= smallest:
            smallest = i

    return li == smallest


def selct(ul):

    ordered_list = []
    for i in range(len(ul)):
        if is_smallest(ul[i], ul):
            ordered_list.append(ul[i])
            ul.pop(i)
    return ordered_list
