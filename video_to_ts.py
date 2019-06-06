import subprocess
import sys
import os
from urllib.parse import  quote_plus


def make_ts(video_path):
    video_name =quote_plus(os.path.splitext( video_path.split("/")[-1])[0])
    video_ts_directory = os.path.join("videos" ,video_name)
    if  not os.path.exists(video_ts_directory):
        os.mkdir(video_ts_directory)
    os.chdir(video_ts_directory)
    subprocess.run("ffmpeg -i {} -profile:v baseline -level 3.0 -s 640x360 "
                   "-start_number 0 -hls_time 10 -hls_list_size 0 -f hls index.m3u8"
                   .format(video_path ) ,shell=True)


if __name__ == '__main__':
    make_ts(sys.argv[1])