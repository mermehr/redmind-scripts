# Takes a list of lists of strings and displays it in a well-organized table
# with each column right-justified

def printtable(tabledata):
    # Step 1: Calculate the width of each column
    colwidth = [0] * len(tabledata)
    for i in range(len(tabledata)):
        colwidth[i] = max(len(item) for item in tabledata[i])

    # Step 2: Print the table row by row
    for row in range(len(tabledata[0])): # Number of rows = length of each column list
        for col in range(len(tabledata)):
            print(tabledata[col][row].ljust(colwidth[col]), end=' ')
        print() # Newline after each row

# Example data
tabledata = [['gold', 'diamond', 'sword', 'potion'],
              ['Trogdor', 'Mermehr', 'Lucious', 'Edgar'],
              ['titans', 'ogers', 'imps', 'bragadines']]

printtable(tabledata)