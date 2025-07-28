# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Entrreprise(models.Model):

    #__Entrreprise_FIELDS__
    siren = models.CharField(max_length=255, null=True, blank=True)
    date_creation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_radiation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    forme_juridique = models.CharField(max_length=255, null=True, blank=True)

    #__Entrreprise_FIELDS__END

    class Meta:
        verbose_name        = _("Entrreprise")
        verbose_name_plural = _("Entrreprise")


class Etablissement(models.Model):

    #__Etablissement_FIELDS__
    siren = models.ForeignKey(Entrreprise, on_delete=models.CASCADE)
    siret = models.CharField(max_length=255, null=True, blank=True)
    id_adresse = models.CharField(max_length=255, null=True, blank=True)

    #__Etablissement_FIELDS__END

    class Meta:
        verbose_name        = _("Etablissement")
        verbose_name_plural = _("Etablissement")



#__MODELS__END
