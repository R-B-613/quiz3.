from colors import bcolors


def newton_raphson(f, df, p0, TOL, N=50):

    for i in range(N):
        if df(p0) == 0:
            print( "Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / df(p0)

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<10}".format("Iteration", i))
        p0 = p
    return p


if __name__ == '__main__':
    f = lambda x: x**2 - 5
    df = lambda x: 2*x
    p0 = 1
    TOL = 1e-6
    N = 100
    roots = newton_raphson(f, df,p0,TOL,N)
    print(bcolors.OKBLUE,"\nThe equation f(x) has an approximate root at x = {:<15.9f} ".format(roots),bcolors.ENDC,)