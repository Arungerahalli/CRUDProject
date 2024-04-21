from django.shortcuts import render,redirect
from CRUDApp.models import CRUDApp_StudentTable
from CRUDApp.forms import CRUDApp_StudentTableForm
# Create your views here.

def CRUDApp_GetStudentIndex(request):
    students_display=CRUDApp_StudentTable.objects.all()
    return render(request,'CRUDApp/CRUDApp_GetStudentsIndex.html',{'students':students_display})



def CRUDApp_CreateStudent(request):
    Student_form = CRUDApp_StudentTableForm()
    # CreateStudent is forms object
    #form class here used to accept the student data
    #below block is for add the value to the data base

    if request.method=='POST':
        Student_form=CRUDApp_StudentTableForm(request.POST)
        if Student_form.is_valid():
            Student_form.save()
        return redirect('/') # indicated the home path
 
        # redirecting to the home page to see all the student data

    return render(request,'CRUDApp/CRUDApp_CreateStudent.html',{'form':Student_form}) 
    # 'form' is used in the html file

# deleting based on the id and redirects to the home page
def CRUDApp_DeleteStudent(request,id):
    student_delete=CRUDApp_StudentTable.objects.get(id=id)
    # id is used to map in html
    #fetch one record, id=id that comes in the request(id should be same in html)
    student_delete.delete()
    return redirect('/')