from setuptools import setup, find_namespace_packages


setup(
    name='GTTD',
    version='0.1.7',
    description='Console bot organizer',
    url='https://github.com/C-Hurtmann/Going_to_the_Dream',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['inquirer', 'colorama'],
    entry_points={'console_scripts': ['helper = bot.interface:main']}
)

