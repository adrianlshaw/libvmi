# pylint: disable=C0301
"""
PyVMI is a python language wrapper for the LibVMI Library. The LibVMI Library
is an introspection library that simplifies access to memory in a target
virtual machine or in a file containing a dump of a system's physical memory.

Author: Bryan D. Payne (bdpayne@acm.org)

Copyright 2013 Bryan D. Payne

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__copyright__",
]

__title__ = "pyvmi"
__summary__ = "Python binding to LibVMI"
__uri__ = "http://www.libvmi.com"

__version__ = "0.9.0"

__author__ = "Bryan D. Payne"
__email__ = "bdpayne@acm.org"

__copyright__ = "Copyright 2012 Bryan Payne"
