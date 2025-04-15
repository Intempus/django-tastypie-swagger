#!/usr/bin/env python

from setuptools import setup
import tastypie_swagger

description = "An adapter to use swagger-ui with django-tastypie"

try:
    longdesc = open('README.rst').read()
except Exception:
    longdesc = description

setup(
    # Metadata
    name='django-tastypie-swagger',
    version='.'.join(map(str, tastypie_swagger.VERSION)),
    description=description,
    long_description=longdesc,
    author='Intempus Aps',
    author_email='info@intempus.com',
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    url='https://github.com/Intempus/django-tastypie-swagger.git',
    download_url='https://github.com/Intempus/django-tastypie-swagger.git',
    license='BSD',
    packages=['tastypie_swagger'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>4,<6',
        'django-tastypie>=0.14.7',
        'swagger_spec_validator',  # https://github.com/Yelp/swagger_spec_validator
        'typing_extensions',
    ],
)
