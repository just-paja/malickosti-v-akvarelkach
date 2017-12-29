from PIL import Image, ImageEnhance
from django.conf import settings


class Watermark:
    def __init__(self, source, opacity=0.5):
        self.source = source
        self.opacity = opacity

    def get_source_path(self):
        return '%s/%s' % (settings.BASE_DIR, self.source)

    def reduce_opacity(self, im, opacity):
        """Returns an image with reduced opacity."""
        assert opacity >= 0 and opacity <= 1
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        else:
            im = im.copy()
        alpha = im.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        im.putalpha(alpha)
        return im

    def process(self, image):
        overlay = self.reduce_opacity(Image.open(self.get_source_path()), self.opacity)
        ratio = min(
            float(image.size[0]) / overlay.size[0] / 1.5,
            float(image.size[1]) / overlay.size[1] / 1.5,
        )
        w = int(overlay.size[0] * ratio)
        h = int(overlay.size[1] * ratio)
        overlay = overlay.resize((w, h), Image.ANTIALIAS)
        image.paste(overlay, (
            int((image.size[0] - w) / 2),
            int((image.size[1] - h) / 2),
        ), overlay)
        return image
