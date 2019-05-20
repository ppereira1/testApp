
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Kaffeetasse"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Kaffeetasse",
                    "label": _("Kaffeetasse Item"),
                    "description": _("Kaffeetasse Item")
                }
            ]     
        }
    ]
