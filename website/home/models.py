from django.db import models

from wagtail.models import (
    Page,
)

from wagtail.fields import RichTextField

class HomePage(Page):

    home_page_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["home_page_hero_image","body"]
