from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock

class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock()
    description = blocks.CharBlock(
        min_length = 10,
        max_length = 100,
        help_text = 'Pequeña descripción')
    author = blocks.CharBlock(
        min_length = 2,
        max_length = 30,
        help_text = 'Nombre del autor')

    class Meta:
        icon = 'pick'
        template = 'document/blocks/document.html'