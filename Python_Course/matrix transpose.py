 

# Step 1: Ask user for the size of the matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Step 2: Input matrix elements row-wise
print("\nEnter the elements row-wise:")
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Step 3: Create the transpose (flip rows and columns)
transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

# Step 4: Display the result
print("\n Transposed Matrix:")
for row in transpose:
    print(row)
