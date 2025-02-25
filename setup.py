#!/usr/bin/env python3
"""
Setup for the homeassistant-component-snmp package.

Author: Troy Kelly (troy@troykelly.com)
Date: 25 February 2025
"""

from setuptools import setup, find_packages

setup(
    name="homeassistant-component-snmp",
    version="0.1.0",
    description="A SNMP component for Home Assistant",
    packages=find_packages(),
    # If you decide to keep your files where they are, you'll need to let Python know how your
    # package maps to the filesystem. For example, if you create an empty homeassistant/__init__.py
    # that imports from your components folder, your package_dir might be just the repository root:
    package_dir={"homeassistant": "."},
    install_requires=[
        "pysnmp",
        "homeassistant",
        "voluptuous",
    ],
    python_requires=">=3.12",
)
