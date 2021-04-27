from model import db, User, Post, connect_to_db
from werkzeug.security import generate_password_hash, check_password_hash

#USER#################################################################################

def create_user(user_name, user_email, user_password):
    """Create and return a new user."""

    user = User(user_email=user_email, 
                user_password=generate_password_hash(user_password, method='sha256'), 
                user_name=user_name)

    db.session.add(user)
    db.session.commit()

    return user

def find_user_by_email(email):
    """Find a user by their email address."""

    return User.query.filter(User.user_email == email).first()

def delete_user(userID):
    """Delete a user from the database."""

    user = User.query.get(userID)

    db.session.delete(user)
    db.session.commit()

    return

#POST#################################################################################

def create_post(user_id, post_date, post_name, post_comment, post_photo_link):
    """Create and return a new post."""

    post = Post(
        user_id=user_id,
        post_date=post_date,
        post_name=post_name,
        post_comment=post_comment,
        post_photo_link=post_photo_link)

    db.session.add(post)
    db.session.commit()

    return post

def get_post_by_id(id):
    """Find a post by post_id."""

    return Post.query.filter(Post.post_id == id).first()

def get_posts():
    """Return all posts."""

    return Post.query.all()

def delete_post(postID):
    """Delete a single post from the database."""

    post = Post.query.get(postID)

    db.session.delete(post)
    db.session.commit()

    return

def delete_all_posts_for_single_user(userID):
    """Delete all of the posts of a single user."""

    posts = Post.query.filter(Post.user_id == userID).all()

    for post in posts:
        db.session.delete(post)
        
    db.session.commit()

    return

def get_post_object(list_of_objects):
    result = {}
    for obj in list_of_objects:
        result[obj.post_id] = obj.post_name
    return result

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()