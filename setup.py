import uuid

from setuptools import setup, find_packages
from pip.req import parse_requirements

reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

setup(
    name='djangocms_easy_featurette',
    version='0.1.0',
    description='A bootstrap featurette plugin for DjangoCMS',
    long_description=open('README.rst').read(),
    url='https://github.com/something',
    author='Ryan C Murray',
    author_email='murraryan@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    keywords='django django-cms bootstrap featurette',
    packages=find_packages(),
    install_requires=[str(x).split(' ')[0] for x in reqs],
    )
