import os


class EncryptImage():

    def __init__(self, image_path: str, key):
        self.image_path = image_path
        self.image_name = self.get_image_name(self.image_path)
        self.key = key
        self.encrypt()

    @staticmethod
    def get_image_name(path):
        path = os.path.normpath(path).split(os.path.sep)
        return path[-1]

    def encrypt(self, destination: str = r'encrypted/'):
        # try:
        with open(self.image_path, mode='rb') as file:
            img = bytearray(file.read())
            for i, values in enumerate(img):
                img[i] = values ^ self.key

            destination = os.path.join(destination, self.image_name)
            cwd = os.getcwd()
            full_dest = os.path.join(cwd, destination)

            if not os.path.isfile(full_dest):
                os.mkdir(full_dest)

            with open(full_dest, mode='wb') as file:
                file.write(img)

        # except Exception:
        #     print('error caught', Exception.__name__)

    @staticmethod
    def decrypt(image_path, key):
        pass


if __name__ == '__main__':
    enc1 = EncryptImage('img1.jpg', 12)
    enc2 = EncryptImage('wallpaper.jpg', 13)
