from django.shortcuts import render,redirect

from todoapp.models import task
# Create your views here.
def home(request):
    data=task.objects.all()
    all_data={'data':data}
    return render(request,'todo/index.html',all_data)




def show(request):
    if (request.method=='POST'):
        heading_=request.POST['heading']
        detail_=request.POST['detail']
        date_=request.POST['date']
        # print(heading_)
        # print(detail_)

        #creating sql query to insert data into databases
        #model_class.objects.create(column_name=value)
        insert_data=task.objects.create(heading=heading_,detail=detail_,date=date_,is_deleted='n')
        #executing sql query
        insert_data.save()
        return redirect("/")



    return render(request,'todo/add.html')

def delete(request,tid):
    record_to_be_deleted=task.objects.filter(id=tid)
    record_to_be_deleted.update(is_deleted='y')
    return redirect("/")


def update(request,tid):
    if (request.method=='POST'):
        heading_f=request.POST['heading']
        detail_f=request.POST['detail']
        date_f=request.POST['date']
        record_tobe_update=task.objects.filter(id=tid)
        record_tobe_update.update(heading=heading_f,detail=detail_f,date=date_f)
        return redirect('/')

    else:
        content={}
        content['data']=task.objects.get(id=tid)
        return render(request,'todo/update.html',content)
