from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class PublicationsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        
        context = super().get_context(request)
        publicationpages = self.get_children().live().order_by('title')
        context['publicationpages'] = publicationpages
        return context

    content_panels = Page.content_panels + ["intro"]

class PublicationPage(Page):

    publication_pic = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Publication promo image",
    )

    name = models.CharField(
        blank=True,
        max_length=255, help_text="Name"
    )

    teaser = models.CharField(
        blank=True,
        max_length=255, help_text="Short teaser text"
    )

    purchase_link = models.URLField(
        blank=True, 
        null=True, 
        help_text="Offsite Purchase URL"
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel("publication_pic"),
        FieldPanel('name'),
        FieldPanel('teaser'),
        FieldPanel('purchase_link'),
        FieldPanel('body'),
    ]
