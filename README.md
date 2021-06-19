# UfaberProj-TaskMgmt

This is a project which was provided by Ufaber for creating a simple Task Management web application.
This project is divided into 2 parts, where the backend is developed using Django Rest Framework and frontend in Django Templates using HTML/Css and Bootstrap (Frontend yet to be implemented).

## Requirements
- Python 3.9.0
- virtualenv

- Clone the project using `git clone https://github.com/kaulashish/UfaberProj-TaskMgmt/`
- Create virtual environment `virtualenv <env-name> --python=python3.9.0`
- Install the required dependencies for the project from the requirements.txt file.
`pip install -r requirements.txt`
- Activate virtual environment

## Backend

The backend is developed using Django Rest Framework and uses the following main tables that is mentioned in `project/models.py` file.
- Project
- Task
- Subtask

The backend consists of the following API's

### User
- #### Login: 
  Takes in the username and password and gives a token as response. POST request
  
  `localhost:8000/api/user/login`

- #### Register: 
  Takes in username, password, password2, first_name, last_name as inputs and gives out token as response. POST request
  
  `localhost:8000/api/user/register`

### Project
- #### Create Project: 
  Takes in name, description and image for the project to be created. POST request.
  
  `localhost:8000/api/project/create`

- #### List Project: 
  Lists the projects along with the tasks and subtasks associated with it. GET request.
  
  `localhost:8000/api/project/list`

- #### Project Detail: 
  Provides the detail of the particular project with tasks and subtasks associated with it. GET method.
  
  `localhost:8000/api/project/<int:pk>`

- #### Update Project: 
  Provides functionality to update the project. PUT/PATCH request method.
  
  `localhost:8000/api/project/<int:pk>/update`

- #### Delete Project: 
  Deletes the project. DELETE request method
  
  `localhost:8000/api/project/<int:pk>/delete`

### Task
- #### Create Task:
  Creates a new task. Takes name, description, start_data, end_date and assignee as input. One can provide multiple assignees by just providing the same key 'assignee'. POST method.
  
  `localhost:8000/api/project/<int:pk>/task/create`
  
- #### List Task:
  Lists the tasks for the specified project. GET method
  
  `localhost:8000/api/project/<int:pk>/task/list`
  
- #### Update Task:
  Updates the task. For assignee. If the assignee exists, it will deassign him or vice versa. PUT method
  
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/update`
  
- #### Delete Task:
  Deletes the task. DELETE method
  
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/delete`
  
### Subtask

- #### Create subtask:
  Creates a new subtask for the associated task. Takes in name, description, start_date, end_date and assignee as input. One can provide multiple assignees by just providing the same key 'assignee'. POST method.
  
  `Note`: The assignee must be mentioned in the task assignee. 
  
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/subtask/create`
  
- #### List subtask:
  Lists the subtasks associated with the project task provided in url. GET method
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/subtask/list`
  
- #### Update subtask:
  Updates the subtasks. If the assignee exists, it will deassign him or vice versa. PUT method
  
  `Note`: The assignee must be mentioned in the task assignee. 
  
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/subtask/<int:pk>/update`
  
- #### Delete subtask:
  Deletes the subtask. DELETE method
  
  `localhost:8000/api/project/<int:pk>/task/<int:pk>/subtask/<int:pk>/delete`
