from django import template

register = template.Library()


@register.filter(name='test')
def images():
	'''Custom filter tag to remove the file name'''
	return 'images/'

