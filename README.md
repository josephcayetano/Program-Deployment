# Program Deployment
### Overview
This project focused on deploying a machine learning model to predict flight delays by building an API and packaging it with Docker for easy and reliable use.
### API Development & Containerization – FastAPI & Docker
-	Deployed the model as a REST API using FastAPI, with endpoints for health checks and predicting delays based on airport and schedule data
-	Wrote tests using pytest to check both correct and incorrect inputs, and added custom error messages for better user feedback
-	Used Docker to package the API and run it on port 8000, solving setup issues with Conda and improving error handling


### Files
1. README.md - A file describing other files in this repository.

2. D602 Task 3 Final.docx - A Word document file that contains the report for Task 3.

3. .gitlab-ci.yml - A YAML file that defined the pipeline stages, jobs, and scripts to automate testing, building and deploying the application.

4. Dockerfile - A file that was used to define the environment for containerizing the application.

5. Dockerfile_old - An older version of Dockerfile.

6. airport_encodings.json - A JSON file that contains encodings to airport data.

7. finalized_model.pkl - A PKL file that stores a trained model that can be loaded later for predictions.

8. app.py - A Python script file that serves as the main application for API.

9. test_app.py - A Python script file that serves as the testing script for app.py.

10. test_app_old.py - an older version of test_app.py

11. requirements.txt - A TXT file that contains all Python dependencies required by the project.
