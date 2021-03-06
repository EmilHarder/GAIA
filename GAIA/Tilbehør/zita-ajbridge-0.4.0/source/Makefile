# ----------------------------------------------------------------------------
#
#  Copyright (C) 2012 Fons Adriaensen <fons@linuxaudio.org>
#    
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------


PREFIX = /usr/local
SUFFIX := $(shell uname -m | sed -e 's/^unknown/$//' -e 's/^i.86/$//' -e 's/^x86_64/$/64/')
VERSION = 0.4.0
BINDIR = $(PREFIX)/bin
LIBDIR = lib$(SUFFIX)
LDFLAGS += -L$(PREFIX)/$(LIBDIR)
CPPFLAGS += -DVERSION=\"$(VERSION)\"
CXXFLAGS += -O2 -Wall -MMD -MP


all:	zita-a2j zita-j2a


ZITA-A2J_O = zita-a2j.o alsathread.o jackclient.o pxthread.o lfqueue.o
$(ZITA-A2J_O):
-include $(ZITA-A2J_O:%.o=%.d)
zita-a2j:	CPPFLAGS += -DAPPNAME=\"zita-a2j\"
zita-a2j:	LDLIBS += -lzita-resampler -lzita-alsa-pcmi -ljack -lasound -lpthread -lm -lrt
zita-a2j:	$(ZITA-A2J_O)
	g++ $(LDFLAGS) -o $@ $(ZITA-A2J_O) $(LDLIBS)


ZITA-J2A_O = zita-j2a.o alsathread.o jackclient.o pxthread.o lfqueue.o
$(ZITA-J2A_O):
-include $(ZITA-J2A_O:%.o=%.d)
zita-j2a:	CPPFLAGS += -DAPPNAME=\"zita-j2a\"
zita-j2a:	LDLIBS += -lzita-resampler -lzita-alsa-pcmi -ljack -lasound -lpthread -lm -lrt
zita-j2a:	$(ZITA-J2A_O)
	g++ $(LDFLAGS) -o $@ $(ZITA-J2A_O) $(LDLIBS)


install:	all
	install -d $(DESTDIR)$(BINDIR)
	install -m 755 zita-a2j $(DESTDIR)$(BINDIR)
	install -m 755 zita-j2a $(DESTDIR)$(BINDIR)


uninstall:
	/bin/rm -f  $(DESTDIR)$(BINDIR)/zita-a2j
	/bin/rm -f  $(DESTDIR)$(BINDIR)/zita-j2a


clean:
	/bin/rm -f *~ *.o *.a *.d *.so
	/bin/rm -f zita-a2j zita-j2a

