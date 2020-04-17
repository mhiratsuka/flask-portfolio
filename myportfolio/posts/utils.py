import os
import secrets
from PIL import Image
from flask import url_for, current_app

def save_work_picture(form_workpicture):
    # print(form_workpicture)
    # random_hex = secrets.token_hex(8)
    # _, f_ext = os.path.splitext(form_workpicture.filename)
    picture_fn = os.path.basename(form_workpicture.filename)
    
    picture_path = os.path.join(current_app.root_path, 'static/images/work_imgs', picture_fn)

    i = Image.open(form_workpicture)
    i.save(picture_path)

    return picture_fn

