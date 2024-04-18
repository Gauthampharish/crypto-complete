import math

def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

def md5_padding(message):
    original_length = len(message) * 8
    message += b'\x80'
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')
    return message

def md5_chunk(message_chunk, state):
    # Constants for MD5
    T = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
    s = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

    a, b, c, d = state

    for i in range(64):
        if i < 16:
            F = (b & c) | ((~b) & d)
            g = i
        elif i < 32:
            F = (d & b) | ((~d) & c)
            g = (5 * i + 1) % 16
        elif i < 48:
            F = b ^ c ^ d
            g = (3 * i + 5) % 16
        else:
            F = c ^ (b | (~d))
            g = (7 * i) % 16

        temp = d
        d = c
        c = b
        b = (b + left_rotate((a + F + T[i] + int.from_bytes(message_chunk[g * 4: (g + 1) * 4], 'little')) & 0xFFFFFFFF, s[i])) & 0xFFFFFFFF
        a = temp

    state[0] = (state[0] + a) & 0xFFFFFFFF
    state[1] = (state[1] + b) & 0xFFFFFFFF
    state[2] = (state[2] + c) & 0xFFFFFFFF
    state[3] = (state[3] + d) & 0xFFFFFFFF

def md5(input_string):
    # Initial MD5 hash values
    state = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    # Pad the message
    padded_message = md5_padding(input_string.encode('utf-8'))

    # Process each 512-bit chunk
    for i in range(0, len(padded_message), 64):
        chunk = padded_message[i:i+64]
        md5_chunk(chunk, state)

    # Convert the final state to a hex string
    result = ''.join(format(val, '08x') for val in state)

    return result

# Example usage
input_string = input("Enter a plain text: ")
md5_result = md5(input_string)
print(f"MD5 hash of '{input_string}': {md5_result}")
