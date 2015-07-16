#!/usr/bin/env python2.7
import nosescript
import setuptools


setuptools.setup(
    name='nosescript',
    version=nosescript.__version__,
    description="A Nose plugin for JavaScript tests.",
    zip_safe=False,
    packages=setuptools.find_packages(exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests",
    ]),
    include_package_data=True,
    install_requires=[
        'nose',
        'python-spidermonkey',
    ],
    setup_requires=[
        'nose-cov>=1.6',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'nosescriptunit = nosescript.unit:NoseScriptUnit'
        ]
    }
)
