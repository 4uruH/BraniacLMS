from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views import generic
from django.views.generic import CreateView, TemplateView
from mainapp import forms as mainapp_forms
from mainapp import models as mainapp_models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


class MainPageView(generic.TemplateView):
    template_name = 'index.html'


class NewsPageView(generic.ListView):
    model = mainapp_models.News
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class NewsCreateView(PermissionRequiredMixin, generic.CreateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.add_news",)


class NewsDetailView(generic.DetailView):
    model = mainapp_models.News


class NewsUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = mainapp_models.News
    fields = "__all__"
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.change_news",)


class NewsDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = mainapp_models.News
    success_url = reverse_lazy("mainapp:news")
    permission_required = ("mainapp.delete_news",)


class ContactsPageView(generic.TemplateView):
    template_name = 'contacts.html'


class DocSitePageView(generic.TemplateView):
    template_name = 'doc_site.html'


class CoursesPageView(generic.TemplateView):
    template_name = 'courses_list.html'


class CoursesListView(generic.TemplateView):
    template_name = "courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            mainapp_models.Courses, pk=pk
        )
        context["lessons"] = mainapp_models.Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        if not self.request.user.is_anonymous:
            if not mainapp_models.CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user
            ).count():
                context["feedback_form"] = mainapp_forms.CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        context["feedback_list"] = mainapp_models.CourseFeedback.objects.filter(
            course=context["course_object"]
        ).order_by("-created", "-rating")[:5]
        return context


class CourseFeedbackFormProcessView(LoginRequiredMixin, CreateView):
    model = mainapp_models.CourseFeedback
    form_class = mainapp_forms.CourseFeedbackForm

    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string(
            "mainapp/includes/feedback_card.html", context={"item": self.object}
        )
        return JsonResponse({"card": rendered_card})
