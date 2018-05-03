from django.contrib import admin
from .models import Member

admin.site.register(Member)
# admin에 등록을해서 django에서 기본제공되는 admin에 나오도록 설정한다.
