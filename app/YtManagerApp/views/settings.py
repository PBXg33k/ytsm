from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Submit
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from YtManagerApp.models import UserSettings


class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            'mark_deleted_as_watched',
            'delete_watched',
            HTML('<h2>Download settings</h2>'),
            'auto_download',
            'download_path',
            'download_file_pattern',
            'download_format',
            'download_order',
            'download_global_limit',
            'download_subscription_limit',
            HTML('<h2>Subtitles download settings</h2>'),
            'download_subtitles',
            'download_subtitles_langs',
            'download_subtitles_all',
            'download_autogenerated_subtitles',
            'download_subtitles_format',
            Submit('submit', value='Save')
        )


class SettingsView(LoginRequiredMixin, UpdateView):
    form_class = SettingsForm
    model = UserSettings
    template_name = 'YtManagerApp/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj, _ = self.model.objects.get_or_create(user=self.request.user)
        return obj
