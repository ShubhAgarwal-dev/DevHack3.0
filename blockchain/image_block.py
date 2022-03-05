from datetime import datetime
from time import mktime
from hashlib import sha256
from json import dumps

from pyweb.encrypt import EncryptImage


class DecryptImage():

    def __init__(self, image, key: int, name: str):
        self.image = image
        self.key = key
        self.name = name
        self.decrypt()

    def decrypt(self):
        image_bytes = bytearray(self.image)
        for i, val in enumerate(image_bytes):
            image_bytes[i] = val ^ self.key
        destination = f'{self.name}+.jpg'
        with open(destination, mode='wb') as file:
            file.write(image_bytes)


class ImageBlockChain():

    def __init__(self, image, key):
        self.first_image_path = image
        self.first_key = key
        self._genesis = self.create_block(proof=1, previous_hash='0')
        self.str_img = self.make_image_string()
        self.chain = []

    def create_block(self, previous_hash, image_data, key):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': mktime(datetime.utcnow().timetuple()),
            'image_data': image_data,
            'key': key,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def encrypt_image(self, image_path, key):
        EncryptImage(image_path, key)

    def image_to_bytes(self, image_path, key):
        self.encrypt_image(image_path, key)
        with open(image_path, mode='rb') as file:
            image_string = file.read()
        return image_string

    def hash_block(self, block):
        encoded_block = dumps(block, sort_keys=True).encode()
        return sha256(encoded_block).hexdigest()

    def add_block(self, image_path, key):
        return self.create_block('proof', self.image_to_bytes(
            image_path, key), key, self.hash_block(self.chain[-1]))

    def decrypt_image(self, index):
        block = self.chain[index-1]
        image = block['image_data']
        key = block['key']
        name = block['index']
        return DecryptImage(image, key, name)


if __name__ == '__main__':
    pass
