import pandas as pd
# from collections import namedtuple
import xml.etree.ElementTree as ETree
from Image_Region.scripts.get_correct_npz import *
from pathlib import Path
datafile = 'test_phrase_entity.csv'


def main():
    multiple_bbox_no = 0
    idxs = []
    df = pd.read_csv(datafile, dtype={'image_id': str, 'entity_id': str})
    writefile = open('test_feat_idx.csv', 'w+')
    print('image_id, phrase1, phrase2, entity_id, bottom-up-feats-idx', file=writefile)
    for i in df.iterrows():
        img_id = i[1][0].strip()
        xml_file = (str(Path.home()) + '/Downloads/annotations/Annotations/' + img_id + '.xml')
        xml_root = ETree.parse(xml_file).getroot()
        ent_id = str(i[1][3]).strip()
        xmin, ymin, xmax, ymax = 0, 0, 0, 0
        for entity in xml_root.iter('object'):
            names = [a.text for a in entity.findall('name')]
            if ent_id in names:
                n = 0
                for coord in entity.find('bndbox').iter():
                    if n == 1:
                        xmin = int(coord.text)
                    elif n == 2:
                        ymin = int(coord.text)
                    elif n == 3:
                        xmax = int(coord.text)
                    elif n == 4:
                        ymax = int(coord.text)
                    n += 1
        ra = Rectangle(xmin, ymin, xmax, ymax)
        count, feat_idx = get_overlap_bbox_idx(img_id, ent_id, ra)
        print(img_id, i[1][1].strip(), i[1][2].strip(), ent_id, feat_idx, file=writefile, sep=', ')
        idxs.append(feat_idx)
        if count > 1:
            multiple_bbox_no += 1
    print(multiple_bbox_no)
    print(sum(idxs)/len(idxs))


if __name__ == '__main__':
    main()