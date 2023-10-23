from setuptools import setup, find_packages

requires = [
    'python-telegram-bot'
]

setup(
    name='queue_bot',
    version='0.1',
    description='telegram bot to manage queue',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='atronah',
    author_email='atronah.ds@gmail.com',
    keywords='python telegram bot queue',
    
    # manual specifying package which is in folder with different name
    packages=['queue_bot'] + find_packages(),
    install_requires=requires,
)