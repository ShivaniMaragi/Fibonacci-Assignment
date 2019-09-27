from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
import time
from Fib_Model.models import Fibinfo


def button(request):

    return render(request,'home.html')

def external(request):
    inp= request.POST.get('param')
    start_time=time.time()
    n=int(inp)
    try:
        if(n<0):
            res="Invalid"
        elif(n==0):
            res=n
        elif(n==1):
            res=n
        else:
            first=0
            second=1
            for n in range(n-1):
                num=first+second
                first=second
                second=num
            res=num
        out=str(res)
        out_t=(time.time()-start_time)
        out_time='%f'% (out_t)
        print(out_time)
        print(out)
        fib_info=Fibinfo(inp_digit=inp,out_result=out,time_taken=out_time)
        fib_info.save()
    except Exception as e:
        raise e
    return render(request,'home.html',{'data1':out,'data_time':out_time})
