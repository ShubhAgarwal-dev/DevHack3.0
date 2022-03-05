from datetime import datetime
from time import mktime
from hashlib import sha256
import json


class ImageBlockChain():

    def __init__(self, image, key):
        self.image_path = image
        