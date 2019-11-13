import pandas as pd
import os.path
import re
from pathlib import Path
import xml.etree.ElementTree as ETree

datafile = '~/Downloads/test_data.csv'
ent_info_file = 'test_phrase_entity.csv'


def get_entity_id(img_id, phr1, phr2):
    entities = []
    entities_with_bbox = []
    with open(os.path.join('/Users/vipulmishra/Downloads/annotations/Sentences/', img_id + '.txt'), 'r') as caption_file:
        captions = caption_file.readlines()
        xml_file = (str(Path.home()) + '/Downloads/annotations/Annotations/' + img_id + '.xml')
        xml_root = ETree.parse(xml_file).getroot()
        for entity in xml_root.iter('object'):
            if entity.find('bndbox') is not None:
                for name in entity.findall('name'):
                    if img_id == '4439654945':
                        print(name.text)
                    entities_with_bbox.append(name.text)
        for caption in captions:
            for match in re.findall(r"[^[]*\[([^]]*)\]", caption.strip()):
                entities.append(match)
    ent_phrase_dict = {}
    for i in entities:
        parts = i.split(' ', 1)
        entity_id = parts[0].strip().split('/')[1][3:]
        phrase = parts[1].strip()
        ent_phrase_dict[phrase] = entity_id

    '''get entities with bbox in xml annotation file'''
    # print([a for a in entities_with_bbox])
    for j, k in ent_phrase_dict.items():
        # print(j, k)
        if j == phr1 or j == phr2:
            if k in entities_with_bbox:
                return k


def main():
    df = pd.read_csv(datafile, dtype = {'image': str, 'original_phrase1' : str, 'original_phrase2' : str})
    with open(ent_info_file, 'w') as writefile:
        print('image_id, phrase1, phrase2, entity_id', file=writefile)
        n = 0
        for row in df.iterrows():
            n+=1
            image_id = row[1][0]
            phrase1 = row[1][3].strip()
            phrase2 = row[1][4].strip()
            entity_id = get_entity_id(image_id, phrase1, phrase2)
            if ',' in phrase1:
                # phrase1 = "\"" + phrase1 + "\""
                phrase1 = phrase1.replace(',', ':', 2) #to ensure all substrings are replaced put 10
            if ',' in phrase2:
                # phrase2 = "\"" + phrase2 + "\""
                phrase2 = phrase2.replace(',', ':', 2)
            # if n == 1045:
            #     print(phrase1)
            #     print(phrase2.replace(',', ':'))
            if entity_id is None:
                print(image_id, entity_id, phrase1, phrase2)
            print(image_id, phrase1, phrase2, entity_id, file=writefile, sep=', ')


if __name__ == '__main__':
    main()
