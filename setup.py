from setuptools import setup, find_packages

setup(
    name='bingo_game',                   # Package name
    version='1.0.0',                     # Version
    packages=find_packages(),            # Automatically find modules
    install_requires=[
        'colorama>=0.4.6'                # Dependency
    ],
    entry_points={
        'console_scripts': [
            'bingo-game=bingo_game.game:main'  # CLI command -> function to run
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple Bingo game to play in the terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AromalShaji/python-bingo',  # GitHub or project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',             # Minimum Python version
)
