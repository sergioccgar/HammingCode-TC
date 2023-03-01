def generate_hamming_code(data):
    """
    Generates Hamming code for a given data string.
    """
    # Determine number of parity bits required
    m = len(data)
    r = 1
    while 2**r < m + r + 1:
        r += 1

    # Create an array with enough space for data and parity bits
    hamming_code = [0] * (m + r)

    # Fill in data bits
    for i in range(m):
        hamming_code[2**r-1-i] = int(data[m-1-i])

    # Calculate parity bits
    for i in range(r):
        parity = 0
        for j in range(2**i-1, m+r, 2**(i+1)):
            parity ^= hamming_code[j]
        hamming_code[2**i-1] = parity

    # Return the Hamming code as a string
    return ''.join(str(bit) for bit in hamming_code[::-1])


def detect_error_hamming_code(code):
    """
    Detects and corrects single bit errors in a Hamming code.
    """
    # Convert Hamming code string to a list of bits
    hamming_code = list(map(int, code))

    # Determine number of parity bits
    r = 1
    while 2**r < len(hamming_code):
        r += 1

    # Calculate syndrome
    syndrome = 0
    for i in range(r):
        parity = 0
        for j in range(2**i-1, len(hamming_code), 2**(i+1)):
            parity ^= hamming_code[j]
        syndrome += parity * 2**i

    # Check for and correct errors
    if syndrome != 0:
        hamming_code[syndrome-1] ^= 1

    # Return the corrected Hamming code as a string
    return ''.join(str(bit) for bit in hamming_code[::-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("ya moms a hoe")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
