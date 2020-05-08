from django.shortcuts import render
from rest_framework import generics
from deals.serializers import *
from deals.models import Deal
from deals.forms import UploadFileForm
from django.http import HttpResponseRedirect
from deals.handles import handle_uploaded_file
from django.db.models import Sum, Count


class DealCreateView(generics.CreateAPIView):
    serializer_class = DealCreateSerializer


class DealListView(generics.ListAPIView):
    serializer_class = DealListSerializer
    queryset = Deal.objects.all()


class DealSpentUsersView(generics.ListAPIView):
    @staticmethod
    def get_deals():
        top_5 = list(Deal.objects.values('customer').annotate(total_sum=Sum('total')).order_by('-total_sum')[:5])
        all_deals = Deal.objects.all()
        for t_sale in top_5:
            items = [sale.item for sale in all_deals if sale.customer == t_sale['customer']]
            t_sale['unique_items'] = list(set(items))
        for t_sale in top_5:
            gems = set()
            for other_sale in top_5:
                if t_sale['customer'] == other_sale['customer']:
                    continue
                intersection = set(t_sale['unique_items']) & set(other_sale['unique_items'])
                if len(intersection):
                    gems.update(intersection)
            t_sale['gems'] = list(gems)

        return top_5

    serializer_class = DealSpentUsersSerializer
    queryset = get_deals.__func__()


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
