from django.views.generic import TemplateView
from datetime import datetime
import json


class MainPageView(TemplateView):
    template_name = 'index.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open("data_file.json", 'r') as file:
            context['news_title_description'] = json.load(file)
        # context['news_title'] = data.keys
        # context['description'] = data
        context['news_date'] = datetime.now()
        context['range'] = range(5)

        return context


class LoginPageView(TemplateView):
    template_name = 'login.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'
