'''
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex
import gettext
import sys
import string

class EggBotStripData(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	'''Main entry point: check to see which tab is selected, and act accordingly.'''									
	def effect(self):		#Pick main course of action, depending on active GUI tab when "Apply" was pressed.
		self.svg = self.document.getroot()
		inkex.etree.strip_elements(self.svg, inkex.addNS('eggbot','svg'))
		inkex.errormsg(gettext.gettext("Okay, I've removed all Eggbot data from this Inkscape file.  Have a nice day!"))

e = EggBotStripData()
e.affect()
