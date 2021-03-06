from django.contrib import admin
from .models import Services, ServicesLandingPage, About, Album, AlbumTrack, Home, Contact

# Register your models here.

class HomeAdmin(admin.ModelAdmin):

	list_display = ['__unicode__', 'timestamp']

	class Meta: 
		model = Home

class ServicesAdmin(admin.ModelAdmin):
	
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = Services

class ContactAdmin(admin.ModelAdmin):
	
	list_display = ['timestamp']

	class Meta:
		model = Contact

class ServicesLandingPageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = ServicesLandingPage

class AboutAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']

	class Meta:
		model = About

class AlbumAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']

	class Meta: 
		model = Album

class AlbumTrackAdmin(admin.ModelAdmin):

	class Meta: 
		model = AlbumTrack




admin.site.register(Home, HomeAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesLandingPage, ServicesLandingPageAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumTrack, AlbumTrackAdmin)