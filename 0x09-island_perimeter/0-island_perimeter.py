#!/usr/bin/python3
'''IsLand Perimeter'''


def isLand_perimeter(grid):
    '''
    IsLand Perimeter function
    '''
    conteur = 0
    grd_max = len(grid) - 1  # last list in the grid
    lst_max = len(grid[0]) - 1  # last square in list

    for lst_idx, lst in enumerate(grid):
        for Land_idx, Land in enumerate(lst):
            if Land == 1:
                # right and left
                if Land_idx == 0:
                    # left
                    conteur += 1

                    # right
                    if lst[Land_idx + 1] == 0:
                        conteur += 1
                elif Land_idx == lst_max:
                    # left
                    if lst[Land_idx - 1] == 0:
                        conteur += 1

                    # right
                    conteur += 1
                else:
                    # left
                    if lst[Land_idx - 1] == 0:
                        conteur += 1

                    # right
                    if lst[Land_idx + 1] == 0:
                        conteur += 1

                # down and top
                if lst_idx == 0:
                    # top
                    conteur += 1

                    # bottom
                    if grid[lst_idx + 1][Land_idx] == 0:
                        conteur += 1
                elif lst_idx == grd_max:
                    # top
                    if grid[lst_idx - 1][Land_idx] == 0:
                        conteur += 1

                    # bottom
                    conteur += 1
                else:
                    # top
                    if grid[lst_idx - 1][Land_idx] == 0:
                        conteur += 1

                    # bottom
                    if grid[lst_idx + 1][Land_idx] == 0:
                        conteur += 1

    return conteur
