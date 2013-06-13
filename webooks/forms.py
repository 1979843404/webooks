# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django import forms
from webooks.models import Chapter

class ChapterAdminForm(forms.ModelForm):
    full_content = forms.CharField(label="full_content",
        widget=forms.Textarea(attrs={'cols': 180, 'rows': 80}))

    class Meta:
        model = Chapter

    def __init__(self, *args, **kwargs):
        super(ChapterAdminForm, self).__init__(*args, **kwargs)
        self.initial.update({"full_content": self.instance.full_content})
