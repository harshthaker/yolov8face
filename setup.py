from setuptools import setup, find_packages

setup(
    name='yolov8face',
    version='0.0.1',
    description='A wrapper to YOLOv8 face detector.',
    packages=find_packages(),
    install_requires=[
        'ultralytics',
        'jupyter',
    ],
)