from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list.as_view(), name = 'home'),
    # path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail'),
    # path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
    path('update/<int:pk>/', views.note_update.as_view(), name='note_update'),
    path('detail/<int:pk>/', views.note_details.as_view(),name='note_detail'),
    path('delete/<int:pk>/', views.note_delete.as_view(), name='note_delete'),
    path('unpinned/<int:pk>/', views.note_unpinned.as_view(), name='note_unpinned'),
    path('pinned/<int:pk>/', views.note_pinned.as_view(), name='note_pinned'),
    path('archived/<int:pk>/', views.note_archived.as_view(), name='note_archived'),
    path('lable/<int:pk>/', views.note_lable.as_view(), name='note_lable'),
    path('reminder/<int:pk>/', views.note_reminder.as_view(), name='note_reminder'),
    path('collaborate/<int:pk>/', views.note_colaborator.as_view(), name='note_collaborate'),
]
#
# url('<int:pk>/', views.note_details.as_view(), name='detail_note'),
# url('update/<int:pk>/', views.note_update.as_view(), name='update_note'),
# url('', views.note_list.as_view(), name='home'),
