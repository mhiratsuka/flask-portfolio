import os
import secrets
from PIL import Image
from flask import url_for, current_app

def save_work_picture(form_workpicture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_workpicture.filename)
    picture_fn = random_hex + f_ext

    picture_path = os.path.join(current_app.root_path, 'static/images/work_imgs', picture_fn)
    i = Image.open(form_workpicture)
    i.save(picture_path)

    return picture_fn

def save_post_picture(form_postpicture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_postpicture.filename)
    picture_fn = random_hex + f_ext

    picture_path = os.path.join(current_app.root_path, 'static/images/post_imgs', picture_fn)
    i = Image.open(form_postpicture)
    i.save(picture_path)

    return picture_fn


def save_post_video(form_video):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_video.filename)
    video_fn = random_hex + f_ext   

    video_path = os.path.join(current_app.root_path, 'static/videos/post_mp4', video_fn)
    form_video.save(video_path)

    return video_fn

