# Password Generator

A simple command-line password generator written in Python. It creates a random password made of **letters, digits and special characters** of the length you choose.

> **Note:** This is a learning project. It uses Python's `random` module, which is not designed for security. Do not use it to protect real accounts.

## Features

- Choose your own password length
- Mixes uppercase letters, lowercase letters, digits and special characters (`! @ # $ % & *`)
- Letters and digits are placed at random positions
- Special characters are scattered randomly (about one quarter of the password)
- Works for lengths from 4 up to 40

## Requirements

- Python 3.x
- No external libraries needed (uses only the built-in `random` module)

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python password_generator.py
   ```

4. Enter the length when asked:

   ```
   Enter length of password(Minimum 4 is recomended): 12
   ```

5. Your password is printed, for example:

   ```
   aT7#k2Q&x9Lm
   ```

## How It Works

1. `char1()` builds a list of all uppercase and lowercase letters.
2. `char2()` builds a list of digits (0-9, repeated to allow longer passwords).
3. Half of the positions (chosen randomly) get letters, and the rest get digits.
4. About `n // 4` random positions are then replaced with special characters.
5. The final password is printed.

## Limitations

- Maximum length is **40**, because `random.sample` cannot pick more digits than the list contains.
- Minimum recommended length is 4. There is no input check yet, so text or very small numbers may cause errors.
- Not cryptographically secure (see the note at the top).

## Future Improvements

- Remove the length limit by using `random.choice`
- Add input validation
- Use the `secrets` module for secure passwords
- Let the user choose which character types to include
- Copy the password to the clipboard

## Author

Made by a 1st-year B.Tech CSE student as a Python practice project.
