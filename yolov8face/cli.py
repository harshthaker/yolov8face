import argparse
from .yolo_model import get_bbox


def main():
    parser = argparse.ArgumentParser(description="Detect faces in an image using YOLOv8")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    bboxes = get_bbox(args.image)
    if bboxes is None:
        print("Face detection failed.")
    else:
        print(bboxes)


if __name__ == "__main__":
    main()
