from django.db import models as m


class EducationPage(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    h1 = m.TextField(null=True, blank=True)
    university = m.TextField(null=True, blank=True)
    text = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Education Page"

    def __str__(self):
        return f"EducationPage(id={self.pk})"
