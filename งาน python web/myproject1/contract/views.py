from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def contract(request):
  template = loader.get_template('mycontract.html')
  return HttpResponse(template.render())


