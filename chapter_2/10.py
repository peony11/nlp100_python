import sys
def line_counter(file):
    cnt = 0
    for line in file:
        cnt += 1
    return cnt

def main():
    f = open(sys.argv[1])
    print line_counter(f)
    f.close()

if __name__ == '__main__':
    main()
