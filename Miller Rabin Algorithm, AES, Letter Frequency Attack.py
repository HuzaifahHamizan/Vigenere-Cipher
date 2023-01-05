import random

def is_prime(n, k=10):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

# To use this function, simply call is_prime(n),
# where n is the number you want to test for primality.
# The optional parameter k controls the accuracy of the test,
# with a higher value of k resulting in a more accurate test but also longer runtime.

def key_expansion(key):
    # Initialize round keys with key
    round_keys = [key]

    # Set Rcon values
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

    # Set number of rounds based on key length
    if len(key) == 16:
        rounds = 10
    elif len(key) == 24:
        rounds = 12
    elif len(key) == 32:
        rounds = 14
    else:
        raise ValueError("Invalid key length")

    for i in range(1, rounds + 1):
        # Initialize the current round key with zeros
        round_key = [0] * 16

        # Copy previous round key to current round key
        for j in range(4):
            round_key[j] = round_keys[i - 1][j]
            round_key[j + 4] = round_keys[i - 1][j + 4]
            round_key[j + 8] = round_keys[i - 1][j + 8]
            round_key[j + 12] = round_keys[i - 1][j + 12]

        # Perform key expansion
        if i % rounds == 0:
            # Rotate the bytes in the current round key
            temp = round_key[15]
            for j in range(15, 4, -1):
                round_key[j] = round_key[j - 1]
            round_key[4] = temp

            # Apply S-Box substitution to each byte in the current round key
            for j in range(4, 16):
                round_key[j] = sbox[round_key[j]]

            # XOR the current round key with the Rcon value for this round
            round_key[0] = round_key[0] ^ Rcon[i // rounds - 1]

        else:
            # XOR the current round key with the previous round key
            for j in range(4, 16):
                round_key[j] = round_key[j - 4] ^ round_key[j - 1]

        # Add the current round key to the list of round keys
        round_keys.append(round_key)

    return round_keys
# This function takes a single argument, key, which is the encryption key. The key can be 16, 24, or 32 bytes long,
# corresponding to 128-bit, 192-bit, and 256-bit keys, respectively.
# The function returns a list of round keys, which are used in the different rounds of the AES algorithm.
# To use this function, simply call key_expansion(key), where key is a byte array representing the encryption key.



from collections import Counter

def letter_frequency_attack(ciphertext):
    # Initialize a dictionary of letter frequencies in English
    letter_frequencies = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
        'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
        'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
        'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
        'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
        'y': 0.01974, 'z': 0.00074
    }

    # Count the frequency of each letter in the ciphertext
    ciphertext_frequencies = Counter(ciphertext)

    # Initialize a list of possible plaintexts
    plaintexts = []

    # Iterate over the letters in the ciphertext and create a mapping
    # between each letter and the most likely corresponding letter in English
    mapping = {}
    for letter in ciphertext_frequencies:
        most_likely_letter = max(letter_frequencies, key=lambda x: letter_frequencies[x])
        mapping[letter] = most_likely_letter
        letter_frequencies.pop(most_likely_letter)

    # Use the mapping to create a possible plaintext
    plaintext = ""
    for letter in ciphertext:
        plaintext += mapping[letter]
    plaintexts.append(plaintext)

    return plaintexts

S
# The function returns a list of possible plaintexts, sorted in rough order of likelihood based on letter frequency.
# To use this function, simply call letter_frequency_attack(ciphertext), where ciphertext is a string representing the ciphertext.
# Here's an example of how you can use this function to perform a letter frequency attack on a monoalphabetic substitution cipher:


ciphertext = "zfspdfttbdf"
plaintexts = letter_frequency_attack(ciphertext)

# Print the top 5 possible plaintexts
for i in range(5):
    print(plaintexts[i])





