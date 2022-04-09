from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

def get_hello(request: WSGIRequest) -> HttpResponse:
	return HttpResponse("hello world")

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
	return HttpResponse("test")
