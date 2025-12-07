from setuptools import setup, find_packages # type: ignore

setup(
    name="dataproc",
    version="0.1.0",
    description="A lightweight text processing library for Chinese NLP tasks",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/327810854/dataproc",
    packages=find_packages(exclude=["tests", "examples"]),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="text processing nlp chinese",
    project_urls={
        "Bug Reports": "https://github.com/327810854/dataproc/issues",
        "Source": "https://github.com/327810854/dataproc",
    },
)
