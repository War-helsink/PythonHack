#/srv/bin/env python


class Noulek:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.argument = ["X", "O"]

    def print_state(self):
        for i, c in enumerate(self.board):
            if (i + 1) % 3 == 0:
                print(f'{c}')
            else:
                print(f'{c}|', end="")

    def good_geme(self, state):
        i = 0
        s = 0
        while s < 3:
            if self.board[i] == state and self.board[i+1] == state and self.board[i+2] == state:
                return True
            elif self.board[s] == state and self.board[s+3] == state and self.board[s+6] == state:
                return True
            s = s + 1
            i = i + 3
        i = 0
        if self.board[i] == state and self.board[i+4] == state and self.board[i+8] == state:
            return True
        elif self.board[i+2] == state and self.board[i+4] == state and self.board[i+6] == state:
            return True
        return False

    def hellow(self, state):
        get = int(input(f"Ход :{state} -->"))
        if self.board[get] == ' ':
            self.board[get] = state
            a = self.good_geme(state)
            if a == True:
                self.Goof_geme(state)
                return True
            return False
        else:
            return True

    def Goof_geme(self, state):
        self.print_state()
        print(f" <-- Победитель --> : {state} :")

    def start(self):
        print("Ход од 0 до 8, нада выбрать клетку")
        try:
            while True:
                for i in self.argument:
                    self.print_state()
                    nulls = self.hellow(i)
                if nulls == True:
                    break
            print("Игра окончена --> :)")
        except IndexError:
            print("Вы вышли за границу доски")
            print("Игра окончена --> :)")


a = Noulek()
a.start()