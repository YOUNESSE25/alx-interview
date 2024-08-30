#!/usr/bin/python3
'''IsLand Perimeter'''


def isLand_perimeter(grid):
    '''Island Perimeter function'''
    conteur = 0
    grd_max = len(grid) - 1 
    lst_max = len(grid[0]) - 1
    for lst_idx, lst in enumerate(grid):
        for Land_idx, Land in enumerate(lst):
            if Land == 1:
                if Land_idx == 0:
                    conteur += 1

                    if lst[Land_idx + 1] == 0:
                        conteur += 1
                elif Land_idx == lst_max:
                    if lst[Land_idx - 1] == 0:
                        conteur += 1

                    conteur += 1
                else:
                    if lst[Land_idx - 1] == 0:
                        conteur += 1

                    if lst[Land_idx + 1] == 0:
                        conteur += 1

                if lst_idx == 0:
                    conteur += 1

                    if grid[lst_idx + 1][Land_idx] == 0:
                        conteur += 1
                elif lst_idx == grd_max:
                    if grid[lst_idx - 1][Land_idx] == 0:
                        conteur += 1

                    conteur += 1
                else:
                    if grid[lst_idx - 1][Land_idx] == 0:
                        conteur += 1

                    if grid[lst_idx + 1][Land_idx] == 0:
                        conteur += 1

    return conteur
