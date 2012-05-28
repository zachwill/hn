"""
Install the package and script.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="hn",
    version="0.1",
    description="A CLI and Python library for using the HNSearch API.",
    keywords="hn, ycombinator, hacker news, newsyc",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="https://github.com/zachwill/hn",
    license="MIT",
    packages=[
        "yc"
    ],
    scripts=[
        "hn"
    ],
    install_requires=[
        "pygments",
        "requests",
        "simplejson"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite="test.py",
    tests_require=[
        "mock"
    ]
)
