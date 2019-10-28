import sys
import pandas as pd


def main():
    with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w+') as outfile:
        csv_content = pd.read_csv(infile, dtype={'type_label': int})
        content = open(sys.argv[1], 'r').readlines()
        print(content[0].strip(), file=outfile)
        for index, row in csv_content.iterrows():
            if row['type_label'] == 2:
                changed = content[index + 1].strip()[:-3] + '1,1'
                print(changed, file=outfile)
            else:
                print(content[index+1].strip(), file=outfile)


if __name__ == '__main__':
    main()