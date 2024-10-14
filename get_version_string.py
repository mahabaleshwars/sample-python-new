import sys
import os

# Add the _vendor directory to sys.path
vendor_path = os.path.join(os.path.dirname(__file__), 'setuptools', '_vendor')
if vendor_path not in sys.path:
    sys.path.append(vendor_path)

from packaging import version

print("Hello world")
