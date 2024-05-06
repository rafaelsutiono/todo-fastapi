  <td>**Endpoint**

   </td>
   <td>**Method**

   </td>
   <td>**Description**

   </td>
   <td>**Request Body**

   </td>
   <td>**Response Body**

   </td>
   <td>/

   </td>
   <td>GET

   </td>
   <td>Returns a welcome message

   </td>
   <td>
   </td>
   <td>    &lt;html>

        &lt;head>

            &lt;title>To-Do List API&lt;/title>

            &lt;link href='https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&display=swap' rel="stylesheet">

            &lt;style>

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

            &lt;/style>

        &lt;/head>

        &lt;body>

            &lt;div class="container">

                &lt;h1>To-Do List with FastAPI&lt;/h1>

                &lt;p>by Rafael Sutiono&lt;/p>

            &lt;/div>

        &lt;/body>

    &lt;/html>

   </td>
   <td>/todo/{id}

   </td>
   <td>GET

   </td>
   <td>Retrieve the ID of the todo you want to view

   </td>
   <td>
   </td>
   <td>{

  "title": title,

  "desc": description,

  "completed": true or false

}

**OR**

{"Error": "invalid todo ID"}

   </td>
   <td>/todo/{title}

   </td>
   <td>GET

   </td>
   <td>Retrieve the title of the todo you want to view

   </td>
   <td>
   </td>
   <td>{

  "title": title,

  "desc": description,

  "completed": true or false

}

OR

{"Error": "Todo not found"}

   </td>
   <td>/todo/completed

   </td>
   <td>GET

   </td>
   <td>Retrieve all completed todos

   </td>
   <td>
   </td>
   <td>{

  "title": title,

  "desc": description,

  "completed": True

}

**OR**

{"Message": "You have no completed todos"}

   </td>
   <td>/todo/incompleted

   </td>
   <td>GET

   </td>
   <td>Retrieve all incompleted todos

   </td>
   <td>
   </td>
   <td>{

  "title": title,

  "desc": description,

  "completed": False

}

**OR**

{"Message": "You have no incompleted todos"}

   </td>
   <td>/todo/post/{id}

   </td>
   <td>POST

   </td>
   <td>Create a todo

   </td>
   <td>{

  "title": "string",

  "description": "string",

  "completed": false

}

   </td>
   <td>{

  "title": "string",

  "description": "string",

  "completed": false

}

**OR**

{"Error": "Todo already exists"}

   </td>
   <td>/todo/update/{id}

   </td>
   <td>PUT

   </td>
   <td>Update a todo

   </td>
   <td>Edit at least 1 field

{

  "title": "string",

  "description": "string",

  "completed": false

}

   </td>
   <td>{

  "title": "string",

  "description": "string",

  "completed": false

}

**OR**

{"Error": "Todo does not exist"}

   </td>
   <td>/todo/delete/{id}

   </td>
   <td>DELETE

   </td>
   <td>Delete a todo

   </td>
   <td>
   </td>
   <td>{

  "Message": "Todo deleted successfully"

}

   </td>
   <td>/todo/delete-all

   </td>
   <td>DELETE

   </td>
   <td>Delete all todos

   </td>
   <td>
   </td>
   <td>{

  "Message": "All todos deleted successfully."

}

   </td>
