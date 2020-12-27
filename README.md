# pyfree

- A simple package to get data from OPEN APIs for your test projects or exp projects. No need to remember the URLS.


# Functions
- `from pyfree import FreeAPI` 
- `FreeAPI.get_bank_details('SBIN0012345')` - to get bank details

# How to create a PyPi package and Host it on pyPi server
- READ kro yeh - https://packaging.python.org/tutorials/packaging-projects/ 
1. create a package with all the modules inside it. 
2. create LICENSE, README.md, setup.py, etc (with content from above URL or from my repo)
3. Generating distribution archives - `python setup.py sdist bdist_wheel` - will create 2 files(`source archive` and `wheels`
) inside dist/. These are the file that will be pushed to the server
4. create a acount for TestPYPI - `https://test.pypi.org/account/register/`
5. Upload to test-PYpi using twine. (install twine if not installed) .  `OPTIONAL - twine check dist/*` and `twine upload --repository testpypi dist/*`
6. It should be uploaded and follow the steps that you see after upload to test or install your package in local.
7. You have successfully installed and uploaded package to TestPypi. Follow the same steps for `https://pypi.org/account/register/`


# notes
- A common way to distribute is to - `source archive` and `wheels`
# files
- `setup.py` - setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include
- `setup.cfg` - a configuration for `setup.py`. More at - https://stackoverflow.com/questions/39484863/whats-the-difference-between-setup-py-and-setup-cfg-in-python-projects and https://docs.python.org/3/distutils/configfile.html
- `.pypirc` - A .pypirc file allows you to define the configuration for package indexes (referred to here as “repositories”), so that you don’t have to enter the URL, username, or password whenever you upload a package with twine or flit. - https://packaging.python.org/specifications/pypirc/. (we place it in ~/.pypirc) (after adding it i just had to do twine upload and it take token and other credential from HOME/.pyprc file)
- `MANIFEST.in` - a file where we list all the extra file that needs to be included 
- `__main__.py` and `entrypoint` in setup.py - It enables excution of the __main__ file with the module name directly with `-m` flag. Eg - `python -m pyfree` will execute content of `main` inside `__main__.py` file

## setuptools
- setuptools (which includes easy_install) is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages.

## Twine
- Twine is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes. It is a command-line program that passes program files and metadata to a web API. Developers use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.

## wheel
- Primarily, the wheel project offers the bdist_wheel setuptools extension for creating wheel distributions. Additionally, it offers its own command line utility for creating and installing wheels.