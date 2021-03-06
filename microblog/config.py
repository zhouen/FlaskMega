"""
The WTF_CSRF_ENABLED setting activates the cross-site request forgery prevention (note that this setting is enabled by default in current versions of Flask-WTF). In most cases you want to have this option enabled as it makes your app more secure.

The SECRET_KEY setting is only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form. When you write your own apps make sure to set the secret key to something that is difficult to guess.
"""
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'



"""
In practice, we will find that a lot of people don't even know that they already have a few OpenIDs. It isn't that well known that a number of major service providers on the Internet support OpenID authentication for their members. For example, if you have an account with Google, you have an OpenID with them. Likewise with Yahoo, AOL, Flickr and many other providers. (Update: Google is shutting down their OpenID service on April 15 2015).

To make it easier for users to login to our site with one of these commonly available OpenIDs, we will add links to a short list of them, so that the user does not have to type the OpenID by hand.
"""
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/people/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


import os
basedir = os.path.abspath(os.path.dirname(__file__))
"""
The SQLALCHEMY_DATABASE_URI is required by the Flask-SQLAlchemy extension. This is the path of our database file.
The SQLALCHEMY_MIGRATE_REPO is the folder where we will store the SQLAlchemy-migrate data files.
"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

"""
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
"""
SQLALCHEMY_TRACK_MODIFICATIONS = True


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = 'zhouen.nathan'
MAIL_PASSWORD = 'ZhEn1981@810904ZE'

# administrator list
ADMINS = ['zhouen.nathan@gmail.com']
