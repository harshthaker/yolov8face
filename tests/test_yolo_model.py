import sys
import types
from unittest import mock

class DummyRequestException(Exception):
    pass

requests_mod = types.ModuleType('requests')
exceptions_mod = types.ModuleType('requests.exceptions')
exceptions_mod.RequestException = DummyRequestException
requests_mod.get = lambda *a, **k: None
requests_mod.exceptions = exceptions_mod
sys.modules.setdefault('ultralytics', types.ModuleType('ultralytics'))
sys.modules['ultralytics'].YOLO = mock.Mock()
sys.modules.setdefault('requests', requests_mod)
sys.modules.setdefault('requests.exceptions', exceptions_mod)

from yolov8face.yolo_model import get_bbox
from yolov8face.yolo_model import RequestException

class DummyResults:
    def __init__(self, boxes):
        class B:
            def __init__(self, b):
                self.boxes = b
        self.boxes = B(boxes)

def test_get_bbox_uses_existing_model():
    class DummyYOLO:
        def __init__(self, path):
            self.path = path
        def __call__(self, img):
            return [DummyResults([1, 2, 3])]

    with mock.patch('yolov8face.yolo_model.os.path.isfile', return_value=True), \
         mock.patch('yolov8face.yolo_model.YOLO', DummyYOLO):
        bbox = get_bbox('img.jpg')
        assert bbox == [1, 2, 3]


def test_get_bbox_downloads_model(tmp_path):
    class DummyYOLO:
        def __init__(self, path):
            self.path = path
        def __call__(self, img):
            return [DummyResults(['bbox'])]

    with mock.patch('yolov8face.yolo_model.os.path.isfile', return_value=False), \
         mock.patch('yolov8face.yolo_model.requests.get') as mock_get, \
         mock.patch('builtins.open', mock.mock_open()) as m_open, \
         mock.patch('yolov8face.yolo_model.YOLO', DummyYOLO):
        mock_resp = mock.Mock()
        mock_resp.content = b'data'
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp
        bbox = get_bbox('img.jpg')
        assert bbox == ['bbox']
        mock_get.assert_called_once()
        m_open.assert_called_with('yolov8n-face.pt', 'wb')

def test_get_bbox_request_exception():
    with mock.patch('yolov8face.yolo_model.os.path.isfile', return_value=False), \
         mock.patch('yolov8face.yolo_model.requests.get', side_effect=RequestException('fail')):
        assert get_bbox('img.jpg') is None
