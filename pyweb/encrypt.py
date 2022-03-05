import os


class EncryptImage():

    def __init__(self, image_path: str, key: str):
        self.image_path = image_path
        self.image_name = self.get_image_name(self.image_path)
        self.key = key
        self.encrypt()

    @staticmethod
    def get_image_name(path):
        path = os.path.normpath(path).split(os.path.sep)
        return path[-1]

    def encrypt(self):
        try:
            with open(self.image_path, mode='rb') as file:
                img = bytearray(file.read())
                for i, values in enumerate(img):
                    img[i] = values ^ self.key
                with open(self.image_path, mode='wb') as file2:
                    file2.write(img)

        except Exception:
            print('error caught', Exception.__name__)


class DecryptImage():

    def __init__(self, image_path: str, key: str) -> None:
        self.image_path = image_path
        self.key = key
        self.decrypt()

    def decrypt(self) -> None:
        try:
            with open(self.image_path, mode='rb') as file:
                img = bytearray(file.read())
                for i, val in enumerate(img):
                    img[i] = val ^ self.key
                with open(self.image_path, mode='wb') as file2:
                    file2.write(img)
        except Exception:
            print('error caught', Exception.__name__)


if __name__ == '__main__':
    enc1 = EncryptImage('img1.jpg', 12)
    enc2 = EncryptImage('img2.jpg', 13)
    denc1 = DecryptImage('img1.jpg', 12)
    denc2 = DecryptImage('img2.jpg', 13)
