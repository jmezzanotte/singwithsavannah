from django import template

register = template.Library()


@register.filter(name='img_helper')
def img_helper():
	'''Custom filter tag to remove the file name'''
	return 'images/'

