# Movie Recommender App

## Description

This is a Content based Movie Recommender System App. Dataset taken from Kaggle TMDB 5000 Movies dataset. The model developed is `Cosine Distance Similarity` Matrix.

## Deployed on AWS EC2 [Live Demo](http://ec2-3-111-188-53.ap-south-1.compute.amazonaws.com:8501/)

## Setup & Run Application [Linux]

- Run `bash app_setup.sh` from terminal
- It will create the virtual env and will install required packages from `requirements.txt`
- Then activate the virtual environment `source env/bin/activate`
- Finally, run `python3 -m streamlit run app.py` to start the application, it will automatically start the web app in a new tab of your default browser.

## Setup & Run Application [Windows]

- Create a virtual environment from Command Prompt (CMD) `python3 -m venv env`
- Activate the virtual env using `CALL env\Scripts\activate` command and install all required packages using `pip install -r requirements.txt`
- Finally, run `python3 -m streamlit run app.py` to start the application, it will automatically start the web app in a new tab of your default browser.

## Folder Structure

- **`archive` :** This folder contains the TMDB 5000 Movies Dataset
- **`model` :** This is the folder where the model is developed
- **`recommender_model.ipynb` :** Python notebook for the model generation. After running this entire notebook, two new files will be created inside the same folder (`model` folder) - (1) `moviesdict.pkl`, and (2) `simimat.pkl`
- **`moviesdict.pkl` :** The final dataframe (as a dictionary) used in the model
- **`simimat.pkl` :** This is the main model, which is a Similarity Matrix about cosine distance of each movie with each another movie
- **`app_setup.sh` :** File to setup virtual environment
- **`app.py` :** Main Python Application File (Streamlit App)

```md

├── archive
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── model
│   ├── recommender_model.ipynb
│   ├── moviesdict.pkl
│   └── simimat.pkl
├── app_setup.sh
├── app.py
├── requirements.txt
├── readme.md
└── .gitignore

```

A special thanks to Nitish Singh Sir (CampusX YouTube) for the concept of this project.
