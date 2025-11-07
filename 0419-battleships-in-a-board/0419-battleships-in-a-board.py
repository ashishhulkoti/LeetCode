class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleshipCount = 0 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if (i == 0 or (i-1 >=0 and board[i-1][j] == ".")) and (j == 0 or (j-1 >=0 and board[i][j-1] == ".")):
                        battleshipCount += 1
        return battleshipCount