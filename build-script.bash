#!/bin/bash
CFLAGS="-I/Users/nickesterer/Documents/development/Gamera/include" sudo python \
setup.py build && sudo python setup.py install && sudo python setup.py install_scripts;
exit 0