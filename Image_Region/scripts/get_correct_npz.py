from numpy import load
import sys
import numpy as np
from pathlib import Path
from collections import namedtuple
from collections import Counter

Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')


bbox_shape = np.zeros([100, 4], dtype=float)
most_overlap_bbox_index = 0
most_overlap_bbox_val = 0

# image_region = np.array([1, 20, 3, 26])
# ra = Rectangle(image_region[0], image_region[1], image_region[2], image_region[3])
# image regionの座標((irxlu,irylu), (irxrd,iryrd)) (irxlu - image  region x left up) --  deprecated


'''get index of correct bbox to use for a given VGP'''
def get_correct_bbox(image_w, image_h, num_bbox, bbox_xy , ra):
    overlap_bboxes = {}
    most_overlap_val = 0.0
    most_overlap_idx = 0
    annot_area = get_own_area(None, ra)
    for i in range(num_bbox):
        if bbox_is_fine(bbox_xy, image_w, image_h, i):
            intersect_area = get_overlap_area(bbox_xy, i, ra)
            union_area = annot_area + get_own_area(bbox_xy[i], None) - intersect_area
            ol_area = intersect_area / union_area
            if ol_area > most_overlap_val:
                most_overlap_val = ol_area
                most_overlap_idx = i

    for i in range(num_bbox):
        intersect_area = get_overlap_area(bbox_xy, i, ra)
        union_area = annot_area + get_own_area(bbox_xy[i], None) - intersect_area
        ol_area = intersect_area / union_area
        if ol_area == most_overlap_val:
            overlap_bboxes[i] = ol_area

    return len(overlap_bboxes.values()), most_overlap_idx, most_overlap_val


def get_own_area(bbox_xy, ra):
    if bbox_xy is None:
        return (ra.xmax - ra.xmin) * (ra.ymax - ra.ymin)
    else:
        return (bbox_xy[2] - bbox_xy[0]) * (bbox_xy[3] - bbox_xy[1])


'''get overlap area between region and bbox'''
def get_overlap_area(bbox_xy, i, ra):
    # ra = Rectangle(image_region[0], image_region[1], image_region[2], image_region[3])
    rb = Rectangle(bbox_xy[i][0], bbox_xy[i][1], bbox_xy[i][2], bbox_xy[i][3])
    dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
    dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
    if (dx >= 0) and (dy >= 0):
        return dx * dy
    else:
        return 0


'''check if the parameters of bounding box are proper'''
def bbox_is_fine(bbox_axes, img_w, img_h, i):
    if bbox_axes[i][1] >= bbox_axes[i][3] or bbox_axes[i][0] >= bbox_axes[i][2]:
        return False
    for j in range(4, 2):
        if bbox_axes[i][j] > img_w:
            return False
            print('false')
        if bbox_axes[i][j+1] > img_h:
            return False
    return True


def get_overlap_bbox_idx(img_id, entity_id, ra):
    data = load(str(Path.home()) + '/Documents/Extras/アルバイト/Datability/bottom-up-feats/' + img_id + '.jpg.npz')
    lst = data.files
    image_w, image_h = data[lst[1]], data[lst[4]]
    num_bbox, bbox_xy = data[lst[3]], data[lst[2]]
    count, feat_idx, val = get_correct_bbox(image_w, image_h, num_bbox, bbox_xy, ra)
    print('value', val)
    return count, feat_idx


def main():
    data = load(sys.argv[1])
    lst = data.files
    image_w, image_h = data[lst[1]], data[lst[4]]
    num_bbox, bbox_xy = data[lst[3]], data[lst[2]]
    vectors_xy = data[lst[0]]
    get_correct_bbox(image_w, image_h, num_bbox, bbox_xy)
    print(most_overlap_bbox_index)


if __name__ == '__main__':
    main()
