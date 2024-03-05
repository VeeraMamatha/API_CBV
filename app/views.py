from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView

class productcrud(APIView):
    def get(self,request):
        pdo=products.objects.all()
        pjo=productdetails(pdo,many=True)
        return Response(pjo.data)

    def post(self,request):
        jdo=request.data
        pdo=productdetails(data=jdo)
        if pdo.is_valid():
            pdo.save()
            return Response({'insert':'data is insert secessfully'})

        else:
            return Response({'error':'data is not inserted'})


