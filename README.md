# deployment
step1. sudo apt install git
step2 .git clone git@github.com:jainpawan/informds.git
step3. setup virtual environment Linux: sudo apt-get install virtualenv Mac: chsh -s /bin/bash sudo easy_install pip pip install virtualenv OR brew install virtualenv
step4. virtualenv venv
step5. source venv/bin/activate
step6. pip install -r requirements.txt (ubuntu)

For deployment on Heroku (you can refer https://medium.com/@shashankmohabia/deploying-a-django-app-to-heroku-using-github-repository-319c04a11c1a for detail)
Step 1. Install dependencies:-
Step 2. Create required files:-
  requirements.txt:
  runtime.txt
  Procfile
Step 3. Update settings.py:-
step 4. Push to GitHub:
Heroku Side Setup:-
Step 1. Create a Heroku app:-
Step 2. Add python build pack:
Step 3. Link your GitHub repository:-
Step 4. Deploy:

Follow the steps for signup using google auth (you can refer https://dev.to/mdrhmn/django-google-authentication-using-django-allauth-18f8 for detail)
  step1. Configuring Google APIs
  step2. Go to Dashboard, create a New Project
  step3. Register App at OAuth Consent Screen
  step4. Create New API Credentials
  step5 .Add social app in Django admin
