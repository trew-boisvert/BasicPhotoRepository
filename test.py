""" Exploratory Testing
List of Features:
    Navbar
        Test that buttons redirect to appropriate pages
    Sign up for account
        Input type:
            Username - text box
                What happens when users enter nothing?
            Password - password box
                What happens when users enter nothing?
            Email - email box
                What happens when users enter something that is not an email address?
                What happens when users enter nothing?
            Button - click
                What happens on click with partially or incorrectly filled form?
        Check database for new entry
        Check entry matches info added
    Login to account
        Input type:
            Email - email box
            Password - password box
            Button - click
        Check login works for existing account
        Check login fails for non-existent account
    View Profile
        Check profile displayed matches account logged into
    Upload Photo to board
        Input type:
            Name of post - text box
            Comment on post - text box
            Choose File button - file selection on click
            Upload - submit on click
        Check database for new entry
        Check discussion board to see if photo is displayed
        Check user profile to see if post is displayed with a delete option
    Delete photo posts from profile
        Input type:
            Button - click
        Check that entry is removed from database
        Check that photo is removed from discussion board
        Check that post is removed from profile
    Logout from account
        Input type:
            Button - click
        Check that profile is unaccessible
        Check that user still exists in database
    Delete user account
        Input type:
            Button - click
        Check that user account is no longer in database
        Check that pages only viewable by a user are unaccessible

"""
