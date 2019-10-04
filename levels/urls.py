from django.urls import path
from . import views
import hashlib



urlpatterns = [
    path('', views.index, name='index'),
    path('caf7e7bf96a799f0547469cb698bfb68', views.indexDemo, name='index'),
    path('level1', views.level1, name='l1'),
    path('level2', views.level2, name='l2'),
    path('level4', views.level4, name='l4'),
    path('level7', views.level7, name='l7'),
    path('level9', views.level9, name='l9'),
    path('level12', views.level12, name='l12'),
    path('level13', views.level13, name='l13'),
    path('level13.old', views.level13_flag, name='l13_flag'),
    path('level13.backup', views.level13_flag, name='l13_flag'),
    path('level13.~', views.level13_flag, name='l13_flag'),
    path('level16', views.level16, name='l16'),
    path('level17', views.level17, name='l17'),
    path('level19', views.level19, name='l19'),
    path('level20', views.level20, name='l20'),
    path('level22', views.level22, name='l22'),
    path('level23', views.level23, name='l23'),
    path('robots.txt', views.level23_robots, name='l23_robots'),
    path('level24', views.level24, name='l24'),
    path('level25', views.level25, name='l25'),

]