import sys
sys.path.pop(0)
from setuptools import setup
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mpu9250",
    py_modules=["mpu9250", "mpu6500", "ak8963"],
    version="0.2.1",
    description="Python I2C driver for MPU9250 9-axis motion tracking device (from Mike Tuupolas work https://github.com/tuupola/micropython-mpu9205)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="accelerometer, gyro, magnetometer, micropython, i2c",
    url="https://github.com/njoc/mpu9250",
    author="Nick OConnor",
    author_email="nickorocks79@gmail.com",
    maintainer="Nick OConnor",
    maintainer_email="nickorocks79@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
