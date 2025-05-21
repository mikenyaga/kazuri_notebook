from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kazuri",
    version="0.1.0",
    author="Hillary Murefu",
    author_email="hillarywang2005@gmail.com",
    description="A self-hosted AI code assistant for Jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hillaryhitch/kazuri_notebook.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "boto3>=1.17.0",
        "requests>=2.25.0",
        "ipython>=7.0.0",
        "python-dotenv>=0.15.0",
    ],
)
