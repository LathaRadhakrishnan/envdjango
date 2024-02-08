from django.shortcuts import render

# Create your views here.
# helloworldapp/views.py

from django.http import HttpResponse
from django.conf import settings


from django.http import HttpResponseServerError
import psutil

def throw_internal_server_error(request):
    # Simulate an internal server error
    raise Exception("Internal Server Error")

def consume_memory(request):
    # Consume memory until reaching a specified limit
    memory_limit = 100000000  # 100 MB
    data = bytearray(memory_limit)
    return HttpResponseServerError("Memory Limit Exceeded")

def use_cpus(request):
    # Use all available CPUs
    cpu_count = psutil.cpu_count()
    for _ in range(cpu_count):
        psutil.cpu_percent(interval=1)
    return HttpResponseServerError("CPU Usage Exceeded")




