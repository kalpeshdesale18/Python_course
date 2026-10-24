

# Step 1: Take matrix sizes from the user
rows_A = int(input("Enter number of rows in Matrix A: "))
cols_A = int(input("Enter number of columns in Matrix A: "))
rows_B = int(input("Enter number of rows in Matrix B: "))
cols_B = int(input("Enter number of columns in Matrix B: "))

# Step 2: Check if matrix multiplication is possible
if cols_A != rows_B:
    print(" Matrix multiplication not possible. Columns of A must equal rows of B.")
else:
    # Step 3: Input elements of Matrix A
    print("\nEnter elements of Matrix A:")
    A = []
    for i in range(rows_A):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        A.append(row)

    # Step 4: Input elements of Matrix B
    print("\nEnter elements of Matrix B:")
    B = []
    for i in range(rows_B):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        B.append(row)

    # Step 5: Create result matrix C with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Step 6: Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                C[i][j] += A[i][k] * B[k][j]

    # Step 7: Display the result
    print("\n Resultant Matrix (A × B):")
    for row in C:
        print(row)
