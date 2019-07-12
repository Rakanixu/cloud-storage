import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cloud_storage_client",
    version = "1.0.1",
    author = "Pablo Aguirre",
    author_email = "paguirrerubio@gmail.com",
    license = "MIT",
    url = "http://packages.python.org/cloud_storage_client",
    packages=['cloud_storage_client'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=[
        'botocore==1.11.4',
        'boto3==1.8.4',
        'google.cloud==0.32.0',
        'azure==3.0.0',
        'pysftp==0.2.9'
    ],
)