|Endpoint         |Method|Description                                    |Request Body                                                                               |Response Body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|------|-----------------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|/                |GET   |Returns a welcome message                      |                                                                                           |<html>  <head>  <title>To-Do List API</title>  <link href='https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&display=swap' rel="stylesheet">  <style>  body {  background-color: black;  background-image: url(https://i.pinimg.com/originals/c0/36/28/c03628e7339e0d492cdd077acb6a9e8f.gif);  color:white;  overflow: hidden;  font-family: 'Arimo';  }  .container {  text-align: center;  background: #cdcbcb;  opacity: 0.7;  padding: 2%;  width: fit-content;  margin-left: auto;  margin-right: auto;  margin-top: 20%;  max-height: 80vh;  overflow-y: auto;  box-shadow: 0px 5px 7px rgb(27, 27, 27);  border-radius: 5px;  }  h1 {  color: #333;  }  p {  color: #666;  }  </style>  </head>  <body>  <div class="container">  <h1>To-Do List with FastAPI</h1>  <p>by Rafael Sutiono</p>  </div>  </body>  </html>|
|/todo/{id}       |GET   |Retrieve the ID of the todo you want to view   |                                                                                           |{  "title": title,  "desc": description,  "completed": true or false } OR {"Error": "invalid todo ID"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|/todo/{title}    |GET   |Retrieve the title of the todo you want to view|                                                                                           |{  "title": title,  "desc": description,  "completed": true or false } OR {"Error": "Todo not found"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|/todo/completed  |GET   |Retrieve all completed todos                   |                                                                                           |{  "title": title,  "desc": description,  "completed": True } OR {"Message": "You have no completed todos"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|/todo/incompleted|GET   |Retrieve all incompleted todos                 |                                                                                           |{  "title": title,  "desc": description,  "completed": False } OR {"Message": "You have no incompleted todos"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|/todo/post/{id}  |POST  |Create a todo                                  |{  "title": "string",  "description": "string",  "completed": false }                      |{  "title": "string",  "description": "string",  "completed": false } OR {"Error": "Todo already exists"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|/todo/update/{id}|PUT   |Update a todo                                  |Edit at least 1 field {  "title": "string",  "description": "string",  "completed": false }|{  "title": "string",  "description": "string",  "completed": false } OR {"Error": "Todo does not exist"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|/todo/delete/{id}|DELETE|Delete a todo                                  |                                                                                           |{  "Message": "Todo deleted successfully" }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|/todo/delete-all |DELETE|Delete all todos                               |                                                                                           |{  "Message": "All todos deleted successfully." }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

