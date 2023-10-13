from django.http import HttpResponse
from myCelery.tasks import sub,add
from celery.result import AsyncResult


# Using delay method
def index(request):
    result = add.delay(10,20)
    result1 = sub.delay(800,10)
    print("resut is ", result)
    print("resut is ", result1)
    return HttpResponse("Hellow this endpoint is working")

# Uing Apply_async method
def home(request):
    result = add.apply_async(args=[10,20])
    result1 = sub.apply_async(args=[800,10])
    print("resut is ", result)
    print("resut is ", result1)
    return HttpResponse("Hellow this endpoint is working")



# Diplay result 
def display(request):
    result = add.apply_async(args=[10,20])
    print("resut is ", result)
    return HttpResponse(result)


# Diplay result in output
def display_res(request,task_id):
    result = AsyncResult(task_id)
    return HttpResponse(result.result)





