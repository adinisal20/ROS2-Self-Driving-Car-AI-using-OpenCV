from .colour_segmentation import segment_lanes
from ...config.config import minArea_resized
from ...config.config import CropHeight_resized






def detect_lanes(img):
        #cropping the roi (eg keeping omly below the horizons)
        img_cropped = img[CropHeight_resized:,:]

        segment_lanes(img_cropped, minArea_resized)
        