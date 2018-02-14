from setuptools import find_packages, setup

VERSION = "1.0.0"
LONG_DESCRIPTION = """

======
Formly
======

.. image:: https://img.shields.io/pypi/v/formly.svg
    :target: https://pypi.python.org/pypi/formly/

\ 

.. image:: https://img.shields.io/circleci/project/github/eldarion/formly.svg
    :target: https://circleci.com/gh/eldarion/formly
.. image:: https://img.shields.io/codecov/c/github/eldarion/formly.svg
    :target: https://codecov.io/gh/eldarion/formly
.. image:: https://img.shields.io/github/contributors/eldarion/formly.svg
    :target: https://github.com/eldarion/formly/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/eldarion/formly.svg
    :target: https://github.com/eldarion/formly/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/eldarion/formly.svg
    :target: https://github.com/eldarion/formly/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: https://img.shields.io/badge/license-BSD-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause

\ 

``formly`` is a forms/survey generator for dynamically constructor multi-page surveys that have the ability to be non-linear.


Development sponsored by `Midwest Communications`_ and `Massachusetts General Hospital`_.


Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+


.. _Midwest Communications: http://mwcradio.com/
.. _Massachusetts General Hospital: http://www.massgeneral.org/
"""

setup(
    author="Patrick Altman",
    author_email="paltman@eldarion.com",
    description="A forms/survey generator for dynamically constructor multi-page surveys",
    name="formly",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/eldarion/formly/",
    license="BSD",
    packages=find_packages(),
    package_data={
        "formly": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "jsonfield>=2.0.2",
        "django-appconf>=1.0.2",
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
