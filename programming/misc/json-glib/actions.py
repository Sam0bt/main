#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    options = "-Ddocs=false \
               -Dintrospection=true \
              "
               
    if get.buildTYPE() == "_emul32":
        options += " --prefix='/usr' \
                     --libdir=/usr/lib32 \
                   "
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    
    if get.buildTYPE() == "_emul32":
        #pisitools.removeDir("/_emul32")
        
        #pisitools.removeDir("/usr/share/gtk-doc")

        pisitools.dodoc("README.md", "NEWS")
