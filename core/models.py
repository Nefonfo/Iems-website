from django.db import models

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.edit_handlers import SnippetChooserPanel

# Create your models here.

# SITE SETTINGS
@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Tu URL de Facebook')
    instagram = models.CharField(
        max_length=255, help_text='Instagram (sin @)')
    twitter = models.URLField(
        help_text='Tu URL de Twitter')

# FRAGMENTS
@register_snippet
class Project(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    company_related = models.ForeignKey('core.Company', blank = False, null=True, on_delete=models.SET_NULL, related_name='+')
    title = models.CharField(
        verbose_name = "Título",
        max_length = 40,
        blank = False, 
        null = False)
    intro = models.CharField(
        verbose_name = "Introducción",
        max_length = 100,
        blank = False,
        null = False)
    date = models.DateField(
        verbose_name = 'Fecha del Proyecto',
        blank= False,
        null = False
    )
    description = RichTextField()

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        SnippetChooserPanel('company_related'),
        FieldPanel('intro'),
        FieldPanel('date'),
        FieldPanel('description', classname='full')
    ]

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

@register_snippet
class Company(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(
        verbose_name = "Título",
        max_length = 40,
        blank = False, 
        null = False)
    intro = models.CharField(
        verbose_name = "Introducción",
        max_length = 100,
        blank = False,
        null = False)
    description = RichTextField()

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('name'),
        FieldPanel('intro'),
        FieldPanel('description', classname='full')
    ]

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Compañia'
        verbose_name_plural = 'Compañias'