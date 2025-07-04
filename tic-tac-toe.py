import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')
        self.player = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text='', font=('Arial', 40), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_click(self, idx):
        if self.board[idx] == '' and not self.check_winner():
            self.board[idx] = self.player
            self.buttons[idx].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo('Game Over', f'Player {self.player} wins!')
                self.reset_board()
            elif '' not in self.board:
                messagebox.showinfo('Game Over', 'It\'s a tie!')
                self.reset_board()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for w in wins:
            if self.board[w[0]] == self.board[w[1]] == self.board[w[2]] != '':
                return True
        return False

    def reset_board(self):
        self.board = ['' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text='')
        self.player = 'X'

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()