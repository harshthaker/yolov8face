# YOLOv8Face

YOLOv8Face is a lightweight Python wrapper around Ultralytics' face detection model. The package automatically downloads the pretrained `yolov8n-face.pt` model and exposes a simple function for retrieving bounding boxes.

## Features

- Automatically downloads the YOLOv8 face model on first use
- Provides a minimal API to obtain face bounding boxes
- Compatible with any image supported by Ultralytics

## Installation

```bash
pip install yolov8face
```

## Quick Start

```python
from yolov8face import get_bbox

bboxes = get_bbox("path/to/image.jpg")
```

## Command Line Interface

After installing the package you can run face detection directly from the
command line:

```bash
yolov8face path/to/image.jpg
```

The command prints the detected bounding boxes to the terminal.

## Example

![Detected faces](https://raw.githubusercontent.com/harshthaker/yolov8face/main/detected_faces.png)

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

Please note that YOLOv8 itself is also released under the GPL-3.0. For commercial use, contact the Ultralytics team to obtain an enterprise license.

## Credits

Developed by [Harsh Thaker](https://github.com/harshthaker).

Special thanks to:
- [akanametov](https://github.com/akanametov/yolov8-face) for providing the pretrained [yolov8n-face](https://github.com/akanametov/yolov8-face/releases/download/v0.0.0/yolov8n-face.pt) model.
- The [Ultralytics](https://github.com/ultralytics/ultralytics) team for the YOLOv8 implementation.

This project stands on the shoulders of the open-source community.
