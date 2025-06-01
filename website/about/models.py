from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class AboutIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        
        context = super().get_context(request)
        aboutpages = self.get_children().live().order_by('title')
        context['aboutpages'] = aboutpages
        return context

    content_panels = Page.content_panels + ["intro"]

class AboutPage(Page):

    profile_pic = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="About profile image",
    )

    name = models.CharField(
        blank=True,
        max_length=255, help_text="Display Name"
    )

    role = models.CharField(
        blank=True,
        max_length=255, help_text="Role Name"
    )

    email = models.EmailField(
        blank=True,
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel("profile_pic"),
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('email'),
        FieldPanel('body'),
    ]