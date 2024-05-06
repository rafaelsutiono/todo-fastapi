from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI()

class ToDo(BaseModel):
    title: str
    description: str
    completed: bool = False

class UpdateTodo(BaseModel):
    title: Optional[str] = None
    description: Optional[int] = None
    completed: Optional[bool] = None

todos = {
    1: {
        "title": "BANGUNNN",
        "desc": "bangun woi jgn snooze",
        "completed": "False"
    }
}

@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = """
    <html>
        <head>
            <title>To-Do List API</title>
            <link href='https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&display=swap' rel="stylesheet">
            <style>
                body {
                    background-color: black;
                    background-image: url(https://i.pinimg.com/originals/c0/36/28/c03628e7339e0d492cdd077acb6a9e8f.gif);
                    color:white;
                    overflow: hidden;
                    font-family: 'Arimo';
                }
                .container {
                    text-align: center;
                    background: #cdcbcb;
                    opacity: 0.7;
                    padding: 2%;
                    width: fit-content;
                    margin-left: auto;
                    margin-right: auto;
                    margin-top: 20%;
                    max-height: 80vh;
                    overflow-y: auto;
                    box-shadow: 0px 5px 7px rgb(27, 27, 27);
                    border-radius: 5px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>To-Do List with FastAPI</h1>
                <p>by Rafael Sutiono</p>
            </div>
        </body>
    </html>
    """
    return html_content

# get todo by ID
@app.get("/todo/{id}")
def get_todo(id: int = Path(...,description="Retrieve the ID of the todo you want to view", gt=0)):
    if id not in todos:
        return {"Error": "invalid todo ID"}
    return todos[id]

# get todo by title
@app.get("/todo/{title}")
def get_todo_title(title: str = Path(...,description="Retrieve the title of the todo you want to view")):
    for id in todos:
        if todos[id]["title"] == title:
            return todos[id]
    return {"Error": "Todo not found"}

# get all completed or incompleted todos
@app.get("/todo/completed")
def get_completed_todos():
    completed_todos = [todos[id] for id in todos if todos[id].completed]
    if not completed_todos:
        return {"Message": "You have no completed todos"}
    return completed_todos
    
# get all incompleted todos
@app.get("/todo/incompleted")
def get_incompleted_todos():
    incompleted_todos = [todos[id] for id in todos if not todos[id].completed]
    if not incompleted_todos:
        return {"Message": "You have no incompleted todos"}
    return incompleted_todos

# post a todo
@app.post("/todo/post/{id}")
def post_todo(id: int, todo: ToDo):
    if id in todos:
        return{"Error": "Todo already exists"}
    
    todos[id] = todo
    return todos[id]

# update a todo
@app.put("/todo/update/{id}")
def update_todo(id: int, todo: ToDo):
    if id not in todos:
        return{"Error": "Todo does not exist"}
    
    if todo.title != None:
        todos[id]["title"] = ToDo.title
    if todo.description != None:
        todos[id]["description"] = ToDo.description
    if todo.completed != None:
        todos[id]["completed"] = ToDo.completed

    return todos[id]

# delete a todo
@app.delete("/todo/delete/{id}")
def delete_todo(id: int):
    if id not in todos:
        return {"Error": "Todo does not exist"}
    
    del todos[id]
    return {"Message": "Todo deleted successfully"}

# delete all todos
@app.delete("/todo/delete-all")
def delete_all_todos():
    todos.clear()
    return {"Message": "All todos deleted successfully."}