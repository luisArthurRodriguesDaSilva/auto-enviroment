from setuptools import setup

setup(
    name="auto-ambient",
    version="0.1",
    packages=["ambient", "ambient.tolls"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "getFile=ambient.getFile:main",
            "createTagsFile=ambient.createTagsFile:main",
        ],
    },
)
