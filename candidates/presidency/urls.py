from django.contrib import admin
from django.urls import path

from candidates.presidency.views import CandidateListView, CandidateDetails

urlpatterns = [
    path('candidate/', CandidateListView.as_view(), name = 'list'),
    path('candidate/<int:pk>', CandidateDetails.as_view(), name = 'details'),
]
