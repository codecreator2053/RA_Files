import sys
import pandas as pd
fin = 'full_data_type_phrase_pair_train.csv'


def main():
    with open(sys.argv[1], 'r') as infile, open(sys.argv[1], 'r') as infile2:
        csv_content = pd.read_csv(infile, dtype={'type_label': int})
        content = infile2.readlines()
        altfile = open(str(sys.argv[1])[:-4] + '_Alternation.csv', 'w')
        ent1file = open(str(sys.argv[1])[:-4] + '_Entailment1.csv', 'w+')
        ent2file = open(str(sys.argv[1])[:-4] + '_Entailment2.csv', 'w+')
        equfile = open(str(sys.argv[1])[:-4] + '_Equivalence.csv', 'w+')
        indfile = open(str(sys.argv[1])[:-4] + '_Independence.csv', 'w+')
        for index, row in csv_content.iterrows():
            if row['type_label'] == 0:
                print(content[index+1].strip(), file=altfile)
            if row['type_label'] == 1:
                print(content[index+1].strip(), file=ent1file)
            if row['type_label'] == 2:
                print(content[index+1].strip(), file=ent2file)
            if row['type_label'] == 3:
                print(content[index+1].strip(), file=equfile)
            if row['type_label'] == 4:
                print(content[index+1].strip(), file=indfile)


if __name__ == '__main__':
    main()
