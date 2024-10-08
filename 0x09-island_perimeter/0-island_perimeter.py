#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''Island Perimeter function'''
    cont = 0
    grid_max = len(grid) - 1  # last list in the grid
    lst_max = len(grid[0]) - 1  # last square in list

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if land_idx == 0:
                    # left
                    cont += 1

                    # right
                    if lst[land_idx + 1] == 0:
                        cont += 1
                elif land_idx == lst_max:
                    # left
                    if lst[land_idx - 1] == 0:
                        cont += 1

                    # right
                    cont += 1
                else:
                    # left
                    if lst[land_idx - 1] == 0:
                        cont += 1

                    # right
                    if lst[land_idx + 1] == 0:
                        cont += 1

                # top and down
                if lst_idx == 0:
                    # top
                    cont += 1

                    # bottom
                    if grid[lst_idx + 1][land_idx] == 0:
                        cont += 1
                elif lst_idx == grid_max:
                    # top
                    if grid[lst_idx - 1][land_idx] == 0:
                        cont += 1

                    # bottom
                    cont += 1
                else:
                    # top
                    if grid[lst_idx - 1][land_idx] == 0:
                        cont += 1

                    # bottom
                    if grid[lst_idx + 1][land_idx] == 0:
                        cont += 1

    return cont
