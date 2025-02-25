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
    packages=find_packages(include=["homeassistant", "homeassistant.*"]),
    package_dir={"homeassistant": "homeassistant"},
    install_requires=[
        "pysnmp",
        "homeassistant",
        "voluptuous",
    ],
    python_requires=">=3.12",
)
