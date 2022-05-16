# stdlib
import sys

# 3rd party
# Test markupsafe
import markupsafe

assert hasattr(markupsafe, "soft_unicode")

# Test jinja2

# 3rd party
import jinja2.filters
import jinja2.utils

assert hasattr(jinja2, "environmentfilter")
assert hasattr(jinja2.filters, "environmentfilter")

assert hasattr(jinja2, "contextfunction")
assert hasattr(jinja2.utils, "contextfunction")

# stdlib
# test typing
import types

if sys.version_info >= (3, 10):
	# stdlib
	assert hasattr(types, "Union")
	assert types.Union is types.UnionType
