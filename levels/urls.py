from django.urls import path
from . import views
import hashlib

app_name = 'levels'

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

    path('level15', views.level15, name='l15'),
    path('697508bad63a602679c9425778ac0faf', views.level15, name='l15'),

    path('level16', views.level16, name='l16'),
    path('c16805f9d36d6f1903633d6cc648f8cf', views.level16, name='l16'),

    path('level17', views.level17, name='l17'),
    path('174d41f50272a75023281ff31aa698ea', views.level17, name='l17'),

    path('level19', views.level19, name='l19'),
    path('f8a8fd9b14a64a8d65d5d43c78a9e132', views.level19, name='l19'),

    path('level20', views.level20, name='l20'),
    path('51651d30a9b0fda668b552f58213134f', views.level20, name='l20'),

    path('level22', views.level22, name='l22'),
    path('a71e79319ff261e4e780c0020c10e39c', views.level22, name='l22'),

    path('level23', views.level23, name='l23'),
    path('7cd319f0748f4daa37749621919d64bd', views.level23, name='l23'),
    path('robots.txt', views.level23_robots, name='l23_robots'),
    path('aa2646a667ee1cd83235786dccef4a26', views.level23_flag, name='l23_flag'),

    path('level24', views.level24, name='l24'),
    path('89e2e6a589eb8ca461a6e10abd3c585c', views.level24, name='l24'),

    path('level25', views.level25, name='l25'),
    path('981c0ba2539e9e053b898ba29a73376d', views.level25, name='l25'),

    path('level26', views.level26, name='l26'),
    path('5abd0b5bc52d246b1f7435ab42c923ce', views.level26, name='l26'),

    path('level27', views.level27, name='l27'),
    path('64faddc6695cb4edc43a7181e9c4e4df', views.level27, name='l27'),

]