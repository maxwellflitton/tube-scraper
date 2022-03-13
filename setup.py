from setuptools import setup, find_packages


setup(
   name='tube-scraper',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/maxwellflitton/tube-scraper",
   description='basic tube status web scrapping tool',
   long_description="basic tube status web scrapping tool",
   package_data={'': ['script.sh']},
   include_package_data=True,
   install_requires=[
       "requests",
       "beautifulsoup4"
   ],
   entry_points={
       "console_scripts": [
       ]
   },
)