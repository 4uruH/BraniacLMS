from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp import models
from django.core.paginator import Paginator


class MainPageView(TemplateView):
    template_name = 'index.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'
    paginated_by = 3

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get(
            'page',
            1
        )
        paginator = Paginator(models.News.objects.all(), self.paginated_by)
        page = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)

        context["page"] = page
        context["news"] = models.News.objects.all()

        return context


class LoginPageView(TemplateView):
    template_name = 'login.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'


class NewsPageDetailView(TemplateView):
    template_name = "news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(models.News, pk=pk)
        return context


class CoursesListView(TemplateView):
    template_name = "courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            models.Courses, pk=pk
        )
        context["lessons"] = models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = models.CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        return context
