"""YtManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

from .views.actions import SyncNowView, DeleteVideoFilesView, DownloadVideoFilesView, MarkVideoWatchedView, \
    MarkVideoUnwatchedView
from .views.auth import ExtendedLoginView, RegisterView, RegisterDoneView
from .views.index import index, ajax_get_tree, ajax_get_videos, CreateFolderModal, UpdateFolderModal, DeleteFolderModal, \
    CreateSubscriptionModal, UpdateSubscriptionModal, DeleteSubscriptionModal
from .views.settings import SettingsView

urlpatterns = [
    # Authentication URLs
    path('login/', ExtendedLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),
    path('', include('django.contrib.auth.urls')),

    # Ajax
    path('ajax/action/sync_now/', SyncNowView.as_view(), name='ajax_action_sync_now'),
    path('ajax/action/delete_video_files/<int:pk>', DeleteVideoFilesView.as_view(), name='ajax_action_delete_video_files'),
    path('ajax/action/download_video_files/<int:pk>', DownloadVideoFilesView.as_view(), name='ajax_action_download_video_files'),
    path('ajax/action/mark_video_watched/<int:pk>', MarkVideoWatchedView.as_view(), name='ajax_action_mark_video_watched'),
    path('ajax/action/mark_video_unwatched/<int:pk>', MarkVideoUnwatchedView.as_view(), name='ajax_action_mark_video_unwatched'),

    path('ajax/get_tree/', ajax_get_tree, name='ajax_get_tree'),
    path('ajax/get_videos/', ajax_get_videos, name='ajax_get_videos'),

    # Modals
    path('modal/create_folder/', CreateFolderModal.as_view(), name='modal_create_folder'),
    path('modal/create_folder/<int:parent_id>/', CreateFolderModal.as_view(), name='modal_create_folder'),
    path('modal/update_folder/<int:pk>/', UpdateFolderModal.as_view(), name='modal_update_folder'),
    path('modal/delete_folder/<int:pk>/', DeleteFolderModal.as_view(), name='modal_delete_folder'),

    path('modal/create_subscription/', CreateSubscriptionModal.as_view(), name='modal_create_subscription'),
    path('modal/create_subscription/<int:parent_folder_id>/', CreateSubscriptionModal.as_view(), name='modal_create_subscription'),
    path('modal/update_subscription/<int:pk>/', UpdateSubscriptionModal.as_view(), name='modal_update_subscription'),
    path('modal/delete_subscription/<int:pk>/', DeleteSubscriptionModal.as_view(), name='modal_delete_subscription'),

    # Pages
    path('', index, name='home'),
    path('settings/', SettingsView.as_view(), name='settings'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)