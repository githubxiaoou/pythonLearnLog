"""定义learning_logs的URL模式。"""

from django.urls import path

from . import views

# 此处踩坑，忘记加app_name，https://stackoverflow.com/questions/51018310
app_name = 'learning_logs'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]
