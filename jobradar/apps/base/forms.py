from django import forms

class QueryForm(forms.Form):
	onfocus = """
		if (this.value == \'Enter Postal Code\') {
			this.value = \'\';
		};
	"""

	extras = {
		'name': 'postal_code',
		'type': 'text',
		'value': 'Enter Postal Code',
		'onfocus': onfocus
	}
	widget = forms.TextInput(attrs=extras)
	location = forms.CharField(label= '',
							   max_length=20,
							   widget=widget)

	def clean_postal_code(self):
		pass