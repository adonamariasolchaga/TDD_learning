import math

def read_ints(io_object):
    """Having an IO bytes object representing a file of ints per line, reads each int into a
    python list.

    Parameters
    ----------
    document_path
        IO bytes object

    Returns
    -------
        Pyhton list with ints readed
    """
    ints = [int(l.strip()) for l in io_object]
    return ints

def count(int_list):
    """Counts the number of elements in a list

    Parameters
    ----------
    int_list
        List with ints

    Returns
    -------
        Number of elements in the list
    """
    return len(int_list)

def summation(int_list):
    """Given an int list adds all its elements

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        The summation of all list ints
    """
    return sum(int_list)

def average(int_list):
    """Given an int list compute the average of its elements

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        The average of all int elements in the list
    """
    return summation(int_list) / count(int_list)

def minimum(int_list):
    """Given an int list computes its minimum

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        Minimum integer of the list
    """
    return min(int_list)

def maximum(int_list):
    """Given an int list computes its minimum

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        Maximum integer of the list
    """
    return max(int_list)

def harmonic_mean(int_list):
    """COmputes harmonic mean of a list of ints

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        Harmonic mean of the list
    """
    return count(int_list) / summation([1/i for i in int_list])

def variance(int_list):
    """Computes variance of a list of integers

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        Variance of the list
    """
    return summation([(i-average(int_list))**2 for i in int_list]) / count(int_list)

def standard_dev(int_list):
    """Computes standard deviation of a list of integers

    Parameters
    ----------
    int_list
        List with integers

    Returns
    -------
        Standard deviation of the list
    """
    return math.sqrt(variance(int_list))

if __name__ == '__main__':
    my_ints = read_ints('random_nums.txt')
    print(my_ints)
    print()
    print(count(my_ints))
    print()
    print(summation(my_ints))
    print()
    print(average(my_ints))
    print()
    print(minimum(my_ints))
    print()
    print(maximum(my_ints))


