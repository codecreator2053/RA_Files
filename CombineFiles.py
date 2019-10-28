import sys
import random


def main():
    with open(sys.argv[1][:-4] + '_oversampled.csv', 'w+') as outfile:
        File_attr =  ['Alternation', 'Entailment1', 'Entailment2', 'Equivalence', 'Independence']
        for attr in File_attr:
            infile = open(str(sys.argv[1])[:-4] + '_' + attr + '.csv', 'r')
            content = infile.readlines()
            for line in content:
                print(line.strip(), file=outfile)
    with open(sys.argv[1][:-4] + '_oversampled.csv', 'r') as newfile:
        content = newfile.readlines()
        random.shuffle(content)
        with open(sys.argv[1][:-4] + '_oversampled.csv', 'w+') as outfile, open(sys.argv[1], 'r') as assistfile:
            print(assistfile.readline(), file=outfile)
            for line in content:
                print(line.strip(), file=outfile)


if __name__ == '__main__':
    main()
