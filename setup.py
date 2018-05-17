from setuptools import find_packages, setup

setup(
    name='tictactoe',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'ttt = tictactoe.__main__:main'
        ]
    },
)
