# -*- coding: utf-8 -*-

from setuptools import setup

project = "aminer"

setup(
    name=project,
    version='0.1',
    url='https://aminer.yutao.us',
    description='AMiner Core',
    author='Yutao Zhang',
    author_email='stack@live.cn',
    packages=["aminer"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Cors',
        'nose',
        "stemming",
        'xpinyin',
        'pymongo',
        'jellyfish',
        'rq'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
