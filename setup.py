from setuptools import setup

setup(
    name="chat",
    version="0.1.0",
    packages=["backend"],
    install_requires=[
        "chainlit",
        "fastapi",
        "uvicorn"
    ],
    exclude=["frontend", "cypress", "images", "node_modules"]
)
