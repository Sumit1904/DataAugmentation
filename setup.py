from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'This package is for Data augmentation of image dataset'
LONG_DESCRIPTION = 'It is a model for augmentation of image dataset. Augmentation of image is carried out by the process' \
                   ' of resize, scale, rotate, translation, transpose, blurring, and by adding noise to the image. ' \
                   'Dataset(X_train) can be augmented to 10x of its original size while saving y_train data for each image.'

# Setting up
setup(
    name="dataaugmentation",
    version=VERSION,
    author="Sumit Singh",
    author_email="<iamsumit1904@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'os', 'numpy', 'matplotlib.pyplot'],
    keywords=['python', 'augmentation', 'image', 'data augmentation', 'image dataset'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
