
"""定义learning_logs的URL模式"""
from django.conf.urls import url  #导入函数url,用来将url映射到视图
from . import views  #导入模块views,句点表示从当前文件夹中导入视图

urlpatterns = [
    # 主页，包含可在应用程序learning_logs中请求的网页
    url(r'^$', views.index, name='index'),
    #显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),


]