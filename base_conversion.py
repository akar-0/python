def dec2Arb(n, base):
    """
    Convert a number from decimal base to an arbitrary base between 2 and 16.

    Parameters
    ---------
    n (int): number to convert.
    base (int): base for the final writing of n.

    Returns
    ------
    n_conv (int): n converted to decimal base.
    """

    n_conv = ''

    while n > 0:
        n_conv = str(int2hex(n % base)) + n_conv
        n = n // base

    return n_conv


def arb2Dec(n, base):
    """
    Convert a number from an arbitrary base between 2 and 16 to decimal base.

    Parameters
    ---------
    n (int or str): number to convert.
    base (int): base for the original writing of n.

    Returns
    ------
    n_dec (int): n converted to decimal base.
    """
    n = str(n)

    n_conv = 0

    for p in range(1, len(n)+1):
        n_conv += (hex2int(n[-p]) * base**(p-1))

    return n_conv


def hex2int(n):
    if "a" <= n <= "f":
        n = n.upper()

    if n.isdigit():
        return int(n)
    elif "A" <= n <= "F":
        return ord(n) - 55
    else:
        print("This is out of expected values(hextoint).")

def int2hex(n):
    if isinstance(n, int) and 0 <= n < 16:
        if n < 10:
            return n
        else:
            return chr(n + 55)
    else:
        print("This is out of expected values(int2hex).")

def main():
    n = input("Number to be converted:  ")
    base_or = int(input("Original base:  "))
    base_fin = int(input("Final base:  "))

    print(dec2Arb(arb2Dec(n, base_or), base_fin))

main()
