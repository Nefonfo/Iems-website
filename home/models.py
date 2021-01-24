from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from . import streams as h_stream

class HomePage(Page):
    body = StreamField([
        ('hero_header', h_stream.HeroHeaderBlock()),
        ('skills', h_stream.SkillsBlock()),
        ('features', h_stream.FeaturesBlock()),
        ('projects', h_stream.ProjectsBlock()),
        ('testimonials', h_stream.TestimonialsBlock()),
        ('mobile_hero', h_stream.MobileHeroBlock()),
        ('laptop_hero', h_stream.LaptopHeroBlock()),
        ('mobile_hero', h_stream.MobileHeroBlock()),
        ('contact_banner', h_stream.ContactBannerBlock()),
        ('companies_block', h_stream.CompaniesBlock()),
        ('team_stack_block', h_stream.TeamStackBlock()),
        ('contact_mobile_block', h_stream.ContactMobileBlock())
    ], blank=False, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    class Meta:
        verbose_name = 'commonpage'