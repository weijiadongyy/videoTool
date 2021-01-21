import os
print(os.getcwd())

OUT_DIR = os.getcwd() + "/../out"
VIDEO_DIR = os.getcwd() +"/../video"

BIN_DIR = os.getcwd() +"/../bin"

BIN_SHELL_DIR = {
    "faststart": BIN_DIR + "/faststart/qt-faststart.exe",
    "ffmpeg": BIN_DIR + "/ffmpeg/bin/ffmpeg.exe",
    "ffprobe": BIN_DIR + "/ffmpeg/bin/ffprobe.exe"
}

def pathApply(value):
    value = value.replace("/", "\\")
    return value