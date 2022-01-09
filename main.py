import numpy as np


def solve(directions):
    """
    Takes a list of directions and removes all redundant consecutive directions in a recursive manner.
    Pairs of NORDEN, SÜDEN and OSTEN, WESTEN will be deleted afterwards.

    :param directions: List of directions with possible list-items: "NORDEN", "SÜDEN", "OSTEN", "WESTEN".
    :return: new List without removed redundant consecutive directions
    """

    # Return if the list does not contain enough items for the algorithm
    if len(directions) < 2:
        return directions

    # (x, y) coords
    dict_num = {"WESTEN": [-1, 0], "OSTEN": [1, 0], "NORDEN": [0, 1], "SÜDEN": [0, -1]}

    # back transformation from 2D cords to character
    # Visualization of back transformation:
    # 2D Array-Index        0       1       -1
    #                  0|         NORDEN  SÜDEN |
    #                  1| OSTEN                 |
    #                 -1| WESTEN                |
    back_transform = [
        [None, "NORDEN", "SÜDEN"],
        ["OSTEN"],
        ["WESTEN"]
    ]

    # Transform direction character into coords
    directions_num = np.array([dict_num[x] for x in directions])

    # length of list before any deletions for check afterwards
    orig_len = len(directions_num)

    # the actual algorithm:
    # look if the 2D coords have a euclidean norm of 0 and collect those indices in a list
    del_indices = []
    for index, value in enumerate(directions_num[:-1]):
        # 2 indices are collected in one run with a positive redundancy check,
        # therefore if an index is already in the list, it should not get checked again
        # because this item is already deleted
        if index not in del_indices and np.linalg.norm(value + directions_num[index+1]) == 0:
            del_indices.append(index)
            del_indices.append(index + 1)

    # do the back transformation and take just those indices that do not appear in the list del_indices
    result = [back_transform[value[0]][value[1]]
              for index, value in enumerate(directions_num)
              if index not in del_indices]

    # Recursively start the algorithm again if there were changes
    # important for lists like: [..., WESTEN, NORDEN, SÜDEN, OSTEN, ...]
    if orig_len != len(result):
        return solve(result)
    else:
        return result


if __name__ == '__main__':
    print('Test 1 with ["WESTEN", "OSTEN", "NORDEN", "NORDEN", "SÜDEN"]')
    directions = ["WESTEN", "OSTEN", "NORDEN", "NORDEN", "SÜDEN"]
    print(solve(directions))

    print('____\nTest 2 with ["NORDEN", "WESTEN", "OSTEN", "SÜDEN", "NORDEN"]')
    print(solve(["NORDEN", "WESTEN", "OSTEN", "SÜDEN", "NORDEN"]))

    print('____\nTest 3 with ["NORDEN", "NORDEN", "OSTEN", "OSTEN", "WESTEN", "WESTEN", "SÜDEN", "WESTEN", ]')
    print(solve(["NORDEN", "NORDEN", "OSTEN", "OSTEN", "WESTEN", "WESTEN", "SÜDEN", "WESTEN", ]))

    print('____\nTest 4 with ["NORDEN"]')
    print(solve(["NORDEN"]))

    print('____\nTest 5 with ["NORDEN", "SÜDEN"]')
    print(solve(["NORDEN", "SÜDEN"]))
