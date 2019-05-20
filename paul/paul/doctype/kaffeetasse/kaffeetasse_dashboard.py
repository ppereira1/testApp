from frappe import _

def get_data():
	return {
		'fieldname': 'kaffeetasse',
		'transactions': [
			{
				'label': _('Verleih der Kaffetassen'),
				'items': ['Kaffeetassenverleih']
			}
		]
	}
