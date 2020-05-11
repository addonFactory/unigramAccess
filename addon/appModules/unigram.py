#appModules/unigram.py
# Copyright (C) 2020 beqa gozalishvili <beqaprogger@gmail.com>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
import api
import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA
import ui

addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):

	def event_NVDAObject_init(self, obj):
		if not isinstance(obj, UIA): return
		try:
			if obj.UIAElement.CachedClassName == 'Hyperlink' and obj.UIAElement.CachedAutomationId == 'Button' and obj.next.role == controlTypes.ROLE_PROGRESSBAR:
				obj.name = _("Play")
			if obj.UIAElement.CachedClassName == 'ToggleButton':
				return
			if obj.role == controlTypes.ROLE_LISTITEM:
				if obj.parent.UIAElement.CurrentAutomationId == "Messages":
					return
				elif obj.parent.UIAElement.CurrentAutomationId == "ScrollingFiles" or obj.parent.UIAElement.CurrentAutomationId == "ScrollingLinks" or obj.parent.UIAElement.CurrentAutomationId == "ScrollingHost" or obj.parent.UIAElement.CurrentAutomationId == "ScrollingMedia" or obj.parent.UIAElement.CurrentAutomationId == "ScrollingMusic" or obj.parent.UIAElement.CurrentAutomationId == "ScrollingVoice" or obj.parent.UIAElement.CurrentAutomationId == "DialogsSearchListView" or obj.lastChild.UIAElement.CurrentAutomationId == "Label":
					name = []
					for i in obj.children:
						name.append(i.name)
					obj.name = ", ".join(name)
		except AttributeError:
			pass
