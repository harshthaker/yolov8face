# yolov8face
Yolov8face is a Python wrapper of Ultrlytics that simplifies the process of detecting faces in images using the yolov8n-face model. It takes care of pre-trained model downloading, loading and postprocessing, allowing you to detect faces in images with just a few lines of code. 

## Installation
```bash
pip install yolov8face
```
## Usage
```python
from yolov8face import get_bbox
bboxes = get_bbox('path-to-image/image.jpg')
```
## Example
![can't load example image](https://raw.githubusercontent.com/harshthaker/yolov8face/main/detected_faces.png)


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

Please note that this project uses the YOLOv8 model from the Ultralytics team, which is also licensed under the GPL-3.0 License. For commercial uses, please contact the Ultralytics team for an Enterprise License.

## Credits

This package was developed by [Harsh Thaker](https://github.com/harshthaker).

Special thanks to:

- [akanametov](https://github.com/akanametov/yolov8-face) for the [yolov8n-face](https://github.com/akanametov/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt) model.
- The [Ultralytics](https://github.com/ultralytics/ultralytics) team for providing the YOLOv8.

This project stands on the shoulders of the open-source community. It wouldn't be possible without the numerous open source projects we've utilised. 



