from flask import Flask, jsonify, render_template, request, flash, session, redirect, url_for
from model import connect_to_db, User, Post
import crud
from datetime import datetime
from jinja2 import StrictUndefined
import cloudinary as Cloud
import cloudinary.uploader
import cloudinary.api
from APIconfig import APIsecret, SecretKey

app = Flask(__name__)
app.secret_key = SecretKey
app.jinja_env.undefined = StrictUndefined

cloudinary.config( 
  cloud_name = "knittr", 
  api_key = "163782255322919", 
  api_secret =  APIsecret
)


#Welcome####################################################################################################

@app.route('/')
def welcome_page():
    """Show the welcome/homepage."""

    return render_template('welcome.html')

#Login/Signup##########################################################################################

@app.route('/login')
def login_page():
    """View login page."""

    return render_template('login.html')

@app.route('/handle-login', methods=['POST'])
def handle_login():
    """Log the user into the application."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(user_email=email).first()

    if not user or not crud.check_password_hash(user.user_password, password):
        flash('Incorrect email/password.  Please try again')
        return redirect('/login')

    session['logged_in'] = True
    session['user_id'] = user.user_id
    session.modified = True
    
    flash(f'Logged in as {user.user_name}')    
    return redirect('/profile')

@app.route('/new-account', methods=['POST'])
def create_new_user():
    """Create/register a new user."""

    email = request.form.get('newemail')
    password = request.form.get('newpassword')
    username = request.form.get('newusername')

    user = crud.find_user_by_email(email)
    if user:
        flash('There is already an account with that email address.')
    else:
        crud.create_user(username, email, password)
        flash('Your account has been created!  Please log in.')

    return redirect('/login') 

#Photos###################################################################################################

@app.route('/photos')
def photos_page():
    """View photos page."""

    if session['logged_in'] == False:
        flash('Please login or create account.')
        return render_template('login.html')

    posts = crud.get_posts()

    return render_template('photos.html', posts=posts)

@app.route('/api/photos', methods=["POST"])
def upload_photo_post():
    """Upload a photo post."""

    post_name = request.form.get('post_name')
    post_comment = request.form.get('post_comment')
    img_url = request.form.get('img_url')

    now = datetime.now()

    post = crud.create_post(session['user_id'], now, post_name, post_comment, img_url)

    return jsonify({'status': 'ok'})

#Profile###################################################################################################

@app.route('/profile')
def profile_page():
    """View profile page."""

    if session['logged_in'] == True:
        user = User.query.filter_by(user_id=session['user_id']).first()
        return render_template('profile.html', user=user)
    
    flash('You must be logged in to see profile.')
    return redirect('/login')

@app.route('/api/posts', methods=['POST'])
def list_posts():
    """Retrieve and return posts associated with user."""

    all_user_posts = Post.query.filter(Post.user_id == session['user_id']).all()
    
    return jsonify(crud.get_post_object(all_user_posts))

@app.route('/delete/<post_id>', methods=['POST', 'GET'])
def ask_if_delete_post(post_id):
    """Show delete page for a selected post."""

    if session['logged_in'] == False:
        flash('Please login or create account.')
        return render_template('login.html')

    post = crud.get_post_by_id(post_id)
    session['to_delete'] = post.post_id
    session.modified = True

    return render_template('delete.html', post=post)

@app.route('/api/delete', methods=['POST'])
def delete_post():
    """Delete selected user post from database."""

    crud.delete_post(session['to_delete'])

    return jsonify({'message': 'Post destroyed!'})

#Logout###################################################################################################

@app.route('/logout')
def logout_page():
    """View logout page."""

    if session['logged_in'] == True:
        return render_template('logout.html')
    
    flash('You are not logged in.')
    return redirect('/login')

@app.route('/handle-logout', methods=['POST'])
def handle_logout():
    """Log the user out of the application."""

    session['logged_in'] = False
    session.modified = True

    return jsonify({'message': 'Successfully logged out!'}) 

@app.route('/api/accountdelete', methods=['POST'])
def delete_user_account():
    """Delete user account and related project records and posts from database."""

    crud.delete_all_posts_for_single_user(session['user_id'])
    crud.delete_user(session['user_id'])
    session['logged_in'] = False
    session.modified = True

    return jsonify({'message': 'Account destroyed!'})



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
    