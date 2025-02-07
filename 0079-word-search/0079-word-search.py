class Solution:
    def exist_helper(self,board,i,j,word_array,k):
        # print(i,j,k)
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word_array[k]:
            return False
        if k==0:
            return True
        tmp=board[i][j]
        board[i][j]=""
        if self.exist_helper(board,i+1,j,word_array,k-1) or self.exist_helper(board,i,j+1,word_array,k-1) or self.exist_helper(board,i-1,j,word_array,k-1) or self.exist_helper(board,i,j-1,word_array,k-1):
            return True
        else:
            board[i][j]=tmp
            return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        if m*n < len(word):
            return False
        word_array=list(word)
        lw=len(word_array)-1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]==word_array[lw] and self.exist_helper(board,i,j,word_array,lw):
                    return True
        return False
                