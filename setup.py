from setuptools import setup

setup(
    name="teste",
    entry_points={
        "console_scripts": [
            "teste=teste.main:main",
        ],
    },
)
