__author__ = 'Daniil Leksin'


def solution(A):
    """
    Function search for equilibrium indices.
    The function returns -1 if no equilibrium index exists.
    :param A: input list
    :return: non -1 if an equilibrium index exists
    """
    if len(A) == 0:                                     # empty list has no equilibrium indices
        return -1                                       # return -1 if list is empty
    right_sum = sum(A)                                  # calculate upper sum of the list A
    left_sum = 0                                        # initialization of the lower list
    for index in range(0, len(A)):                      # go through the all elements of the list A
        if right_sum - A[index] == left_sum:            # compare left and right sums
            return index                                # return not -1 value if equilibrium index
        else:
            left_sum += A[index]                        # increase left sum
            right_sum -= A[index]                       # decrease right sum
    return -1                                           # return -1 if no equilibrium indices

if __name__ == '__main__':
    solution([-1, 3, -4, 5, 1, -6, 2, 1])
