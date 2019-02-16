from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    path("choices/", views.choices, name="choices"),
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("pytanie/<slug:question_text>/", views.pyt, name="pyt"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# urlpatterns = [
#     path("choices/", views.choices, name="choices"),
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]