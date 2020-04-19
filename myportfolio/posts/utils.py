import os
import secrets
from PIL import Image
from flask import url_for, current_app

def save_work_picture(form_workpicture):
    picture_fn = os.path.basename(form_workpicture.filename)
    
    picture_path = os.path.join(current_app.root_path, 'static/images/work_imgs', picture_fn)

    i = Image.open(form_workpicture)
    i.save(picture_path)

    return picture_fn

def save_post_picture(form_postpicture):
    picture_fn = os.path.basename(form_postpicture.filename)
    
    picture_path = os.path.join(current_app.root_path, 'static/images/post_imgs', picture_fn)

    i = Image.open(form_postpicture)
    i.save(picture_path)

    return picture_fn

