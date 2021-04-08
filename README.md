========================================================================
## TO RUN:
You will first need to install Python and Django by following the install instructions below. Note that the bottom of
this page are the basic Django commands that we will need in the future.
python3 manage.py runserver

#### the current url to hit this project is 

http://127.0.0.1:8000<br>
OR since 127.0.0.1 is localhost:<br>
http://localhost:8000

### Admin Panel

http://127.0.0.1:8000/admin/<br>
OR<br>
http://localhost:8000/admin/<br>
username: admin<br>
password: admin

========================================================================

## Git Commands

### Get the status of your branch
git status

### See all branches
git branch

see all branches including everyone in the group

git branch -a

If for some reason all branches are not showing up just do a:<br>
git fetch --all

### Create a new branch

git checkout <branch_you_want_to_branch_from><br>
git branch <name_your_branch><br>
git checkout <branch_you_just_made>

or do it all at once with:

git checkout <branch_you_want_to_branch_from><br>
git checkout -b <name_your_branch><br>
you will now be on your new branch you created.

### Checkout a branch

git checkout <name_of_branch>

### Push your code to your branch

git status //this is just to see all the files you have added or modified<br>
git add <the_file(s)_you_have_added_or_modified><br>
git commit -m 'the message of what you have added or changed'<br>
git push

### Pull master 

git checkout master<br>
git pull

### Merge master into your branch

git checkout <your_branch_name><br>
git merge master

## After your branch has been merged into master, clean up our branches by doing the following

### delete branch remotely

git push origin --delete <remote_branch_name>

### delete branch locally

git branch -d <local_branch_name>

========================================================================

### install python:
Go to python.org and click the downloads button. Download version 3.8.4
Go ahead and install python, IF YOU ARE ON WINDOWS you will see a checkbox at the bottom of the install window that
says "add python to path" just make sure that box is checked. Mac users will not see this option. follow the install
instructions. After you are finished installing:

windows users may need to reboot at this point, mac users do not

open terminal or command prompt and type:

python3 --version

you should see Python 3.8.4. That will verify installation was successful.

========================================================================
### install django on mac:
open terminal and type:

sudo easy_install pip
pip3 install django==2.2

## Django commands that are run in terminal:

#### Start a server-
You can start your local server simply by typing either in the pycharm terminal, or in your terminal in the root folder<br>
for the project.<br>
python3 manage.py runserver


#### Create a new app-
python3 manage.py startapp name_of_app<br>
OR<br>
django-admin startapp users


#### To create a db table OR Update a table
Any time you make a change to, or add a model you will need to migrate that change with the following commands:<br>
python3 manage.py makemigrations “name_of_app”<br>
python3 manage.py sqlmigrate “name_of_app” “number_of_migration”<br>
python3 manage.py migrate


#### Admin Panel
python3 manage.py createsuperuser

#### Libraries to Install
pip install django-crispy-forms
pip install django-autoslug
pip install pillow