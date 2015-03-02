from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProtectedResource(models.Model):
    
    path = models.CharField(_('Protected Resource'), max_length=255,
                            unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('protected_resource')
        verbose_name_plural = _('protected_resources')
        ordering = 'path'

    def __unicode__(self):
        return self.path


class WhitelistedHost(models.Model):

    host = models.CharField(_('Whitelisted Host'), max_length=255,
                            unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('whitelisted_host')
        verbose_name_plural = _('whitelisted_hosts')
        ordering = 'host'

    def __unicode__(self):
        return self.host


