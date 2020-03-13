class Solution(object):

    def n_queens(self, input_n):
        def place(board, row, res):
            if row == n:
                res.append(output(board))
                return
            for j in range(n):
                board[row] = j
                if check_pass(board, row):
                    place(board, row + 1, res)

        def check_pass(board, row):
            current_index = board[row]
            for i in range(row):
                if board[i] == current_index:
                    return False
                if (board[i] + i) == (current_index + row):
                    return False
                if (board[i] - i) == (current_index - row):
                    return False
            return True

        def output(board):
            r = []
            size = len(board)
            for i in range(size):
                row = ""
                for j in range(size):
                    if board[i] == j:
                        row += "Q"
                    else:
                        row += "."
                r.append(row)
            return r

        n = input_n
        board = [-1 for i in range(n)]
        res = []
        if n == 1:
            return [['Q']]
        if n < 4:
            return []
        place(board, 0, res)
        return res

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return self.n_queens(n)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(self.n_queens(n))
