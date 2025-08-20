from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TodoItem(BaseModel):
    id: str
    text: str
    created_at: datetime
    completed: bool = False

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    response: str
    todos: List[TodoItem]

class TodoCreate(BaseModel):
    text: str

class TodoResponse(BaseModel):
    id: str
    text: str
    created_at: datetime
    completed: bool
