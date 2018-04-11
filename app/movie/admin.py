from django.contrib import admin

from .models import *

admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(StillCut)
admin.site.register(TrailerYouTube)
admin.site.register(Movie)
admin.site.register(MovieToMember)
admin.site.register(UserToMovie)
