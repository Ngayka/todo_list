from django.core.exceptions import ValidationError
from django.db import models


class Task(models.Model):
    content = models.TextField()
    date_of_applying = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    its_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def clean(self):
        if self.deadline and self.deadline < self.date_of_applying:
            raise ValidationError("Deadline cannot be earlier than date of applying")


class Tag(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return f"#{self.name}"