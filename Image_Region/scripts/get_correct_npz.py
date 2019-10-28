from numpy import load
import sys
import numpy as np

bbox_shape = np.zeros([100, 4], dtype=float)

def main():
        data = load(sys.argv[1])
        lst = data.files



        image_w = data[lst[1]]
        image_h = data[lst[4]]
        num_bbox = data[lst[3]]
        bbox_xy = data[lst[2]]
        vectors_xy = data[lst[0]]

        print(bbox_xy)




if __name__ == '__main__':
    main()