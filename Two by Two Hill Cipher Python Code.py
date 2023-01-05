keyMatrix = [[0] * 2 for i in range(2)]
 
# Generate vector for the message
messageVector = [[0] for i in range(2)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(2)]
 
# Following function generates the
# key matrix for the key string
def MatrixKey(key):
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypt(messageVector):
    for i in range(2):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(2):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    MatrixKey(key)
 
    # Generate vector for the message
    for i in range(2):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypt(messageVector)
 
    # Generate the encrypted text
    # from the encrypted vector
    CipherText = []
    for i in range(2):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    # Finally print the ciphertext
    print("Ciphertext: ", "".join(CipherText))
 
# Driver Code

# Get the message to be encrypted

text = "CA"
text2 = "KE"

# Get the key
key = "BAKE"

HillCipher(text, key)
HillCipher(text2, key)

#following code were taken from geeksforgeeks website and modified