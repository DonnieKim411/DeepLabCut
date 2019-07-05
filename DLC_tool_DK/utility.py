import os
from pathlib import Path
import shutil
import cv2

def key_dict_generater(case):
    case_key = {'animal_id': None, 'session': None, 'scan_idx': None}
    for ind, key in enumerate(case_key.keys()):
        case_key[key] = int(case.split('_')[ind])

    return case_key

def get_frame(path_to_video, frame_num):
    cap = cv2.VideoCapture(path_to_video)
    cap.open(path_to_video)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    _, img = cap.read()
    cap.release()
    return img
