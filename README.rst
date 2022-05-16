=====================
sphinx-jinja2-compat
=====================

.. start short_desc

**Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions.**

.. end short_desc

Also makes some Sphinx versions work correctly on Python 3.10.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/workflows/Linux/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/workflows/Windows/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/workflows/macOS/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/workflows/Flake8/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/workflows/mypy/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.herokuapp.com/github/sphinx-toolbox/sphinx-jinja2-compat/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/sphinx-toolbox/sphinx-jinja2-compat/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sphinx-toolbox/sphinx-jinja2-compat?logo=codefactor
	:target: https://www.codefactor.io/repository/github/sphinx-toolbox/sphinx-jinja2-compat
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/sphinx-jinja2-compat
	:target: https://pypi.org/project/sphinx-jinja2-compat/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sphinx-jinja2-compat?logo=python&logoColor=white
	:target: https://pypi.org/project/sphinx-jinja2-compat/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sphinx-jinja2-compat
	:target: https://pypi.org/project/sphinx-jinja2-compat/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/sphinx-jinja2-compat
	:target: https://pypi.org/project/sphinx-jinja2-compat/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/sphinx-jinja2-compat?logo=anaconda
	:target: https://anaconda.org/domdfcoding/sphinx-jinja2-compat
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/sphinx-jinja2-compat?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/sphinx-jinja2-compat
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/sphinx-jinja2-compat
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/sphinx-jinja2-compat
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/sphinx-jinja2-compat/v0.2.0b1
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/sphinx-jinja2-compat
	:target: https://github.com/sphinx-toolbox/sphinx-jinja2-compat/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2022
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/sphinx-jinja2-compat
	:target: https://pypi.org/project/sphinx-jinja2-compat/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``sphinx-jinja2-compat`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install sphinx-jinja2-compat

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install sphinx-jinja2-compat

.. end installation
