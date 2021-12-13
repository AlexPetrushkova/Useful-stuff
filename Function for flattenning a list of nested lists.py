import functools
import operator


#lst = [['one'], [343, 'two'], [[9.0, '9', 9], [[777, 666], [[[[42]]]]]]] # test list


def functools_reduce_iconcat(a):
    """
    Flattens a list of nested lists 
    """
    return functools.reduce(operator.iconcat, a, [])


def list_pull(lst):
    """
    Flattens a list of nested lists of nested lists
    """
    res = list()
    l = functools_reduce_iconcat(lst)
    while True:
        i = 0
        while i < len(l):
            if type(l[i]) != list:
                res.append(l[i])
                del l[i]
                i -= 1
            i += 1
        if len(l) == 0:
            break
        else:
            l = functools_reduce_iconcat(l)
            continue
    return res

