from setuptools import setup, find_packages

setup(
    name='changelog_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pulsar-client>=2.0.0',
        'langchain>=0.3.0',
        'datetime',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'changelog=changelog_generator:generate_changelog'
        ]
    },
    author='Shirley Kane',
    author_email='shirley@example.com',
    description='A changelog generator for microservices and LangChain/Pulsar projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shirleykane/changelog-generator',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)