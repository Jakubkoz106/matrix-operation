def inputaADD():
    q = [int(a) if a.isdigit() else float(a) for a in input("Enter size of first matrix:").split()]
    A = [[int(a) if a.isdigit() else float(a) for a in input("Enter first matrix:").split()] for i in range(q[0])]
    w = [int(a) if a.isdigit() else float(a) for a in input("Enter size of second matrix:").split()]
    B = [[int(a) if a.isdigit() else float(a) for a in input("Enter second matrix:").split()] for i in range(w[0])]
    # c=int(input())
    return [q, A, w, B]


def inputaMULTIPLY():
    q = [int(a) if a.isdigit() else float(a) for a in input("Enter size of matrix:").split()]
    A = [[int(a) if a.isdigit() else float(a) for a in input("Enter matrix:").split()] for i in range(q[0])]
    # w=[int(a) for a in input().split()]
    # B=[[int(a) for a in input().split()] for i in range(w[0])]
    g = input("Enter constant:")
    c = [int(g) if g.isdigit() else float(g)]
    return [q, A, c]


def inputaMULTIPLYTWO():
    q = [int(a) if a.isdigit() else float(a) for a in input("Enter size of first matrix:").split()]
    A = [[int(a) if a.isdigit() else float(a) for a in input("Enter first matrix:").split()] for i in range(q[0])]
    w = [int(a) if a.isdigit() else float(a) for a in input("Enter size of second matrix:").split()]
    B = [[int(a) if a.isdigit() else float(a) for a in input("Enter second matrix:").split()] for i in range(w[0])]
    # c=int(input())
    return [q, A, w, B]


def inputatrans():
    q = [int(a) if a.isdigit() else float(a) for a in input("Enter matrix size:").split()]
    A = [[int(a) if a.isdigit() else float(a) for a in input("Enter matrix:").split()] for i in range(q[0])]
    return [q, A]


def inputainverse():
    q = [int(a) if a.isdigit() else float(a) for a in input("Enter matrix size:").split()]
    A = [[int(a) if a.isdigit() else float(a) for a in input("Enter matrix:").split()] for i in range(q[0])]
    return [q, A]


def menuPrint():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")


def menuTrans():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    wejscie = input("Your choice:")
    return wejscie


def choicetrans(trans):
    if trans == "1":
        dane = inputatrans()
        new = mainDiagonal(dane[0], dane[1])
        printi(new)
    elif trans == "2":
        dane = inputatrans()
        new = sideDiagonal(dane[0], dane[1])
        printi(new)
    elif trans == "3":
        dane = inputatrans()
        new = vertical(dane[0], dane[1])
        printi(new)
    elif trans == "4":
        dane = inputatrans()
        new = horizontal(dane[0], dane[1])
        printi(new)


def append(q, A, w, B):
    if q == w:
        for i in range(q[0]):
            for x in range(q[1]):
                A[i][x] += B[i][x]
        return A
    else:
        print("The operation cannot be performed.")


def multiply(q, A, c):
    for i in range(q[0]):
        for x in range(q[1]):
            A[i][x] *= c[0]
    return A


def between(q, A, w, B):
    if q[1] == w[0]:
        new = []
        for i in range(q[0]):
            db = []
            for x in range(w[1]):
                e = 0

                for z in range(q[1]):
                    e += A[i][z] * B[z][x]
                db.append(e)
            new.append(db)
        return new
    else:
        print("The operation cannot be performed.")


def mainDiagonal(q, A):
    new = []
    for i in range(q[1]):
        sb = []
        for x in range(q[0]):
            sb.append(A[x][i])
        new.append(sb)
    return new


def sideDiagonal(q, A):
    new = []
    for i in range(1, q[1] + 1):
        sb = []
        for x in range(1, q[0] + 1):
            sb.append(A[-1 * x][-1 * i])
        new.append(sb)
    return new


def vertical(q, A):
    new = []
    for i in range(q[1]):
        sb = []
        for x in range(1, q[0] + 1):
            sb.append(A[i][-1 * x])
        new.append(sb)
    return new


def horizontal(q, A):
    new = []
    for i in range(1, q[0] + 1):
        new.append(A[-1 * i])
    return new


def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]

    elif len(A) == 2 and len(A[0]) == 2:
        det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return det

    for x in indices:
        As = A.copy()
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:x] + As[i][x + 1:]

        sign = (-1) ** (x % 2)
        sub_det = determinant_recursive(As)
        total += sign * A[0][x] * sub_det

    return total


def reverse(q, A):
    det = determinant_recursive(A)
    if det != 0:
        new = []
        for i in range(q[0]):
            lis = []
            for x in range(q[1]):
                xs = A.copy()
                xs.pop(i)
                for a in range(len(xs)):
                    xs[a] = xs[a][0:x] + xs[a][x + 1:]
                zm = determinant_recursive(xs)
                aa = (((-1) ** (i + x)) * zm) / det
                lis.append(aa)
            new.append(lis)
        newn = mainDiagonal(q, new)
        printi(newn)
    else:
        print("This matrix doesn't have an inverse.")


def printi(new):
    if new is not None:
        print("The result is:")
        for i in new:
            print(" ".join(str(x) for x in i))


def main():
    while True:
        menuPrint()
        wejscie = input("Your choice:")
        if wejscie == "1":
            dane = inputaADD()
            new = append(dane[0], dane[1], dane[2], dane[3])
            printi(new)
        elif wejscie == "2":
            dane = inputaMULTIPLY()
            new = multiply(dane[0], dane[1], dane[2])
            printi(new)
        elif wejscie == "3":
            dane = inputaMULTIPLYTWO()
            new = between(dane[0], dane[1], dane[2], dane[3])
            printi(new)
        elif wejscie == "4":
            trans = menuTrans()
            choicetrans(trans)
        elif wejscie == "5":
            dane = inputatrans()
            new = determinant_recursive(dane[1])
            print("The result is:\n{}".format(new))
        elif wejscie == "6":
            dane = inputainverse()
            reverse(dane[0], dane[1])
        elif wejscie == "0":
            break


main()