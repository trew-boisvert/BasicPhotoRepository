# Fam's Out, Cam's Out!

## Table of Contents

* [Summary](#summary)
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#setup)
* [About the Developer](#developer)

## <a name="summary"></a>Summary
**Fam's Out, Cam's Out!** is a basic photo repository.  It allows users to create an account and upload photos. 

## <a name="tech-stack"></a>Tech Stack
__Front End:__ HTML5, Jinja2, CSS, JavaScript, AJAX, jQuery, Bootstrap<br/>
__Back End:__ Python, Flask, PostgreSQL, SQLAlchemy <br/>

## <a name="features"></a>Features

Create and Log in to an account.

Upload photos to the photo/discussion board.

Log out from or delete your account.  Fam's Out, Cam's Out! respects your right to be forgotten!

## <a name="setup"></a>Setup/Installation

#### Requirements:

- Python 3.6.8
- PostgreSQL

To run this app on your local computer, follow these steps:

Clone repository:
```
$ git clone https://github.com/trew-boisvert/ShopifyDevInternChallenge.git
```

Create a virtual environment:
```
$ virtualenv env
```

Activate the virtual environment:
```
$ source env/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

To run Flask you need to set a secret key. Create a 'secrets.sh' file in the project directory and add a key.

Add the key to your environmental variables (do this each time you restart your virtual environment):
```
$ source secrets.sh
```

Create database 'pics':
```
$ createdb pics
```

Create your database tables:
```
$ python3 model.py
```

Run app from the command line:
```
$ python3 server.py
```

Visit localhost:5000 on your browser.

## <a name="developer"></a>About the Developer

Trew Boisvert (they/them) has a background in fashion and textiles.  They enjoy solving puzzles, be it the logic puzzles inherent in programming, or the mathmatical puzzle of creating clothing patterns.  You can learn more about them on their <a href="https://www.linkedin.com/in/trew-boisvert-a78309a1/">LinkedIn.</a>
