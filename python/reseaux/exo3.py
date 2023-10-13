def no_of_bits(bit_length: int, final_length: int = 32, shift: int = 0) -> str:
    return str(final_length - bit_length * shift).zfill(3) + 'b'


def binary_or_multiple(strings):
    # Ensure all strings are of the same length
    lengths = [len(s) for s in strings]
    if len(set(lengths)) != 1:
        raise ValueError("All strings must be of the same length")

    # Start with a string of '0's as the initial result
    result = '0' * lengths[0]

    # Perform the or operation for each string in the array
    for s in strings:
        result = ''.join('1' if result[i] == '1' or s[i] == '1' else '0' for i in range(len(result)))

    return result


def encrypt(x: int, y: int, z: int, b1: bool, b2: bool) -> int:
    """
    Une fonction qui permet d'encrypter 3 entiers et 2 booleans. \n
    - Chaque entier est codé sur 9 bits \n
    - Les booleans sont codé sur 1 bit \n
    Ces 5 valeurs seront codé dans un nombre binaire de 32 bits. \n

    Example : \n
    x = 241 \n
    y = 13 \n
    z = 411 \n
    b1 = True \n
    b2 = False \n
    (00001110 01101100 00011010 11110001) 2 \n
    (241 965 809) 10 \n

    :param x: (int) [0, 511]
    :param y: (int) [0, 511]
    :param z: (int) [0, 511]
    :param b1: (bool)
    :param b2: (bool)
    :return: La valeur de retour est un nombre decimal représentant le nombre binaire.
    """
    assert 0 <= x <= 511
    assert 0 <= y <= 511
    assert 0 <= z <= 511
    assert isinstance(b1, bool)
    assert isinstance(b2, bool)

    NUMBER_OF_BITS = 32

    # On convertit les entiers en binaire
    xb = format(x, no_of_bits(9)).ljust(NUMBER_OF_BITS, '0')
    yb = format(y, no_of_bits(9, shift=1)).ljust(NUMBER_OF_BITS, '0')
    zb = format(z, no_of_bits(9, shift=2)).ljust(NUMBER_OF_BITS, '0')
    # On convertit les booleans en binaire
    b1 = format(b1, no_of_bits(9, shift=3)).ljust(32, '0')
    b2 = format(b2, no_of_bits(9, shift=4)).ljust(32, '0')

    # On concatène les 5 valeurs
    result = binary_or_multiple([xb, yb, zb, b1, b2])
    return int(result, 2)


def decrypt(secret: int) -> tuple:
    """
    Une fonction qui permet de décrypter un nombre binaire de 32 bits. \n
    Ce nombre binaire représente 5 valeurs : \n
    - 3 entiers codés sur 9 bits \n
    - 2 booleans codés sur 1 bit \n

    :param secret: (int) [0, 2^32 - 1]
    :return: (tuple) (x, y, z, b1, b2)
    """
    assert 0 <= secret <= 2 ** 32 - 1

    # On convertit le nombre binaire en string
    secret = format(secret, no_of_bits(32))
    # On récupère les 5 valeurs
    ints = []
    for i in range(3):
        ints.append(int(secret[32 - 9 * (i + 1):32 - 9 * i], 2))

    b1 = bool(int(secret[32 - 9 * 5], 2))
    b2 = bool(int(secret[32 - 9 * 4], 2))

    return *ints, b1, b2

def test():
    x, y, z = 241, 13, 411
    b1, b2 = True, False
    try:
        secret = encrypt(x, y, z, b1, b2)
        print("Secret:", secret)
        x2, y2, z2, b12, b22 = decrypt(secret)
        assert x == x2
        assert y == y2
        assert z == z2
        assert b1 == b12
        assert b2 == b22
        print("Les valeurs sont correctes")
    except AssertionError:
        print("Error: Les valeurs ne sont pas correctes")


test()
