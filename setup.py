from setuptools import setup

setup(
    name="auto-ambient",
    version="0.3.1",
    packages=["ambient", "ambient.tolls", "ambient.models", "src"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "getFile=ambient.getFile:main",
            "createTagsFile=ambient.createTagsFile:main",
            "createAmbient=ambient.createAutoAmbient:main",
        ],
    },
    install_requires=[
        "PySimpleGUI==4.20.0",
        "botcity==1.8.1",
        "requests>=2.25.1"
    ],
    license='MIT',
)
