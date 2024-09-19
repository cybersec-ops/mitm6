from setuptools import setup
import sys

# Python 3 requirements
if sys.version_info[0] == 2:
    reqs = ["scapy>=2.4", "ipaddress", "future", "twisted", "netifaces"]
else:
    reqs = ["scapy>=2.5", "twisted", "netifaces"]

setup(name='mitm6',
      version='1.0.0',
      description='Pwning IPv4 via IPv6',
      license='GPLv2',
      classifiers=[
        'Intended Audience :: Information Technology',
        'Framework :: Twisted',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
      ],
      author='Steven Leong',
      author_email='dirkjan.mollema@fox-it.com',
      url='https://github.com/cybersec-ops/mitm6/',
      packages=['mitm6'],
      install_requires=reqs,
      entry_points= {
        'console_scripts': ['mitm6=mitm6.mitm6:main']
      }
     )