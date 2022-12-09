import cv2 
import numpy as np
from ...config.config import debugging_L_ColorSeg

hls = 0
src = 0

#white_regions
hue_l = 0
lit_l = 130
sat_l = 0

#yellow_regions
hue_l_y = 30
hue_h_y = 43
lit_l_y = 0
sat_l_y = 0

def on_hue_low_change(val):
    global hue_l
    hue_l = val
    maskextract()

def on_lit_low_change(val):
    global lit_l
    lit_l = val
    maskextract()

def on_sat_low_change(val):
    global sat_l
    sat_l = val
    maskextract()

def on_hue_low_y_change(val):
    global hue_l_y
    hue_l_y = val
    maskextract()

def on_hue_high_y_change(val):
    global hue_h_y
    hue_h_y = val
    maskextract()

def on_lit_low_y_change(val):
    global lit_l_y
    lit_l_y = val
    maskextract()

def on_sat_low_y_change(val):
    global sat_l_y
    sat_l_y = val
    maskextract()

def maskextract():
    print("hls in maskextract(): {}". format(hls))
    print("src in maskextract(): {}". format(src))
    mask = clr_segment(hls, (hue_l, lit_l, sat_l),(255, 255, 255))
    mask_y = clr_segment(hls, (hue_l_y, lit_l_y, sat_l_y),(hue_h_y, 255, 255))

    mask_y_ = mask_y !=0
    dst_Y = src*(mask_y_[:,:,None].astype(src.dtype))
    
    mask_ = mask !=0
    dst = src*(mask_[:,:,None].astype(src.dtype))
    if (debugging_L_ColorSeg):
        cv2.imshow('white_regions', dst)
        cv2.imshow('yellow_regions', dst_Y) 

if (debugging_L_ColorSeg):
    cv2.namedWindow("white_regions", cv2.WINDOW_NORMAL)
    cv2.namedWindow("yellow_regions", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("Hue_L", "white_regions", hue_l, 255, on_hue_low_change)
    cv2.createTrackbar("Lit_L", "white_regions", lit_l, 255, on_lit_low_change)
    cv2.createTrackbar("Sat_L", "white_regions", sat_l, 255, on_sat_low_change)
    cv2.createTrackbar("Hue_L_Y", "yellow_regions", hue_l_y, 255, on_hue_low_y_change)
    cv2.createTrackbar("Hue_H_Y", "yellow_regions", hue_h_y, 255, on_hue_high_y_change)
    cv2.createTrackbar("Lit_L_Y", "yellow_regions", lit_l_y, 255, on_lit_low_y_change)
    cv2.createTrackbar("Sat_L_Y", "yellow_regions", sat_l_y, 255, on_sat_low_y_change)

def clr_segment(img, lower_range, upper_range): 
    lower = np.array([lower_range[0], lower_range[1], lower_range[2]])
    upper = np.array([upper_range[0], 255, 255])
    print("upper:{}".format(upper))
    print("lower:{}".format(lower))
    mask_in_range = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize = (3,3))
    mask_dilated = cv2.morphologyEx(mask_in_range, cv2.MORPH_DILATE, kernel)
    return mask_dilated

def segment_lanes (frame, min_area):
    global hls, src
    src = frame.copy()
    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    print("hls in segment_lanes: {}". format(hls))
    print("src in segment_lanes: {}". format(src))
    white_regions = clr_segment(hls, np.array([hue_l, lit_l, sat_l]), np.arrray([255, 255, 255]))
    yellow_regions = clr_segment(hls, np.array([hue_l_y, lit_l_y, sat_l_y]), np.array([hue_h_y, 255, 255]))
    cv2.imshow("white_regions", white_regions)
    cv2.imshow("yellow_regions", yellow_regions)

    cv2.waitKey(1)

