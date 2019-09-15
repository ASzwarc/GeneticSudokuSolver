from collections import namedtuple

Item = namedtuple("Item", ["row", "col", "value"])


class Board():
    """
    Class for holding already filled sudoku board elements.
    """
    def __init__(self):
        """
        Empty initialises Board.
        """
        self._items = []

    @property
    def items(self):
        """
        Items getter.
        Returns:
            List[Item] -- returns list of already filled elements.
        """
        return self._items

    def inject_board(self):
        """
        Injects predefined sudoku board.
        """
        # Board taken from this page, section "Easiest":
        # https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
        board = []
        board.append(Item._make([0, 3, 2]))
        board.append(Item._make([0, 4, 6]))
        board.append(Item._make([0, 6, 7]))
        board.append(Item._make([0, 8, 1]))

        board.append(Item._make([1, 0, 6]))
        board.append(Item._make([1, 1, 8]))
        board.append(Item._make([1, 4, 7]))
        board.append(Item._make([1, 7, 9]))

        board.append(Item._make([2, 0, 1]))
        board.append(Item._make([2, 1, 9]))
        board.append(Item._make([2, 5, 4]))
        board.append(Item._make([2, 6, 5]))

        board.append(Item._make([3, 0, 8]))
        board.append(Item._make([3, 1, 2]))
        board.append(Item._make([3, 3, 1]))
        board.append(Item._make([3, 7, 4]))

        board.append(Item._make([4, 2, 4]))
        board.append(Item._make([4, 3, 6]))
        board.append(Item._make([4, 5, 2]))
        board.append(Item._make([4, 6, 9]))

        board.append(Item._make([5, 1, 5]))
        board.append(Item._make([5, 5, 3]))
        board.append(Item._make([5, 7, 2]))
        board.append(Item._make([5, 8, 8]))

        board.append(Item._make([6, 2, 9]))
        board.append(Item._make([6, 3, 3]))
        board.append(Item._make([6, 7, 7]))
        board.append(Item._make([6, 8, 4]))

        board.append(Item._make([7, 1, 4]))
        board.append(Item._make([7, 4, 5]))
        board.append(Item._make([7, 7, 3]))
        board.append(Item._make([7, 8, 6]))

        board.append(Item._make([8, 0, 7]))
        board.append(Item._make([8, 2, 3]))
        board.append(Item._make([8, 4, 1]))
        board.append(Item._make([8, 5, 8]))

        self._items = board.copy()
