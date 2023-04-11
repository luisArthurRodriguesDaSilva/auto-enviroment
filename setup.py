from setuptools import setup

setup(
    name="get_file_by_github",
    entry_points={
        "console_scripts": [
            "getFile=getFile.main:main",
        ],
    },
)
