from setuptools import setup, find_packages


def _read_description() -> str:
    """Return the README contents for the long description."""
    with open("README.md", encoding="utf-8") as fh:
        return fh.read()


setup_params = dict(
    name="yolov8face",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["ultralytics"],
    description=(
        "Yolov8face is a Python wrapper of Ultrlytics that simplifies the "
        "process of detecting faces in images using the yolov8n-face model. "
        "It takes care of model downloading, loading and postprocessing, "
        "allowing you to detect faces in images with just a few lines of "
        "code."
    ),
    include_package_data=True,  # Include additional files like README, LICENSE, etc.
    long_description=_read_description(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "yolov8face=yolov8face.cli:main",
        ]
    },
)


if __name__ == "__main__":
    setup(**setup_params)
