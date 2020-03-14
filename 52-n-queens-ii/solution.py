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
            return [a for a in board]

        n = input_n
        board = [-1 for i in range(n)]
        res = []
        place(board, 0, res)
        return len(res)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n < 4:
            return 0
        return self.n_queens(n)
