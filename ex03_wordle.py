"""Wordle restricted to 6 guesses."""

__author__ = "730400691"


def contains_char(secret_word: str, single_character: str) -> bool:
    """Checks to see if a single character is present anywhere within the word."""
    assert len(single_character) == 1
    index_yellow_check: int = 0
    while index_yellow_check < len(secret_word):
        if single_character == secret_word[index_yellow_check]:
            return True
        index_yellow_check += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Returns a colored emoji sequence that tells you what part of your guess is correct."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    emoji_str: str = ""
    while index < len(secret_word):
        if guess[index] == secret_word[index]:
            emoji_str += GREEN_BOX
        elif contains_char(secret_word, guess[index]) is True:
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        index += 1
    return emoji_str   


def input_guess(expected_length: int) -> str:
    """Prompts the user to continue to guess a word until it meets the required length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess 


def main() -> None:
    """The entrypoint of the program and the game loop."""
    turn_number: int = 1
    turn_str: str = ""
    winning_status: bool = False
    # these are variables exclusive to the game loop and aren't used in any of the other three defined functions.

    while turn_number <= 6 and winning_status is False:
        # There are two things that need to happen for you to guess again: you haven't reached six guess and you haven't guessed the secret word. So, two conditions for while loop.
        secret_word: str = "codes"
        expected_length: int = len(secret_word)
        emoji_str: str = ""
        guess: str = ""
        # First you have to define all of your variables so they can be manipulated by the functions in later stages, and so they can reset at the beginning of each loop. Otherwise you guess variable will just become a string of all of your guesses.
        turn_str = f"=== Turn {turn_number}/6 ==="
        print(turn_str)
        guess += input_guess(expected_length)
        emoji_str += emojified(guess, secret_word)
        print(emoji_str)
        if guess == secret_word:
            winning_status = True
        else:
            turn_number += 1
    
    if winning_status is True:
        print(f"You won in {turn_number}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    # These statements are separate from the while loop because they're printed at the very end of the game.


if __name__ == "__main__":
    main()
# Let's us run the main function as a module instead of importing it in a REPPL each time
