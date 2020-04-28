# Install instructions

## Download the repository
`Download or clone` the repository for you from the [main page](https://github.com/StrappedGlint13/fridge-follower).

## Install Python requirements
Install all the Python-project requirements:`pip install -r requirements.txt`. Do this on current virtual environment. In addition, you also need install pip and python. 

## Install venv
Install virtual environment venv to your root directory: `python3 -m venv venv`.

## Run MyFridge locally
To run the project, use command `source venv/bin/activate` in the root directory. Then Run `python3 run.py`. Then the app will open automatically in the browser.

## Install MyFridge in Heroku
To run the project in Heroku, lets start installing driver[psycopg2](https://www.psycopg.org/) as a tool for PostgreSQL-database management `pip install psycopg2`.

Second step is make a Procfile: `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`

Then we need to update our requirements (Heroku is using these to load dependencies): `pip freeze | grep -v pkg-resources > requirements.txt`.

Next step is make a environment variable to Heroku and add a database:

- `heroku config:set HEROKU=1`
- `heroku addons:add heroku-postgresql:hobby-dev`

Last steps are make your file as git-project with `git init`-command. Then create your app `heroku create <app name>`. Then `git remote add heroku https://git.heroku.com/<nimi>.git`, `git add .`, `git commit -m "Application to Heroku"` and `git push heroku master`. 

Now the app should be available and ready to use in Heroku. 

