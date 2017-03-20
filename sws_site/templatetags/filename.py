from django import template
import os 


register = template.Library()

@register.filter(name='filename')
def filename(value):
	'''Custom filter tag to remove the file name'''
	return os.path.basename(os.path.splitext(value)[0]).replace('_', ' ')

