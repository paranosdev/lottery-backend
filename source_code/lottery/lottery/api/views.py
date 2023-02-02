from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):

    def get(self, request, *args, **kwargs):
        return Response(data={'pong': True})

    def post(self, request, *args, **kwargs):
        return Response(data={"pong": True})


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={"pong": True})

    def post(self, request, *args, **kwargs):
        return Response(data={"pong": True})
