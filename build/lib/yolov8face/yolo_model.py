from ultralytics import YOLO
from typing import Union
import os
import requests
from requests.exceptions import RequestException

def get_bbox(image_path: str) -> Union[list, None]:
    """
    Download (if not exist) and load the YOLO model to get bounding boxes for the input image.
    
    The function checks if the model file 'yolov8n-face.pt' exists in the current directory. 
    If not, it downloads the model file from a specific URL and saves it to the current directory. 
    Then, it initializes a YOLO model instance using this file and apply the model on the input image 
    to get the bounding boxes.
    
    Parameters:
    image_path (str): The path of the image to apply face detection.

    Returns:
    List of bounding boxes if successful, None otherwise.
    """
    
    model_path = 'yolov8n-face.pt'
    url = "https://github.com/akanametov/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt"
    
    if not os.path.isfile(model_path):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful.
        except RequestException as err:
            print(f"Requests Error: {err}")
            return None
        else:
            with open(model_path, 'wb') as f:
                f.write(response.content)

    try:
        model = YOLO(model_path)
        results = model(image_path)
        bbox = results[0].boxes.boxes 
    except Exception as err:
        print(f"Model Loading Error: {err}")
        return None
    else:
        return bbox
