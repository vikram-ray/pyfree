import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfree", 
    version="1.0.0",
    author="Vikram Ray",
    author_email="vik8876@gmail.com",
    description="A lib for free APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rayvikram/pyfree",
    # packages=setuptools.find_packages(),
    packages=["pyfree"],

    # this is used to include files that are defined in MANIFEST.in
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_script": [
            "pyfree=pyfree.__main__:main"
        ]
    },
    install_requires = [
        "requests",
    ],
    python_requires='>=3.6',
)