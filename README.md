# GuessGame
This is a Python application for GuessGame.

You can clone the repository and start the game by running main.py file.

You can choose a length for the passcode. Then, the game will generate a secret passcode with that length. Your task is to crack the code by making guesses.

# Usage:
You can start playing the game by running the command below:

```
python main.py
```

# Cracking the Passcode:
Let's say the passcode generated is 45387 (length = 5).

If you make a guess of 12345, the application will print this line:
```
12345
  3**
```

This means, digit '3' is in the right position. Digits '4' and '5' are in the passcode, but they are in wrong positions. So, you make another guess:

```
45367
453 7
```

This means, there is no digit '6' in passcode. So, you continue guessing and find that the passcode is 45387.
