from django.urls import path
from . import views
import hashlib



urlpatterns = [
    path('', views.index, name='index'),
    path('caf7e7bf96a799f0547469cb698bfb68', views.indexDemo, name='index'),

    path('level1', views.level1, name='l1'),
    path('c341b271f5dba18dd4099435670a2c74', views.level1, name='l1'),

    path('level2', views.level2, name='l2'),
    path('3105bcfda5ac6fb239ab134c6724673d', views.level2, name='l2'),

    path('level4', views.level4, name='l4'),
    path('c9dfacd4ab90728131cba2fa604329da', views.level4, name='l4'),

    path('level7', views.level7, name='l7'),
    path('061d06844f75ab4a77087f83f09f1bec', views.level7, name='l7'),

    path('level9', views.level9, name='l9'),
    path('eaff21cfa63a828f34f02f4bc739a5de', views.level9, name='l9'),

    path('level12', views.level12, name='l12'),
    path('e3cb9dac40a829e5d0194b8fadc5ea0b', views.level12, name='l12'),

    path('level13', views.level13, name='l13'),
    path('0fc1d6918da0bacc7d8b3dcbf25853ad', views.level13, name='l13'),

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