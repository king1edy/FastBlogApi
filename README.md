Blog Api with Authentication using FastApi nad postgres DB

###################
# To re-create the virtual enviroment
pyhton -m venv venv
# To activate the virtual environment
venv\Scripts\activate
# Run the server locally using uvicorn with hot reload
uvicorn main:app --reload