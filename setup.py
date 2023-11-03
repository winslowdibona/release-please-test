from setuptools import find_packages, setup

setup(
    name='release-please-test',
    version='0.1.0',
    author='winslowdibona',
    packages=find_packages(exclude=['release-please-test/tests']),
    url='https://github.com/winslowdibona/release-please-test',
    license='LICENSE',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
        "Django == 3.2.22",
    ],
)
