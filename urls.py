from django.contrib import admin
from django.urls import path, include


#todoprojectのurls.pyでなくtodoappのurls.pyを使うんだという宣言
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("todoapp.urls"))
]
