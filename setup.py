#!/usr/bin/env python

from distutils.core import setup

kwargs = {
    "name": "pagerdutyduty",
    "version": "0.4",
    "scripts": ["bin/pagerdutyduty"],
    "description": "Set PagerDuty schedules with SMART COMPUTERS and YAML",
    "author": "Jeff Zellner",
    "maintainer": "Jeff Zellner",
    "author_email": "jeff@olark.com",
    "maintainer_email": "jeff@olark.com",
    "url": "https://github.com/olark/pagerdutyduty",
    "install_requires": ['pygerduty>=0.16', 'PyYAML>=3.10'],
}

setup(**kwargs)
