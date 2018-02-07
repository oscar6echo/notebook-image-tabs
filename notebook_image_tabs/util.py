
import os
import base64
import requests as rq


def is_path_img(path):
    """
    """
    filename = os.path.basename(path)
    s = filename.split('.')
    if len(s) > 1:
        ext = s[-1]
        if ext in ['png', 'gif', 'jpg', 'jpeg']:
            return True
    return False


def load_img(str_img):
    """
    """
    str_b64 = None

    if os.path.exists(str_img) and is_path_img(str_img):
        with open(str_img, 'rb') as f:
            content = f.read()
            content_b64 = base64.b64encode(content)
            str_b64 = content_b64.decode('utf-8')

    elif str_img.startswith('http'):
        res = rq.get(str_img)
        if res.status_code == 200:
            content_b64 = base64.b64encode(res.content)
            str_b64 = content_b64.decode('utf-8')

    elif isinstance(str_img, bytes):
        str_img = str_img

    return str_b64
