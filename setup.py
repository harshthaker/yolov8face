from setuptools import setup, find_packages
import os

setup(
    name='yolov8face',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'ultralytics'
    ],
    description=(
        'Yolov8face is a Python wrapper of Ultrlytics that simplifies the '
        'process of detecting faces in images using the yolov8n-face model. '
        'It takes care of model downloading, loading and postprocessing, '
        'allowing you to detect faces in images with just a few lines of '
        'code.'
    ),
    include_package_data=True,  # Include additional files like README, LICENSE, etc.
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'yolov8face=yolov8face.cli:main',
        ]
    },
)