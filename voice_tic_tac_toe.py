import numpy as np
import speech_recognition as sr
import pyttsx3
import pyaudio

r = sr.Recognizer() # Speech recognition Object


def tts(command): # Text to speech function
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    return 0


def stt(): # Speech to text function
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source=source2, duration=0.2)
        audio2 = r.listen(source2)
        mytext = r.recognize_google(audio2)
        mytext = mytext.lower() # Simple pre-processing
    return mytext


class TTT(): # Main tic tac toe class
    ch = ' ' # Global variable
    print("positions:")
    a = np.matrix([["(0,0)", "(0,1)", "(0,2)"], ["(1,0)", "(1,1)", "(1,2)"], ["(2,0)", "(2,1)", "(2,2)"]])
    print(a)
    tts("enter player 1 name: ")
    p1 = input("enter player 1 name: ")
    tts("enter player 2 name: ")
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
    print("tell your positions as x.y at faster pace") # x dot y
    tts("tell your positions as x.y at a faster pace")

    print("lets begin! \n")

    def p1f(self, p1): # Player 1
        while True:
            print(f"tell your positions  {p1}: ")
            mys2 = stt()
            (i, c, j) = tuple(mys2)
            if (int(i) < 3 and int(j) < 3): # Check for valid position
                return int(i), int(j)
            else:
                print("enter correct positions w.r.t to position matrix given above!")

    def p2f(self, p2): # Player 2
        while True:
            print(f"tell your positions  {p2}: ")
            mys1 = stt()
            (i, c, j) = tuple(mys1)
            if (int(i) < 3 and int(j) < 3):
                return int(i), int(j)
            else:
                print("enter correct positions w.r.t to position matrix given above!")

    def gp(self): # Game play function
        count = 9
        while count >= 0: # Keeping track of all 9 positions on the board
            pos1, pos2 = self.p1f(self.p1)
            if (self.a[pos1, [pos2]] != self.s1 and self.a[pos1, [pos2]] != self.s2): # Check for availability of position
                self.a[pos1, [pos2]] = self.s1
            else:
                print("position already used, enter a new position")
                continue
            print(self.a)
            self.check() # Check if the player has won the game mid game
            if (self.ch == self.s1):
                print(f"{self.p1} won the game!")
                exit()
            if count == 1:
                break
            while True: # For second player
                pos3, pos4 = self.p2f(self.p2)
                if (self.a[pos3, [pos4]] != self.s2 and self.a[pos3, [pos4]] != self.s1):
                    self.a[pos3, [pos4]] = self.s2
                    break
                else:
                    print("position already used, enter a new position")
                    continue
            print(self.a)
            self.check() # Check if the player has won the game mid game
            if (self.ch == self.s2):
                print(f"{self.p2} won the game!")
                exit()
            count -= 2 # Two positions were used
        return 0

    def ck(self, ar): # For determining which player's sign belongs to the array ar
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
        # Check for game winning

        # Determining two diagonals of the board
        d1 = self.ck(self.a.diagonal())
        d2 = self.ck(np.fliplr(self.a).diagonal())
        for i in range(3): # Checking for winning conditions
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
    # If any player wins the game in mid then this program exits after displaying the players name!
    # If no one wins the below functions are executed!
    obj.check() # This is done to check the winning condition after game play has ended
    obj.end() # To display who won the game


main()
