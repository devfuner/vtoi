#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import subprocess
import shutil


base_path = ".\\resource"

"""
-i : 입력파일 이름, 이미지를 추출할 원본 동영상 파일 지정
-r : 출력영상의 프레임 레이트를 변경한다.
-t : 30초 까지만 
"""
# "ffmpeg -i video-filename -r 1 -t 30 image-filename-%2d.jpeg"
command = "ffmpeg -i {0} -r 1 -t 1000 {1}-%4d.jpeg"


def execute_command(path):
    print("PID :", os.getpid())

    for path in glob.glob(path):
        dirname = os.path.dirname(path)
        filename, ext = os.path.splitext(os.path.basename(path))
        dest_dir = os.path.join(dirname, filename)
        # print("filepath :", dirname)
        # print("filename :", filename)
        # print("ext :", ext)  # 첫 문자가 .으로 시작할 수 있음.
        # print("destdir :", dest_dir)

        if os.path.isdir(dest_dir):
            shutil.rmtree(dest_dir)

        os.mkdir(dest_dir)
        os.chdir(dest_dir)

        com_str = command.format(path, filename)
        # print(com_str)

        subprocess.call(com_str.split())
        os.chdir(dirname)


if __name__ == '__main__':
    # execute_command(base_path + "\\*.avi")
    execute_command("D:\\PycharmProjects\\vtoi\\resource\\*.avi")
