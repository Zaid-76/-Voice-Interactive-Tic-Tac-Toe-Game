import numpy as np


class TTT():
    ch = ' '
    print("positions:")
    a = np.matrix([["(0,0)", "(0,1)", "(0,2)"], ["(1,0)", "(1,1)", "(1,2)"], ["(2,0)", "(2,1)", "(2,2)"]])
    print(a)
    p1 = input("enter player 1 name: ")
    p2 = input("enter player 2 name: ")
    while True:
        s1 = input(f"select your sign(X/O) {p1}: ")
        if (s1 == 'X' or s1 == 'O'):
            break
        print("please enter either X or O (in caps)")
        continue
    while True:
        s2 = input(f"select your sign(X/O) {p2}: ")
        if (s2 == 'X' or s2 == 'O'):
            break
        print("please enter either X or O (in caps)")
        continue

    print("lets begin! \n")

    def p1f(self, p1):
        while True:
            (i, c, j) = tuple((input(f"enter your positions as x,y {p1}: ")))
            if (int(i) < 3 and int(j) < 3):
                return int(i), int(j)
            else:
                print("enter correct positions w.r.t to position matrix given above!")

    def p2f(self, p2):
        while True:
            (i, c, j) = tuple((input(f"enter your positions as x,y {p2}: ")))
            if (int(i) < 3 and int(j) < 3):
                return int(i), int(j)
            else:
                print("enter correct positions w.r.t to position matrix given above!")

    def gp(self):
        count = 9
        while count >= 0:
            pos1, pos2 = self.p1f(self.p1)
            if (self.a[pos1, [pos2]] != self.s1 and self.a[pos1, [pos2]] != self.s2):
                self.a[pos1, [pos2]] = self.s1
            else:
                print("position already used, enter a new position")
                continue
            print(self.a)
            self.check()
            if (self.ch == self.s1):
                print(f"{self.p1} won the game!")
                exit()
            if count == 1:
                break
            while True:
                pos3, pos4 = self.p2f(self.p2)
                if (self.a[pos3, [pos4]] != self.s2 and self.a[pos3, [pos4]] != self.s1):
                    self.a[pos3, [pos4]] = self.s2
                    break
                else:
                    print("position already used, enter a new position")
                    continue
            print(self.a)
            self.check()
            if (self.ch == self.s2):
                print(f"{self.p2} won the game!")
                exit()
            count -= 2
        return 0

    def ck(self, ar):
        an_array = ar
        another_array1 = [['X'], ['X'], ['X']]
        another_array2 = [['O'], ['O'], ['O']]
        comparison1 = an_array == another_array1
        equal_arrays1 = comparison1.all()
        comparison2 = an_array == another_array2
        equal_arrays2 = comparison2.all()
        if (equal_arrays1 == True):
            return 'X'
        if (equal_arrays2 == True):
            return 'O'
        return None

    def check(self):
        d1 = self.ck(self.a.diagonal())
        d2 = self.ck(np.fliplr(self.a).diagonal())
        for i in range(3):
            col = self.ck(self.a[:, i])
            row = self.ck(self.a[i, :])
            if (col == 'X' or row == 'X' or d1 == 'X' or d2 == 'X'):
                self.ch = 'X'
                break
            if (col == 'O' or row == 'O' or d1 == 'O' or d2 == 'O'):
                self.ch = 'O'
                break
            if (col == None or row == None or d1 == None or d2 == None):
                continue
        return self.ch

    def end(self):
        if (self.ch == self.s1):
            print(f"{self.p1} won the game!")
        if (self.ch == self.s2):
            print(f"{self.p2} won the game!")
        if (self.ch == ' '):
            print("the game has ended with a draw!")
        return 0


def main():
    obj = TTT()
    obj.gp()
    obj.check()
    obj.end()


main()
