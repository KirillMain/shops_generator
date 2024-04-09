import random

from moviepy.editor import *


def video_gen(count: int, duration: int = 4):
    time = 6
    src_clip = f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\back_res.png"
    clip = ImageClip(src_clip).set_duration(5)

    arr = [clip]
    for i in range(0, count):
        time += duration
        src = f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\res{i}.png"
        clip = ImageClip(src).set_duration(duration)
        arr.append(clip)

    final_clip = concatenate_videoclips(arr, method="compose")

    num = random.randint(0,5)
    src_audio = f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\music\\track{num}.mp3"
    audio_clip = AudioFileClip(src_audio)
    final_clip = final_clip.set_audio(audio_clip)
    final_clip = final_clip.set_duration(time)

    final_clip.write_videofile(f"C:\\Users\\kiril\\Documents\\GitHub\\wb_parser\\data\\tt_post\\movie.mp4", fps=24)