#  Voice-Controlled Tic Tac Toe

Hey there, Zaid here and 
This is a Python-based Tic Tac Toe game that you can play completely hands-free using **voice commands**.  
It integrates **speech-to-text** for move inputs and **text-to-speech** for prompts, making the experience interactive and engaging for two players.

##  How It Works
1. **Game Setup**
   - The board is displayed as a 3x3 matrix with positions from `(0,0)` to `(2,2)`.  
   - Players enter their names and choose their sign: **X** or **O**.  

2. **Gameplay**  
   - Players speak their moves in the format `x.y` (e.g., `1.2` for row 1, column 2).  
   - The game listens via microphone (`SpeechRecognition`) and converts speech to text.  
   - Valid moves are placed on the board using `numpy` for matrix handling.  

3. **Interaction**  
   - The game uses `pyttsx3` to announce prompts like asking for a move or declaring a winner.  
   - Invalid inputs or occupied positions prompt the player to try again.  

4. **Win Checking**  
   - After every move, the game checks all rows, columns, and diagonals for a winning combination.  
   - If a player wins, their name is announced and the game ends.  
   - If the board is full without a winner, it declares a draw.  


## 🚀 Installation & Run
1. Clone the repository.
2. run the main file.

IMPORTANT POINTS:
1. There are two files, one is voice interactive and other is without voice interaction ie, normal keyboard gameplay.

THANK YOU! FOLLOW UP FOR MORE AND MORE EXCITING UPDATES AND PROJECTS! BOOYAH!!!!!!!!
