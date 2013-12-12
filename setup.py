#!/usr/bin/env python

from distutils.core import setup

kwargs = {
    "name": "pagerdutyduty",
    "version": "0.3",
    "py_modules": ["pagerdutyduty"],
    "scripts": ["bin/pagerdutyduty"],
    "description": "Set PagerDuty schedules with SMART COMPUTERS and YAML",
    "author": "Jeff Zellner",
    "maintainer": "Jeff Zellner",
    "author_email": "jeff@olark.com",
    "maintainer_email": "jeff@olark.com",
    "url": "https://github.com/olark/pagerdutyduty",
}

setup(**kwargs)
