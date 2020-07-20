from django.db import models as m


class ResumePage(m.Model):
    title = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    h1 = m.TextField(null=True, blank=True)
    preview = m.TextField(null=True, blank=True)
    article = m.TextField(null=True, blank=True)
    text = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Resume Page"

    def __str__(self):
        return f"ResumePage [id_{self.pk}]"


class Technology(m.Model):
    name = m.TextField()
    description = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return f"{self.name} [id_{self.pk}]"


class Project(m.Model):
    started_at = m.DateField(null=True, blank=True)
    finished_at = m.DateField(null=True, blank=True)
    summary = m.TextField(null=True, blank=True)
    achievements_text = m.TextField(null=True, blank=True)
    technologies = m.ManyToManyField(Technology, related_name="project")
    link = m.TextField(null=True, blank=True)
    name = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.name} [id_{self.pk}]"


class Responsibility(m.Model):
    summary = m.TextField()
    project = m.ForeignKey(
        Project, on_delete=m.CASCADE, related_name="responsibilities"
    )

    class Meta:
        verbose_name_plural = "Responsibilities"

    def __str__(self):
        return f"Responsibility [id_{self.pk}]"
