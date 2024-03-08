#   This is a component of LinuxCNC
#   Copyright 2011, 2012, 2013 Dewey Garrett <dgarrett@panix.com>,
#   Michael Haberler <git@mah.priv.at>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
from stdglue import *
import linuxcnc

#   Read the offsets of Pp tool from the tooltable and set it as global #<_read_tool_table_XXXX>
#      If I word is set, the global vars will be initialized and the P word will be ignored
def g101(self, **words):
    try:
        arg = self.blocks[self.remap_level]
        
        # I word causes the memory locations to be initialized
        if arg.i_flag:
            self.execute("#<_read_tool_table_diameter> = 0")
            self.execute("#<_read_tool_table_frontangle> = 0")
            self.execute("#<_read_tool_table_backangle> = 0")
            self.execute("#<_read_tool_table_orientation> = 0")
            self.execute("#<_read_tool_table_xoffset> = 0")
            self.execute("#<_read_tool_table_yoffset> = 0")
            self.execute("#<_read_tool_table_zoffset> = 0")
            self.execute("#<_read_tool_table_aoffset> = 0")
            self.execute("#<_read_tool_table_boffset> = 0")
            self.execute("#<_read_tool_table_coffset> = 0")
            self.execute("#<_read_tool_table_uoffset> = 0")
            self.execute("#<_read_tool_table_voffset> = 0")
            self.execute("#<_read_tool_table_woffset> = 0")
            return INTERP_OK
            
        # P word sets the tool number to read
        if not arg.p_flag:
            self.set_errormsg("G10.1 P word requires a value") 
            return INTERP_ERROR
        p = arg.p_number
        s = linuxcnc.stat()
        s.poll()
        tl = s.tool_table
        # find the pocket number of the selected tool
        result = next((i for i, v in enumerate(tl) if v[0] == p), None)
        if result == None:
            self.set_errormsg("G10.1 Selected tool #<r> not found in tooltable")
            return INTERP_ERROR
        d = s.tool_table[result].diameter
        fa = s.tool_table[result].frontangle
        ba = s.tool_table[result].backangle
        o = s.tool_table[result].orientation
        x = s.tool_table[result].xoffset
        y = s.tool_table[result].yoffset
        z = s.tool_table[result].zoffset
        a = s.tool_table[result].aoffset
        b = s.tool_table[result].boffset
        c = s.tool_table[result].coffset
        u = s.tool_table[result].uoffset
        v = s.tool_table[result].voffset
        w = s.tool_table[result].woffset
        self.execute("#<_read_tool_table_diameter> = " + str(d))
        self.execute("#<_read_tool_table_frontangle> = " + str(fa))
        self.execute("#<_read_tool_table_backangle> = " + str(ba))
        self.execute("#<_read_tool_table_orientation> = " + str(o))
        self.execute("#<_read_tool_table_xoffset> = " + str(x))
        self.execute("#<_read_tool_table_yoffset> = " + str(y))
        self.execute("#<_read_tool_table_zoffset> = " + str(z))
        self.execute("#<_read_tool_table_aoffset> = " + str(a))
        self.execute("#<_read_tool_table_boffset> = " + str(b))
        self.execute("#<_read_tool_table_coffset> = " + str(c))
        self.execute("#<_read_tool_table_uoffset> = " + str(u))
        self.execute("#<_read_tool_table_voffset> = " + str(v))
        self.execute("#<_read_tool_table_woffset> = " + str(w))

        return INTERP_OK

    except Exception as e:
        self.set_errormsg("G10.1 error: %s)" % (e))
        return INTERP_ERROR
        