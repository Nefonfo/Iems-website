from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from .streams import DocumentBlock
# Create your models here.
class DocumentPage(Page):
    documents = StreamField([
        ('document', DocumentBlock())
    ], blank = True, null = True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('documents')
    ]