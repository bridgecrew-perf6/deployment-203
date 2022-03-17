# deployment
sudo apt install git
git clone git@github.com:jainpawan/informds.git
setup virtual environment Linux: sudo apt-get install virtualenv Mac: chsh -s /bin/bash sudo easy_install pip pip install virtualenv OR brew install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt (ubuntu)

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
  Configuring Google APIs
  Go to Dashboard, create a New Project
  Register App at OAuth Consent Screen
  Create New API Credentials
  Add social app in Django admin
