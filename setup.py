from setuptools import setup


setup(
    name='envm',
    version='0.2.3',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'envm = main:envm',
        ],
    },
)
