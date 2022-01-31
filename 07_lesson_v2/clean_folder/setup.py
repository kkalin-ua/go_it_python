from setuptools import setup, find_packages

"""
setup(name='useful',
      version='1',
      description='some code',
      url='https://github.com/kkalin-ua',
      author='Kkalin_ua',
      author_email='kkalin@ukr.net',
      license='MIT',
      packages = find_packages(),
      description = "Clean folder script"
      entry_points = {'console_scripts': ['clean_folder = clean_folder:clean:main']}

)"""


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='useful',
    version="0.0.1",
    author="kkalin_ua",
    author_email="kkalin@ukr.net",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.comkkalin-ua/go_it_python",
    project_urls={
        "Bug Tracker": "https://github.com/kkalin-ua/go_it_python",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "clean_folder"},
    packages=setuptools.find_packages(where="clean_folder"),
    python_requires=">=3.6",
)
