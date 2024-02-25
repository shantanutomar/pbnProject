# Patient management system backend in python using Django framework

The project is backend for patient management system. It is built in python using Django framework. 
The backend allows the user to manage patients. The user can add, edit, delete and view patients.
For the database, postgres is used.
The UI is available
[here](https://github.com/shantanutomar/pbn-patients-ui)

## Initial postgres setup
1. Install postgres using the following command:
   ```
   brew install postgres
   ```
2. Start the postgres server using the following command:
   ```
   brew services start postgres
   ```
3. Once postgres is running locally, create a database and owner using the following command:
   ```
   CREATE database practice_data;

   CREATE USER practice_rw WITH PASSWORD 'password';

   GRANT ALL PRIVILEGES ON DATABASE practice_data TO practice_rw;
   ```

4. The application will connect to the database using the following credentials:
   ```
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'practice_data',
         'USER': 'practice_rw',
         'PASSWORD': 'password',
         'HOST': 'localhost',
         'PORT': '',
         }
    }
   ```
5. Make sure the database is running on the default port 5432. If not, update the port in the settings.py file.

## Setting up virtual environment and installing dependencies

1. Clone the [repository](https://github.com/shantanutomar/pbnProject)
2. Make sure you have pyenv to install the python version. If not, install it using the following command:
   ```
   brew install pyenv
   
   Update the .zshrc file with the following:
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   ```
3. Set the python version to 3.8.12 using the following command:
   ```
   pyenv install 3.8.5
   pyenv global 3.8.5
   ```
4. Now navigate to the cloned project directory and create a virtual environment using the following command:
   ```
   python -m venv pbnProjectEnv
   ```
5. Activate the virtual environment using the following command:
   ```
   source pbnProjectEnv/bin/activate
   ```
6. Once environment is activated, install the following dependencies using the commands. The dependencies will be 
installed in the virtual env.
   ```
    pip install django==1.11.17
    pip install SQLAlchemy==1.3.17
    pip install alembic==0.9.9
    pip install psycopg2-binary==2.9.1
    pip install djangorestframework==3.8.2
    pip install django-cors-headers==3.2.1

   ```
7. Once the dependencies are installed, navigate to the app directory:
    ```
    cd patients/
    ```
8. Run the following command to start the server:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running postgres migration using alembic

1. Once the database is setup, navigate to the app directory:
    ```
    cd patients/
    ```
2. The alembic.ini file is already present in the app directory and also the migration file is present.
    ```
    54141d4c44d5_create_patients_table.py
    ```
3. Run the following command to run the migration:
    ```
    alembic upgrade head
    ```
4. The migration will create the patients table in the database.

## Running the server
1. Once the database is setup and the migration is run, navigate to the app directory:
    ```
    cd patients/
    ```
2. Run the following command to start the server:
    ```
    python manage.py runserver
    ```

3. The server will be running on the local server. The application will be available at the following URL:
   ```
   http://localhost:8000
   ```

## Future enhancements
1. I am using python and Django after a long time. It took me sometime to go over the documentation and understand different packages that I have installed. Given the time, the application can be improved a lot in terms of features.
1. The list endpoint can be enhanced with pagination and search params to search the patients.
2. I am not sure how to do this in python yet, but I would like to segregate the API response with database models. Right now I am using
    the same model with serialize for the API response. Probably I would like to have a separate model for the API response. 
The API response can have field names that are different from the database model and more inclined with the frontend.

