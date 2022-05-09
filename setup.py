# -*- coding: utf-8 -*-
"""A setup module for the dictmatch Python package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob

from distutils.core import setup

LONGDOC = """
dictmatch
*********
dictmatch：词典匹配工具
完整文档见 ``README.md``
GitHub: https://github.com/Bond-H/dictmatch

安装说明
*********
代码对 Python 2/3 均兼容
- pip安装：`pip install dictmatch`
- clone安装：先clone本代码库，然后运行 `python setup.py install`
- 手动安装：将 dictmatch 目录放置于当前目录或者 site-packages 目录，通过 `import dictmatch` 来引用
"""

_PACKAGES = (
        "dictmatch",
)

_PACKAGES_DIRECTORIES = { 
        'dictmatch' : 'dictmatch', 
        #'dictmatch.chdir' : 'dictmatch.chdir', 
}
setup(
        name='dictmatch', version='0.1.0',
        description='Dict Match Utilities',
        long_description=LONGDOC,
        platforms="any",
        author_email="huangdb3@mail2.sysu.edu.cn",
        url="https://github.com/Bond-H/dictmatch",
        license='Apache 2.0',
        keywords="dict match",
        packages=_PACKAGES,
        package_dir = _PACKAGES_DIRECTORIES,
)

