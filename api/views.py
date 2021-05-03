from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Submissions
from .serializers import SubmissionsSerializer


class SubmissionsView(APIView):
    def post(self, request, format=None):
        serializer = SubmissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Analytics(APIView):
    def post(self, request):
        start_date=request.data['start_date']
        end_date=request.data['end_date']
        data=[]
        submissions = Submissions.objects.filter(date_created__range=[start_date, end_date])
        for contact in submissions: 
            day=contact.date_created.strftime("%Y-%m-%d")
            if len(data)==0 or data[-1]['day']!=day:
                daily_contacts=submissions.filter(date_created=day)
                count_per_day=daily_contacts.count()
                result={"day":day , "count":count_per_day}
                data.append(result)
          
        return Response(data)
  
    



