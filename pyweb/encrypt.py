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
        try:
            with open(self.image_path, mode='rb') as file:
                img = bytearray(file)
                for i, values in enumerate(img):
                    img[i] = values ^ self.key

                with open(destination, mode='wb') as file:
                    destination = destination+self.image_name
                    file.write(destination)

        except Exception:
            print('error caught', Exception.__name__)

    @staticmethod
    def decrypt(image_path):
        pass


if __name__ == '__main__':
    enc1 = EncryptImage('img1.jpg', 12)
    enc2 = EncryptImage('wallpaper.jpg', 13)
