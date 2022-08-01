import os
from src.PATH import BIN_SHELL_DIR



def pathApply(value):
    value = value.replace("/", "\\")
    return value
    # return "\"" + value + "\""


def moveMp4MetaToHead(inUrl, outUrl):
    outUrl = outUrl + ".mp4"

    shell = pathApply(BIN_SHELL_DIR["faststart"]) + " " + pathApply(inUrl) + " " + pathApply(outUrl)
    print(shell)

    os.system(shell)

    return outUrl


def initMp4(inUrl, outUrl):
    outUrl = outUrl + ".mp4"

    shell = pathApply(BIN_SHELL_DIR["ffmpeg"]) + \
            " -i " + pathApply(inUrl) + \
            " -acodec copy -vcodec copy " + \
            pathApply(outUrl)
    print(shell)

    os.system(shell)

    return outUrl


def mp4ToM3u8(inUrl, outUrl):
    os.mkdir(outUrl)
    m3u8Url = outUrl + "/" + outUrl.split("/")[-1] + ".m3u8"
    outUrl = outUrl + "/" + outUrl.split("/")[-1] + "-%07d.m3u8"

    shell = pathApply(BIN_SHELL_DIR["ffmpeg"]) + \
            " -i " + pathApply(inUrl) + \
            " -c:v libx264 -hls_time 5 -hls_list_size 0 -c:a aac -strict -2 -f hls " + \
            pathApply(outUrl)
    print(shell)

    os.system(shell)
    os.rename(outUrl, m3u8Url)

    return None

def mp4ToGif(inUrl, outUrl):
    outUrl = outUrl + ".gif"
    shell = pathApply(BIN_SHELL_DIR["ffmpeg"]) + \
            " -i " + pathApply(inUrl) + \
            "" + \
            pathApply(outUrl)
    print(shell)

    os.system(shell)
    return outUrl


HANDLER = {
    "INITMP4": initMp4,
    "MP4META": moveMp4MetaToHead,
    "MP4TOM3U8": mp4ToM3u8,
    "MP4TOGIF": mp4ToGif,
}
