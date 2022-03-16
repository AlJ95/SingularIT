from setuptools import setup, find_packages


setup(
    name='singular_it_Albrecht',
    version='0.1.0',
    packages=find_packages(include=['singular_it', 'singular_it,*']),
    install_requires=[
        "numpy"
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)