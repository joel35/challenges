def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0  # var. for the counts

    for row_num, row in enumerate(grid):
        for col_num, item in enumerate(row):
            islands += mark_islands(row_num, col_num, grid)
    return islands


def mark_islands(row_num, col_num, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    if is_item_invalid(row_num, col_num, grid) or \
            grid[row_num][col_num] == '#' or \
            grid[row_num][col_num] == 0:
        return 0

    grid[row_num][col_num] = '#'

    top_neighbor = {
        'row': row_num - 1,
        'col': col_num
    }
    bottom_neighbor = {
        'row': row_num + 1,
        'col': col_num
    }
    left_neighbor = {
        'row': row_num,
        'col': col_num - 1
    }
    right_neighbor = {
        'row': row_num,
        'col': col_num + 1
    }

    neighbors = [
        top_neighbor,
        bottom_neighbor,
        left_neighbor,
        right_neighbor
    ]

    for neighbor in neighbors:
        mark_islands(neighbor['row'], neighbor['col'], grid)

    return 1


def is_item_invalid(row_num, col_num, grid):
    return row_num < 0 or \
           row_num >= len(grid) or \
           col_num < 0 or \
           col_num >= len(grid[0])
