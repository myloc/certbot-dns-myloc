import os
import sys
from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__))), 'VERSION')) as version_file:
    version = version_file.read().strip()

install_requires = [
    'certbot>=2.0.0',
    'setuptools',
    'httpx'
]

setup(
    name='certbot-dns-myloc',
    version=version,
    description='myLoc DNS Authenticator plugin for Certbot',
    url='https://github.com/myloc/certbot-dns-myloc',
    author='myLoc managed IT AG',
    author_email='opensource@myloc.dev',
    license='Apache License 2.0',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-myloc = certbot_dns_myloc.dns_myloc:Authenticator',
        ],
    },
)
