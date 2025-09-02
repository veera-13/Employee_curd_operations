import requests
import json
Base_url="http://127.0.0.1:8000/"
End_point="employee/"
def create():
    empid=int(input("Enter Employee id:"))
    empname=input("Enter Employee Name:")
    job=input("Enter Job:")
    salary=float(input("Enter salary:"))

    d={'empid':empid,'empname':empname,'job':job,'salary':salary}
    stud_data=json.dumps(d)
    res=requests.post(Base_url+End_point,data=stud_data)
    print(res.json())

def get_all():
    d={}
    json_data=json.dumps(d)
    res=requests.get(Base_url+End_point,data=json_data)
    print(res.json())


def delete():
    num=int(input("Enter employee id:"))
    d={'empid':num}
    json_data=json.dumps(d)
    response=requests.delete(Base_url+End_point,data=json_data)
    print(response.json())
# delete()
# create()












get_all()