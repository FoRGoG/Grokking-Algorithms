"""pseudocode"""
if word_a[i] == word_b[j]:          # Буквы совпадают
    cell[i][j] = cell[i-1][j-1] + 1 # Буквы не совпадают
else:
    cell[i][j] = 0

if word_a[i] == word_b[j]:          # Буквы совпадают
    cell[i][j] = cell[i-1][j-1] + 1
else:                               # Буквы не совпадают
    cell[i][j] = max(cell[i-1][j], cell[i][j-1])