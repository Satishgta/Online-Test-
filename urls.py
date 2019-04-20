from django.conf.urls import url
from exam import views
urlpatterns=[
    url('result/',views.showResult),
    url('test/',views.showTest),
]