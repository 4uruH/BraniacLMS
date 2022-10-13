from django.urls import path
from .views import *
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('doc_site/', DocSitePageView.as_view(), name='doc_site'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('news/', NewsPageView.as_view(), name='news'),
    path("news/create/", NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("news/<int:pk>/update", NewsUpdateView.as_view(), name="news_update"),
    path("news/<int:pk>/delete", NewsDeleteView.as_view(), name="news_delete"),
    path('courses_list/', CoursesListView.as_view(), name='courses_list'),
    path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail"),
    path("course_feedback/", CourseFeedbackFormProcessView.as_view(), name="course_feedback")

]
