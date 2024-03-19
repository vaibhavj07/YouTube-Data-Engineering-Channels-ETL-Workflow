# YouTube-Data-Engineering-Channels-ETL-Workflow

## Project Overview
This project demonstrates an end-to-end data engineering pipeline that extracts data from the YouTube API, focusing on channels related to data engineering. The pipeline utilizes Python and Airflow for data processing and is deployed on AWS EC2, with the processed data stored in Amazon S3.

## Technologies Used
- Python
- Apache Airflow
- AWS EC2
- Amazon S3
- YouTube API

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them:
- Python 3.x
- Apache Airflow
- AWS CLI
- `google-api-python-client` library

**Clone the repository**:
git clone https://github.com/yourusername/youtube-data-engineering-project.git ```

### Install required Python libraries from requirements.txt

### Note
- Modify the dag_foler path to point to where the python files are stored in airflow.cfg
dags_folder = /path/to/youtube-data-engineering-project
- use airflow standalone to start the server
- Open the web UI on port 8080
