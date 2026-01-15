from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=5)

class NoteResponse(NoteCreate):
    id: int

    class Config:
        from_attributes = True
