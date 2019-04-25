# smile-widget-code-challenge

The Smile Widget Company currently sells two types of smile widgets: a Big Widget and a Small Widget.  We'd like to add more flexibility to our product pricing.

## Setup with Docker
1. Install Docker (https://docs.docker.com/install/)
2. Clone this repository.
3. `>>> docker-compose up --build`

## Setup without Docker
1. Install Python (>3.4)
2. Install postgres.  By default the Django app will connect to the database named 'postgres'.  See `settings.DATABASES`.
3. Clone this repository.
4. Install requirements.
  * `>>> pip install -r requirements.txt`
5. Run migrations.
  * `>>> python manage.py migrate`
6. Load data from fixtures:
  * `>>> python manage.py loaddata 0001_fixtures.json`

### Technical Requirements
* We currently have to products with the following prices:
    * Big Widget - $1000
    * Small Widget - $99
* These products, along with existing gift cards are already setup in the database.  Study the existing models and initial data.
* Create a new ProductPrice model and setup the following price schedule:    
  * Black Friday Prices (November 23, 24, & 25)
    * Big Widget - $800
    * Small Widget - FREE!
  * 2019 Prices (starting January 1, 2019)
    * Big Widget - $1200
    * Small Widget - $125
* Build a JSON API endpoint that accepts a product code, date, and (optional) gift card and returns product price.
  * The endpoint should live at `api/get-price` and accept the following parameters:
    * `"productCode"`
    * `"date"`
    * `"giftCardCode"`
* Update this README file with instructions on how to run and access your price calculator.
* Create a pull request with your changes.

### Additional Information
* Please use Django Rest Framework or a Python web framework of your choice to create the endpoint.
* Just as a general guideline, we've designed this exercise to take less than 4 hours.


## Updating readme with run/access instrction

 ### Directory of C:\Users\Deepankar\Downloads\Smile Widget\smile-widget-code-challenge

    04/24/2019  09:49 PM    <DIR>          .
    04/24/2019  09:49 PM    <DIR>          ..
    04/24/2019  09:38 PM                53 .dockerignore
    04/24/2019  09:38 PM               538 .gitignore
    04/24/2019  09:38 PM               290 docker-compose.yml
    04/24/2019  09:38 PM               440 Dockerfile
    04/24/2019  09:38 PM             1,920 README.md
    04/24/2019  09:38 PM                46 requirements.txt
    04/24/2019  09:43 PM    <DIR>          smilewidgets
    04/24/2019  09:38 PM               423 startup-script.sh
    04/24/2019  09:49 PM    <DIR>          venv_smile
                   7 File(s)          3,710 bytes
                   4 Dir(s)  414,580,178,944 bytes free

- install virtual env (here 'venv_smile') inside the cloned git  directory
- use the requirements.txt file to get benchmarked version using pip install
- activate the Virtual Env (use 'venv_smile/Scripts/activate')

- open the project file (here 'smilewidgets') review the code in Pycharm(any IDE).
 - cd smilewidgets
 - python manage.py runserver
 - Open Browser

### open url	" http://127.0.0.1:8000/api/get_price "

### please find attached screenshot in the Screenshot Folder

[Browser Screenshot](/Browser.png)
[pycharm Screenshot](/pycharm.png)


