#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "rustc-%s-src" %get.srcVERSION()
crt_ver = "11.0.0"

def build():
    shelltools.export("LC_ALL", "en_US.UTF-8")
    shelltools.export("RUST_BACKTRACE", "1")
    shelltools.export("RUST_COMPILER_RT_ROOT", "%s/%s/compiler-rt-%s.src" % (get.workDIR(), WorkDir, crt_ver))
    shelltools.system("python ./x.py dist")
    

def install():
    shelltools.system("DESTDIR=%s python ./x.py install" % get.installDIR())
    
    #pisitools.insinto("/", "build/x86_64-unknown-linux-gnu/stage0/etc")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/bin")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/lib")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/share")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/manifest.in")
        
    #pisitools.dodoc("LICENSE","AUTHORS","README*")
