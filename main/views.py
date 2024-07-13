from django.db.models import Sum
from django.shortcuts import render
from utils import *
from .models import *


def index(request):
    if request.method == "POST":
        delete_record()
        insert_to_db()
    if request.method == "GET":
        q1 = Protocol.objects.values('date').annotate(traffic_sum=Sum('traffic'))
        list_q1 = list(q1)
        labels_q1 = []
        values_q1 = []
        for i in list_q1:
            labels_q1.append(str(i['date']).split(' ')[0])
            values_q1.append(i['traffic_sum'])

        q2 = Protocol.objects.values('user__name').annotate(traffic_sum2=Sum('traffic'))
        list_q2 = list(q2)
        labels_q2 = []
        values_q2 = []
        for i in list_q2:
            labels_q2.append(i['user__name'])
            values_q2.append(i['traffic_sum2'])

        q3 = Protocol.objects.values('websystem__name').annotate(traffic_sum2=Sum('traffic'))
        list_q3 = list(q3)
        labels_q3 = []
        values_q3 = []
        for i in list_q3:
            labels_q3.append(i['websystem__name'])
            values_q3.append(i['traffic_sum2'])

        return render(request,
                      'index.html',
                      {
                          'labels': labels_q1,
                          'values': values_q1,

                          'labels_q2': labels_q2,
                          'values_q2': values_q2,

                          'labels_q3': labels_q3,
                          'values_q3': values_q3,
                      })

    return render(request, 'index.html')
