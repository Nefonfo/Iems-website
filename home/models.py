from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from . import streams as h_stream

from project.models import ProjectsPage

class HomePage(Page):
    body = StreamField([
        ('hero_header', h_stream.HeroHeaderBlock()),
        ('skills', h_stream.SkillsBlock()),
        ('features', h_stream.FeaturesBlock()),
        ('projects', h_stream.ProjectsBlock()),
        ('mobile_hero', h_stream.MobileHeroBlock()),
        ('laptop_hero', h_stream.LaptopHeroBlock()),
        ('mobile_hero', h_stream.MobileHeroBlock()),
        ('contact_banner', h_stream.ContactBannerBlock())
    ], blank=False, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    def get_context(self, request, *args, **kwargs):
        ctx = super(HomePage, self).get_context(request, *args, **kwargs)
        ctx['inner_projects_page'] = ProjectsPage.objects.live()[0]
        return ctx
