from colors import bcolors


def secant_method(f, x0, x1, TOL, N=50):

    for i in range(N):
        if f(x1) - f(x0) == 0:
            print( " method cannot continue.")
            return

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<10}".format("Iteration:", i))
        x0 = x1
        x1 = p

    return p


if __name__ == '__main__':
    f = lambda x: x**2 - 5
    x0 = -1
    x1 = 0
    TOL = 1e-6
    N = 20
    roots = secant_method(f, x0, x1, TOL, N)
    print(bcolors.OKBLUE, f"\n The equation f(x) has an approximate root at x = {roots}", bcolors.ENDC)