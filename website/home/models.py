from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting

@register_setting
class BrandSettings(BaseGenericSetting):

    """Branding for our custom site"""
    logo = models.ImageField(blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)

    panels = [
        MultiFieldPanel([
            FieldPanel("logo"),
        ], heading="Site Branding")
    ]

@register_setting
class SocialMediaSettings(BaseGenericSetting):

    """Social media settings for our custom website."""
    discord = models.URLField(blank=True, null=True, help_text="Discord URL")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    bluesky = models.URLField(blank=True, null=True, help_text="Bluesky URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")
    linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
    
    panels = [
        MultiFieldPanel([
            FieldPanel("discord"),
            FieldPanel("facebook"),
            FieldPanel("bluesky"),
            FieldPanel("youtube"),
            FieldPanel("linkedin"),
        ], heading="Social Media Settings")
    ]



class HomePage(Page):
    hero_image = models.ImageField(blank=True,upload_to=None, height_field=None, width_field=None, max_length=None)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["hero_image","body"]
