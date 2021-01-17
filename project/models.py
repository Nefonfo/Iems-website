from django.http import Http404
from django.db import models

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

from pure_pagination import Paginator, PageNotAnInteger

from core.models import Project

# Create your models here.
class ProjectsPage(RoutablePageMixin, Page):

    header_title = models.CharField(verbose_name='Título de cabezera', max_length=50)

    content_panels = Page.content_panels + [
        FieldPanel('header_title')
    ]

    @route(r'^$')
    def index(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        resources = Project.objects.all()
        p = Paginator(resources, request=request, per_page=3)

        return self.render(
            request,
            context_overrides= {
                'projects': p.page(page)
            }
        )

    @route(r'^page/(\d+)/$')
    def project_page(self, request, project):
        print(project)
        try:
            project_find = Project.objects.get(pk=project)
            suggests = Project.objects.order_by('?')[0:4]
            return self.render(
                request,
                context_overrides= {
                    'project': project_find,
                    'suggests': suggests
                },
                template='project/project_page.html'
            )
        except:
            raise Http404
