
def main():
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    print_board(rows, columns)

def print_board(rows,cols):
    for _ in range(rows):
        print(" ---" * cols)
        print("|   " * (cols+1))
    print(" ---" * cols)    
        
if __name__ == "__main__":
	main()