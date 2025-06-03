from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)

from wagtail.models import (
    Page,
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting

from wagtail.snippets.models import register_snippet

@register_setting
class BrandSettings(BaseGenericSetting):

    """Branding for our custom site"""
    brand_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    affiliate_text = RichTextField(blank=True)

    affiliate_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("brand_logo"),
            FieldPanel("affiliate_text"),
            FieldPanel("affiliate_logo"),
        ], heading="Site Branding")
    ]

@register_setting
class SocialMediaSettings(BaseGenericSetting):

    """Social media settings for our custom website."""
    discord = models.URLField(blank=True, null=True, help_text="Discord URL")
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
    bluesky = models.URLField(blank=True, null=True, help_text="Bluesky URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")
    linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
    
    panels = [
        MultiFieldPanel([
            FieldPanel("discord"),
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("bluesky"),
            FieldPanel("youtube"),
            FieldPanel("linkedin"),
        ], heading="Social Media Settings")
    ]

@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]