from django.contrib import admin
from .models import Services, ServicesLandingPage, About

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
	
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = Services

class ServicesLandingPageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = ServicesLandingPage

class AboutAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = About

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesLandingPage, ServicesLandingPageAdmin)
admin.site.register(About, AboutAdmin)