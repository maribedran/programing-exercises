def is_smallest(li, l):

    smallest = l[0]
    for i in l:
        if i <= smallest:
            smallest = i

    return li == smallest


def selct(ul):

    ordered_list = []
    while len(ul) > 0:
        for i in ul:
            if is_smallest(i, ul):
                ordered_list.append(i)
                ul.remove(i)
    return ordered_list
