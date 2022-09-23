from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('doc_site/', DocSitePageView.as_view(), name='doc_site'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('courses_list/', CoursesPageView.as_view(), name='courses_list'),
    path('news/', NewsPageView.as_view(), name='news')
]
