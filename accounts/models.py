from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

# Create your models here.


class NewUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)


class Project(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    client = models.ForeignKey(NewUser, blank=True, null=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})


class Proposal(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="proposals",
    )
    body = models.TextField()
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.project.title, self.author)

    def get_absolute_url(self):
        return reverse("provider_dashboard")


class Contract(models.Model):
    title = models.CharField(max_length=255, null=True)
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE, related_name="contracts"
    )
    client = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s " % (self.proposal.project.title, self.title)

    def get_absolute_url(self):
        return reverse("contract_detail", kwargs={"pk": self.pk})
