#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from PIL import Image
from shutil import copy
from dhash import dhash


def img_diff(orig, modif, hash_size):
    # o = Image.open(orig).crop((0, 0, 1920, 800))
    # m = Image.open(modif).crop((0, 0, 1920, 800))
    o = Image.open(orig)
    m = Image.open(modif)
    if dhash(o, hash_size) != dhash(m, hash_size):
        print("Difference Image {0} / {1}".format(orig, modif))
        return True


if __name__ == '__main__':
    event_dir = "D:\\PycharmProjects\\vtoi\\resource\\event\\"

    if not os.path.isdir(event_dir):
        os.mkdir(event_dir)

    file_list = glob.glob("D:\\PycharmProjects\\vtoi\\resource\\cctv\\*")

    for idx, file in enumerate(file_list):
        try:
            print(file, file_list[idx + 1])
            if img_diff(file, file_list[idx + 1], 4):
                copy(file, event_dir)
        except IndexError as e:
            print(e)
