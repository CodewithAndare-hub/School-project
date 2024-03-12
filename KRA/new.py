import random
import string

def generate_random_word(length=13):
    # Combine uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    # Generate the random word
    random_word = ''.join(random.choice(characters) for _ in range(length))
    return random_word

# Example usage:
random_13_char_word = generate_random_word()
print(f"Random 13-character word: {random_13_char_word}")
