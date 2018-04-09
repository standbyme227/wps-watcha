from django.contrib import admin
from .. import views
from django.urls import path, include
from ..urls import apis, urls

urlpatterns = [
    path('', include('config.urls.urls')),
    path('api/', include('config.urls.apis')),

]
# '/media/'로 시작하는 요청은 settings.MEDIA_ROOT폴더(ROOT_DIR/.media)에서 파일을 찾아 리턴
# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT,
# )
