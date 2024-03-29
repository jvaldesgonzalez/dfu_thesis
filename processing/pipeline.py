from processing.color.pipeline import pipeline as color_pipeline
from processing.depth.pipeline import pipeline as depth_pipeline


def pipeline(rgb_img, depth_frame):
    rgb_img_processed = color_pipeline(rgb_img)
    depth_frame_processed = depth_pipeline(depth_frame)

    return rgb_img_processed, depth_frame_processed
