from setuptools import setup, find_packages

setup(
    name="pyasm",
    version="0.0.1",
    author="Martmists",
    author_email="martmists@gmail.com",
    description="A low-level library for manipulating Python Bytecode in an easy way.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License"
    ],
    packages=["asm", "asm.ops"],
    python_requires=">=3.5",
)
