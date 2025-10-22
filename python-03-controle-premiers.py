def main():
    n = 733
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
            break
    return premier

if __name__ == "__main__":
    print(main())