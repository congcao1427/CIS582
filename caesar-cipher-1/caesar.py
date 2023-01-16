
def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    inc = key % 26
    num_letter = ord(letter)
    num_letter += inc
    if num_letter>90:
        num_letter = num_letter-26
    letter_new = chr(num_letter)
    ciphertext += letter_new
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    dec = key % 26
    num_letter = ord(letter)
    num_letter -= dec
    if num_letter<65:
        num_letter = num_letter+26
    letter_new = chr(num_letter)
    plaintext += letter_new    
    return plaintext


