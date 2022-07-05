def gcd(a, b):
    """
    Compute the GCD of a and b.

        Parameters:
            a (int): an nonnegative integer
            b (int): an nonnegative integer

        Returns:
            int: the gcd of a and b
    """

    # TODO
    if b == 0:
        return 0
    else:
        return 0


def exgcd(a, b):
    """
    Compute the GCD of a and b with coefficients satisfying ax+by=gcd(a, b).

        Parameters:
            a (int): an nonnegative integer
            b (int): an nonnegative integer

        Returns:
            (int, int, int): a tuple of (x, y, g)
    """

    # TODO
    if b == 0:
        return (0, 0, 0)
    else:
        return (0, 0, 0)


action = input()
# input a and b
a = int(input())
b = int(input())

# compute and output
if action == "gcd":
    print(gcd(a, b))
else:
    x, y, g = exgcd(a, b)
    print(x)
    print(y)
    print(g)
