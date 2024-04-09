import json
from fastapi import FastAPI, HTTPException, APIRouter
from bson import json_util
from bson import ObjectId
from config.db import collection
from schemas.studentSchema import StudentModel, PatchStudentModel

studentApp = APIRouter()


#  API to insert student records
@studentApp.post("/students")
async def add_students(student: StudentModel):
    # Insert student into database
    result = collection.insert_one(student.dict())
    if result.inserted_id:
        return {"status": "201 Created", "student_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create student")


# get all student details
@studentApp.get("/students")
async def get_students():
    students_cursor = collection.find({})
    students_list = []
    for student in students_cursor:
        students_list.append(student)

    # Convert the list of documents to JSON
    return json.loads(json_util.dumps(students_list))


@studentApp.get("/students/{student_id}")
async def get_student(student_id: str):
    try:
        student_id = ObjectId(student_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid student_id")

    # Query to Retrieve data from database
    student_data = collection.find_one({"_id": student_id})
    if student_data:
        student = StudentModel(name=student_data["name"], age=student_data["age"], address=student_data["address"])
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")


# Patch API to update student details
@studentApp.patch("/students/{student_id}")
async def update_student(student_id: str, update_data: PatchStudentModel):
    try:
        student_id = ObjectId(student_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid student_id")

    update_data = {key: value for key, value in update_data.dict().items() if value is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    # Query to Update the new data in database
    result = collection.update_one({"_id": student_id}, {"$set": update_data})
    if result.modified_count > 0:
        return {"status": "200 OK, Student updated"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")


# Delete student records from database
@studentApp.delete("/students/{student_id}")
async def remove_student(student_id: str):
    try:
        student_id = ObjectId(student_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid student_id")

    # Query to delete data from database
    deleted_student = collection.delete_one({ "_id": student_id })

    if deleted_student.deleted_count:
        return {"status": "200 OK: Student Deleted"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
