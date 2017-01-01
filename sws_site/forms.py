from django import forms 

class ContactForm(forms.Form):

	name = forms.CharField(required=True, label_suffix='')
	email = forms.EmailField(required=True, label_suffix='')
	subject = forms.CharField(required=True, label_suffix='')
	message = forms.CharField(
		required=True, 
		widget=forms.Textarea, 
		label_suffix=''
		)

	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "What's your name? "
		self.fields['email'].label = "Email"
		self.fields['subject'].label = "Subject "
		self.fields['message'].label = "Your message "

