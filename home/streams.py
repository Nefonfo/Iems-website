from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailfontawesome.blocks import IconBlock

from core.models import Project
from project.models import ProjectsPage

class HeroHeaderBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        min_length = 2,
        max_length = 30,
        help_text = 'Titulo')
    dynamic_text = blocks.ListBlock(
        blocks.CharBlock(
            min_length = 1,
            max_length = 30,
            help_text = 'Titulo Dinámico'))
    subtitle = blocks.CharBlock(
        min_length = 10,
        max_length = 70,
        help_text = 'Titulo')
    button_text = blocks.CharBlock(
        min_length = 3,
        max_length = 70,
        help_text = 'Titulo')
    image = ImageChooserBlock()

    class Meta:
        icon = 'pick'
        template = 'home/blocks/hero_header.html'

class SkillsBlock(blocks.StructBlock):

    class SkillBlock(blocks.StructBlock):
        name = blocks.CharBlock(
            min_length = 1,
            max_length = 20,
            help_text = 'Tecnología')
        percentage = blocks.FloatBlock(
            min_value = 0,
            max_value = 100,
            help_text = 'Porcentaje'
        )
        image = ImageChooserBlock()

        class Meta:
            icon = 'placeholder'

    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    skills = blocks.ListBlock(
        SkillBlock())

    class Meta:
        icon = 'form'
        template = 'home/blocks/skills.html'

class FeaturesBlock(blocks.StructBlock):

    class FeatureBlock(blocks.StructBlock):
        icon = IconBlock()
        title = blocks.CharBlock(
            min_length = 5,
            max_length = 100,
            help_text = 'Titulo')
        text = blocks.TextBlock(
            help_text = 'Descripción'
        )

        class Meta:
            icon = 'placeholder'

    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    features = blocks.ListBlock(
        FeatureBlock())

    class Meta:
        icon = 'cogs'
        template = 'home/blocks/features.html'

class ProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')

    def get_context(self, value, parent_context):
        ctx =  super(ProjectsBlock, self).get_context(value, parent_context=parent_context)
        try:
            ctx['inner_projects_page'] = ProjectsPage.objects.live()[0]
            ctx['projects'] = Project.objects.order_by('?')[0:6]
        except Project.DoesNotExist:
            ctx['projects'] = None
            ctx['inner_projects_page'] = None
        return ctx

    class Meta:
        icon = 'doc-empty'
        template = 'home/blocks/release_projects.html'

class TestimonialsBlock(blocks.StructBlock):

    class TestimonialBlock(blocks.StructBlock):
        author = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Subtítulo')
        author_position = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Subtítulo',
            required=False)
        image = ImageChooserBlock()
        text = blocks.CharBlock(
            min_length = 10,
            max_length = 400,
            help_text = 'Subtítulo')

        class Meta:
            icon = 'placeholder'

    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    subtitle = blocks.CharBlock(
            min_length = 10,
            max_length = 400,
            help_text = 'Subtítulo')
    testimonials = blocks.ListBlock(TestimonialBlock())

    class Meta:
        icon = 'wagtail'
        template = 'home/blocks/testimonial.html'


class MobileHeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    text = blocks.TextBlock(
            help_text = 'Texto')
    image = ImageChooserBlock()

    class Meta:
        icon = 'radio-full'
        template = 'home/blocks/mobile_hero.html'

class LaptopHeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    text = blocks.TextBlock(
            help_text = 'Texto')
    image = ImageChooserBlock()

    class Meta:
        icon = 'radio-empty'
        template = 'home/blocks/laptop_hero.html'

class ContactBannerBlock(blocks.StructBlock):
    title = blocks.CharBlock(
            min_length = 10,
            max_length = 100,
            help_text = 'Titulo')
    button_title = blocks.CharBlock(
            min_length = 10,
            max_length = 70,
            help_text = 'Titulo del Botón')
    link = blocks.PageChooserBlock()

    class Meta:
        icon = 'cogs'
        template = 'home/blocks/contact.html'


