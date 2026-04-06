from setuptools import setup, find_packages

setup(
    name='quick-logging',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pulsar-client>=2.8.0',
        'langchain>=0.0.254',
    ],
    author='Shirley Kane',
    author_email='shirley.kane@example.com',
    description='Logging integration module for quick-scripts',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shirleykane/quick-scripts',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)