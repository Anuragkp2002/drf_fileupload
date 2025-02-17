from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.


class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')

        if not file:
            return Response({"error": "File is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith('.csv'):
            return Response({"error": "Only csv files are allowed."}, status=status.HTTP_400_BAD_REQUEST)


        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='ISO-8859-1')
        # print("df:",df)
        
        

        required_columns = {'name', 'email', 'age'}
        # print("required_columns",required_columns)
        if not required_columns.issubset(df.columns):
            return Response({"error": "CSV must contain 'name','email','age' columns"}, status=status.HTTP_400_BAD_REQUEST)

        total_records=len(df)
        success_count=0 
        failure_count=0
        errors = []

        for _, row in df.iterrows():
            data = {'name': row['name'], 'email': row['email'], 'age': row['age']}

            serializer = UserSerializers(data=data)
            if serializer.is_valid():
                if not User_tbl.objects.filter(email=row['email']).exists():
                    serializer.save()
                    success_count += 1
                else:
                    failure_count += 1
            else:
                failure_count += 1
                errors.append({'data': data, 'errors': serializer.errors})

        return Response({
            
            "totalrecords": total_records,
            "successfullrecords": success_count,
            "rejectedrecords": failure_count,
            "errors": errors
            
        }, status=status.HTTP_201_CREATED)
