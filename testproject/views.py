# from django.shortcuts   import render
# from datetime import datetime
# def index(request):
#     date = datetime.today()
#     context={"thdate":date}
#     return render(request,"testproject/index.html",context)
from django.http import HttpResponse
def index(request):
    return HttpResponse(' Application home page ')
