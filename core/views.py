from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .search_logic import search_engine

class SearchView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        query = request.data.get("query", '').strip()
        
        if not query:
            return Response({'error': "No search query was sent."}, status = status.HTTP_400_BAD_REQUEST)
        
        results = search_engine.search(query, top_n=10)
        
        return Response(results, status=status.HTTP_200_OK)