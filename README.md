# cookiecutter-simple-django

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for Django.  Based on work by [MarcoFucci](https://github.com/marcofucci/cookiecutter-simple-django/).

## Description

Lighter version of the Daniel Greenfeld's cookiecutter-django, but heavier than [Marco's](https://github.com/marcofucci/cookiecutter-simple-django/).

It uses the latest stable versions and it defines a skeleton which can be extended as needed.  Support for a custom bootstrap compilation, heroku push, and grunt workflow is included.

## Usage

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject` and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter to do all the work.

First, get cookiecutter. Trust me, it's awesome.

Set up your virtualenv:

    $ cd <your-envs-folder>
    $ virtualenv  --no-site-packages redditclone
    $ cd redditclone
    $ source bin/activate
    $ pip install cookiecutter

Now run it against this repo:

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/bwarren2/cookiecutter-simple-django.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.  It prompts you for questions; answer them.

If you are using cookiecutter < 0.7 and you answered *no* to *with_documentation*, you might want to delete the `docs`
folder.  From version 0.7+, that folder is automatically deleted for you.

Create the database `redditclone` and then set up your project:

    $ cd redditclone/
    $ ls
    $ pip install -r requirements/local.txt
    $ python ./manage.py syncdb
    $ python ./manage.py migrate
    $ python ./manage.py runserver

and load localhost:8000/admin

Create a GitHub repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:(you)/redditclone.git
    $ git push -u origin master

*Note*: The `requirements` files don't define any package versions because it makes more sense for you to use the latest ones when you set up your
project. After that point though, you really want to take note of the specific
versions installed so that they are not going to get updated without you knowing it.

In order to do this, just activate your virtual environment, pip freeze it and
update your requirements files:

    $ activate <your-envs-folder>/redditclone/bin/activate
    $ pip freeze
    $ # now open requirements/* and note down the versions used.

There are some non-python project extensions here implemented by bwarren2:

## Extensions

### Env vars
From the directory with manage.py in it, the below will expose settings vars.

    export DJANGO_SETTINGS_MODULE='zzz.settings.local'
    export PYTHONPATH=`pwd`

Add a database with

    export DATABASE_URL=<url>

### Grunt Pipeline
The grunt asset pipeline relies on node.

1. `npm init`
2. (Fill details)
3. `npm install  grunt grunt-concat-css grunt-contrib-concat grunt-contrib-cssmin grunt-contrib-less grunt-contrib-uglify grunt-contrib-watch jit-grunt load-grunt-config time-grunt  --save-dev`
4. Set "private": true in the package.json to avoid accidental publication.

### Bower statics

1. `npm install bower`
1. `bower init`
2. (Fill details)
3. `bower install bootstrap jquery`


### Grunting

Run `grunt css` and `grunt js` to get an initial compilation of bootstrap up.  Just `grunt` will monitor files for changes and recompile.  When you want to add more css and js to you project, just loop it into the grunt/ files.

### Test

Check it out with `django-admin runserver`!

### Pushing to Heroku

1. `heroku create (repo_name)` (or else ou must fix ALLOWED_HOSTS)
2. `heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python`
3. `git push heroku master`
4. (Config env vars)
(4a.
 * `heroku config:set PYTHONPATH=$PYTHONPATH:'/app/appname/'`
 * `heroku config:set DJANGO_SETTINGS_MODULE='appname.settings.production'`
 For email of errors:
 * `heroku config:set EMAIL_HOST_PASSWORD=(pass)`
 * `heroku config:set EMAIL_HOST_USER=(user)`
)

### Overall

Stringing this all together, you might get a command list like:

    cookiecutter cookiecutter-simple-django/
    # Project named barfoo

    export DATABASE_URL=(postgres url)
    # This is important because of the pwd
    cd barfoo/barfoo/
    export DJANGO_SETTINGS_MODULE='barfoo.settings.local'
    export PYTHONPATH=`pwd`
    export SECRET_KEY=mahsecret
    cd ..

    # Get grunt and bootstrap up
    npm init
    npm install  grunt grunt-concat-css grunt-contrib-concat grunt-contrib-cssmin grunt-contrib-less grunt-contrib-uglify grunt-contrib-watch jit-grunt load-grunt-config time-grunt  --save-dev
    npm install bower --save-dev
    bower init
    bower install bootstrap jquery
    grunt css
    grunt js

    # Test
    django-admin runserver
    git init
    git aa
    git ci -m "Initial commit"

    # Config heroku
    heroku create barfoo
    heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python
    heroku config:set DJANGO_SETTINGS_MODULE='barfoo.settings.production'
    heroku config:set PYTHONPATH=$PYTHONPATH:'/app/barfoo/'
    heroku config:set SECRET_KEY='(mysecretkey)'
    heroku config:set EMAIL_HOST_PASSWORD=(pass)
    heroku config:set EMAIL_HOST_USER=(email)

    git push heroku master
    heroku logs -t -p web

## Structure

The structure used should look quite familiar:

### Requirements

The `requirements` folder contains a requirements file for each environment.

If you need to add a dependency please choose the right file.

### Settings

The `settings` folder contains a settings file for each environment and the `local` settings should be gitignored.

If you take a look at `base.py`, you'll see that it includes the optional module `local.py` in the same folder. There you can override the local values and gitignore will exclude it from your commits.

The `testing.py` module is loaded automatically after `base.py` and `local.py` every time you run `python ./manage.py test`.

### Apps

The `apps` folder should contain all your local django apps, this is to keep
the structure of the project clean.

When it's time to `python ./manage.py startapp <name>`, just move the generated
module to `apps`. If you want to know why this works, just take a look at the line:

    sys.path.insert(0, root('apps'))

in `settings/base.py`.


# Done!

Now, it's time to write the code!!!


# Not Exactly What You Want?

This is what I want. *It might not be what you want.* Don't worry, you have options:

## Fork This

If you have differences in your preferred setup, I encourage you to fork this to create your own version.

If branch this repo into something new, I encourage you to submit it to the following places:

* [cookiecutter](https://github.com/audreyr/cookiecutter) so it gets listed in the README as a template.
* The [cookiecutter grid](https://www.djangopackages.com/grids/g/cookiecutter/) on Django Packages.

## Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they make my own project development experience better.

## Upcoming

I might add a skeleton for the Celery side of a project.
