import random
import sys

TOTAL_NUM = 2712


def main():
    with open(sys.argv[1], 'r') as infile,  open(sys.argv[1], 'a') as editfile:
        content = infile.readlines()
        linenum = len(content)
        print(TOTAL_NUM - linenum)
        for n in range(TOTAL_NUM - linenum):
            print(content[random.randint(0, linenum-1)].strip(), file=editfile)
    with open(sys.argv[1], 'r') as infile,  open(sys.argv[1], 'a') as editfile:
        content = infile.readlines()
        print(len(content))


def shuffle():
    with open(sys.argv[1], 'r') as infile:
        content = infile.readlines()
        print(len(content))
        random.shuffle(content)
        print(len(content))
        with open(sys.argv[1], 'w') as outfile:
            for data_record in content:
                print(data_record.strip(), file=outfile)


if __name__ == '__main__':
    main()
    shuffle()
