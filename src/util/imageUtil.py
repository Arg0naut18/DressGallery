import base64
from io import BytesIO
from PIL import Image


class ImageUtil:
    @staticmethod
    def image_to_base64(image_path: str, format: str = "JPEG"):
        buffered = BytesIO()
        image = Image.open(image_path)
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue())

    @staticmethod
    def base64_to_image(b64_string: str, format: str = "JPEG"):
        return Image.open(BytesIO(base64.b64decode(b64_string)))
