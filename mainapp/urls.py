from django.urls import path

from .views import *

urlpatterns = {
    path('', MainPageView.as_view()),
    path('login.html/', LoginPageView.as_view()),
    path('doc_site.html/', DocSitePageView.as_view()),
    path('contacts.html/', ContactsPageView.as_view()),
    path('courses_list.html', CoursesPageView.as_view()),
    path('news.html/', NewsPageView.as_view())
}
