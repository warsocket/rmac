#!/usr/bin/env python
"""
    Generate a random mac address with various settings (globally unique, broadcast)
    Copyright (C) 2015  Bram Staps

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

#for v1 no options
import random
import sys

def byte2hex(b):
    return chr(b).encode("hex")

l = []
l.append( random.getrandbits(6) * 4 )

for x in xrange(5):
    l.append( random.getrandbits(8) )

sys.stdout.write( ":".join(map(byte2hex, l)) )
