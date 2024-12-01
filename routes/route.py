from fastapi import APIRouter , HTTPException, Query, Path
from fastapi.responses import JSONResponse
from models.todos import Todo
from models.students import Student, StudentUpdate
from config.database import collection_name
from config.database import db
from schema.schemas import list_serial
from bson import ObjectId
from pydantic import BaseModel

router = APIRouter()

# GET Request
@router.get("/")
async def get_root():
    '''Return the name'''
    return JSONResponse(content={"message": "API Working, go to /docs"})
    
# POST Request for creating a student
@router.post("/students", status_code=201)
async def create_student(student: Student):
    """
    Create a new student in the system.
    """
    # Insert the student data into the database
    result = db.students.insert_one(student.dict())
    
    if result.inserted_id:
        return {"id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create student")

@router.get("/students", response_model=dict)
async def list_students(country: str = Query(None, description="To apply filter of country"),
                        age: int = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result")):
    """
    List students with optional filters.
    """
    query = {}
    
    if country:
        query['address.country'] = country
        
    if age:
        query['age'] = {'$gte': age}
    
    students = db.students.find(query)
    student_list = [{"name": student["name"], "age": student["age"]} for student in students]
    return {"data": student_list}

@router.get("/students/{id}", response_model=Student)
async def get_student(id: str = Path(..., title="The ID of the student")):
    """
    Fetch details of a specific student by ID.
    """
    student = db.students.find_one({"_id": ObjectId(id)})
    
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")
    
@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student_update: StudentUpdate):
    """
    Update details of a specific student by ID.
    """

    update_data = student_update.dict(exclude_unset=True)
    
    result = db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
@router.delete("/students/{id}", status_code=200)
async def delete_student(id: str = Path(..., title="The ID of the student")):
    """
    Delete a specific student by ID.
    """

    result = db.students.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {}