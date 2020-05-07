from django.shortcuts import render
from rest_framework import generics
from deals.serializers import DealCreateSerializer, DealDetailSerializer, DealListSerializer
from deals.models import Deal
from deals.forms import UploadFileForm
from django.http import HttpResponseRedirect
from deals.handles import handle_uploaded_file


class DealCreateView(generics.CreateAPIView):
    serializer_class = DealCreateSerializer


class DealListView(generics.ListAPIView):
    serializer_class = DealListSerializer
    queryset = Deal.objects.all()


class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DealDetailSerializer
    queryset = Deal.objects.all()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request)
            return HttpResponseRedirect('all')
    else:
        form = UploadFileForm()

    context = {'form': form}
    return render(request, 'deals/upload.html', context)
