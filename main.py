from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


@app.get("/hello")
def get_hello():
    return {"message": "Hello, world"}



@app.get('/users/{user_id}')
def get_user(user_id):
    return {'user_id':user_id}

employees_db = {
    1: {"name": "sai", "email": "sai@aifa.com", "position": "Software Engineer", "salary": 75000},
    2: {"name": "ram", "email": "ram@aifa.com", "position": "Project Manager", "salary": 90000},
    3: {"name": "mohan", "email": "mohan@aifa.com", "position": "Data Scientist", "salary": 85000},
}

class Employee(BaseModel):
    name:str
    email:str
    position:str
    salary:int

@app.get("/employees/{employee_id}")
def get_employee(employee_id:int):
        return employees_db[employee_id]





 



