# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:38:40 2017

@author: viraj
"""

from django.conf.urls import url,include

from . import views

urlpatterns = [
        
        url(r'^$',views.index,name='index'),
        url(r'^result/',views.result,name='result'),
        url(r'^afterlogin/',views.login,name='afterlogin'),
	url(r'^syllabus/(?P<syllabus_name>[\w ].*)/',views.show_syllabus,name='show_syllabus'),
	url(r'^review/', include('review.urls')),
	url(r'^allcontent',views.all_content),
	url(r'^submission',views.syllabus_submission),
        url(r'^projectboard',views.project_board),
	url(r'^submitproject',views.project_submission), 
]
