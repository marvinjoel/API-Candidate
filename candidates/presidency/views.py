from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from candidates.presidency.models import PresidencyModel
from candidates.presidency.serializers import PresidencySerializers


class CandidateListView(APIView):

    def get(self, request):
        candidate = PresidencyModel.objects.all()
        candidate_json = PresidencySerializers(candidate, many=True)
        return Response(candidate_json.data)


class CandidateDetails(APIView):

    def get(self, request, pk):
        try:
            candidate = PresidencyModel.objects.get(pk=pk)
            candidate_json = PresidencySerializers(candidate)
            return Response(candidate_json.data)
        except PresidencyModel.DoesNotExist:
            raise Http404
