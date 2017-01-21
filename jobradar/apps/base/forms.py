from django import forms

class QueryForm(forms.Form):
	extras = {
		'name': 'postal_code',
		'type': 'text',
		'value': 'Enter Postal Code',
		'onfocus': 'if (this.value==\'Enter Postal Code\') this.value=\'\';'
	}
	widget = forms.TextInput(attrs=extras)
	location = forms.CharField(label= '',
							   max_length=20,
							   widget=widget)

	# <!-- <input 
	# id="location" 
	# type="text" 
	# name="postal_code" 
	# value="Enter Postal Code" 
	# onfocus="if (this.value=='Enter Postal Code') this.value='';"> -->