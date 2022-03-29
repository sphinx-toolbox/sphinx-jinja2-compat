#!/usr/bin/env python3
#
#  __init__.py
"""
Patches Jinja2 v3 to restore compatibility with earlier Sphinx versions.
"""
#
#  Copyright © 2022 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
from typing import Any, Callable, List, TypeVar

__all__: List[str] = []

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2022 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

F = TypeVar('F', bound=Callable[..., Any])

# 3rd party
import markupsafe  # noqa: E402

if not hasattr(markupsafe, "soft_unicode"):

	def soft_unicode(s: Any) -> str:
		return markupsafe.soft_str(s)

	markupsafe.soft_unicode = soft_unicode  # type: ignore[attr-defined]

# 3rd party
import jinja2  # noqa: E402
import jinja2.filters  # noqa: E402
import jinja2.utils  # noqa: E402

if not hasattr(jinja2.filters, "environmentfilter"):

	def environmentfilter(f: F) -> F:
		return jinja2.utils.pass_environment(f)

	jinja2.filters.environmentfilter = environmentfilter  # type: ignore[attr-defined]
	jinja2.environmentfilter = environmentfilter  # type: ignore[attr-defined]

if not hasattr(jinja2.utils, "contextfunction"):

	def contextfunction(f: F) -> F:
		return jinja2.utils.pass_context(f)

	jinja2.utils.contextfunction = contextfunction  # type: ignore[attr-defined]
	jinja2.contextfunction = contextfunction  # type: ignore[attr-defined]
