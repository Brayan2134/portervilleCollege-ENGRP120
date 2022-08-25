def main(n):

    n_before1 = n - 1
    print("3 to the ", n_before1, " is: ", 3 ** n_before1)

    print("3 to the ", n, " is: ", 3 ** n)

    n_after1 = n + 1
    print("3 to the n plus ", n_after1, " is: ", 3 ** n_after1)





    final = 0
    for i in range(n + 1):
        final = final + (3 ** i)
    
    print(final)
main(3)