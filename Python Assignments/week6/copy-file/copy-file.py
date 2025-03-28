def main():
    f1 = open("example.txt")
    f2 = open("example2.txt","a")
    for line in f1:
        f2.write(line)
    f1.close()
    f2.close()


if __name__ == "__main__":
    main()