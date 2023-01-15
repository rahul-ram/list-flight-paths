from setuptools import setup

setup(
    name="list-flight-paths",
    version='0.1',
    py_modules=['flight_paths'],
    install_requires=[
        'Click',
    ],
    test_suite='tests',
    entry_points='''
        [console_scripts]
        list-flight-paths=flight_paths:cli
    ''',
)
