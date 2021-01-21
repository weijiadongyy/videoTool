import os
import shutil

from src.encode_api import HANDLER
from src.PATH import OUT_DIR, VIDEO_DIR


# config = ["MP4META"]
config = ["INITMP4", "MP4META"]


# config = ["MP4TOM3U8"]

# config = ["TOMP4"]

def initVideoList():
    fileList = []
    for root, dirs, files in os.walk(VIDEO_DIR):
        for f in files:
            fileList.append(f)
    return fileList


def init():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.mkdir(OUT_DIR)
    return initVideoList()


def applyVideo(fileName, CACHE_DIR):
    VIDEO_END_DIR = OUT_DIR + "/" + fileName.split(".")[0]
    if os.path.exists(CACHE_DIR):
        shutil.rmtree(CACHE_DIR)
    os.mkdir(CACHE_DIR)
    inUrl = VIDEO_DIR + "/" + fileName
    if len(config) == 0:
        print("请先配置操作")
    elif len(config) > 1:
        for i in range(len(config)):
            outUrl = CACHE_DIR + "/" + str(i)
            hander = config[i]
            inUrl = HANDLER[hander](inUrl, outUrl)
            if None == inUrl:
                print("无法继续之后得操作了吧！！")
                break

        shutil.move(inUrl, VIDEO_END_DIR + "." + inUrl.split(".")[-1])
    else:
        HANDLER[config[0]](inUrl, VIDEO_END_DIR)


def run(fileList):
    CACHE_DIR = OUT_DIR + "/CACHE"
    for file in fileList:
        applyVideo(file, CACHE_DIR)
    shutil.rmtree(CACHE_DIR)


def main():
    run(init())


if __name__ == "__main__":
    main()
