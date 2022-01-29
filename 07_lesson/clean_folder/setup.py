from setuptools import setup

setup(name='useful',
      version='1',
      description='some code',
      url='https://github.com/kkalin-ua',
      author='Kkalin_ua',
      author_email='kkalin@ukr.net',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['markdown'],
      entry_points={'console_scripts': ['clean_folder = useful.clean:clean_folder']}
)

