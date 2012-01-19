#!/usr/bin/env python

from django.conf import settings
from django.db import models

from redd.models.base_upload import BaseUpload

class RelatedUpload(BaseUpload):
    """
    A file related to a dataset file uploaded to PANDA.
    """
    from redd.models.dataset import Dataset

    dataset = models.ForeignKey(Dataset, related_name='related_uploads',
        help_text='The dataset this upload is associated with.')

    file_root = settings.MEDIA_ROOT

    class Meta:
        app_label = 'redd'
        ordering = ['creation_date']

