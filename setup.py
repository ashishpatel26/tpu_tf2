from setuptools import setup, find_packages
import os

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

# Setting up
setup(
    name="tpu_tf2",
    version="1.0",
    author="ashishpatel26",
    author_email="ashishpatel.ce.2011@gmail.com",
    description="TPU use in single line in colab.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['tensorflow-cpu==2.7.0', 'tensorflow-gpu==2.7.0'],
    keywords=['tpu_tf2','tpu', 'colab tpu', 'tpu_tf2', 'TPU', 'tpu use in single line in colab'],
    url='https://github.com/ashishpatel26/tpu_tf2',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)