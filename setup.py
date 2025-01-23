from setuptools import setup, find_packages

setup(
    name="chat",
    version="0.1.0",
    packages=find_packages(include=["backend", "libs"]),
    install_requires=[
        "chainlit",
        "fastapi",
        "uvicorn"
    ]
)
