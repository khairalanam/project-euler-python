from itertools import permutations


def decrypt(ciphertext, key):
    return ''.join(chr(ciphertext[i] ^ key[i % 3]) for i in range(len(ciphertext)))


def find_key(ciphertext):
    for key in permutations(range(97, 123), 3):
        decrypted = decrypt(ciphertext, key)
        if ' the ' in decrypted.lower():
            return key


def main():
    with open('cipher.txt') as file:
        ciphertext = list(map(int, file.read().strip().split(',')))

    key = find_key(ciphertext)
    decrypted_text = decrypt(ciphertext, key)

    result = sum(ord(char) for char in decrypted_text)
    print(result)


if __name__ == "__main__":
    main()
