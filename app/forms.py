from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(('Username'), validators=[DataRequired()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    remember_me = BooleanField(('Remember Me'))
    submit = SubmitField(('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(('Username'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(('Password'), validators=[DataRequired()])
    password2 = PasswordField(('Repeat Password'), validators=[DataRequired(),
                                                               EqualTo('password')])
    submit = SubmitField(('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        ('Repeat Password'), validators=[DataRequired(),
                                         EqualTo('password')])
    submit = SubmitField(('Request Password Reset'))


class EditProfileForm(FlaskForm):
    u_pict = FileField(('User Picture'))
    username = StringField(('Username'), validators=[DataRequired()])
    email = StringField(('Email'), validators=[DataRequired(), Email()])
    about_me = TextAreaField(('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    p1 = TextAreaField(('Project'), validators=[DataRequired()])
    p2 = TextAreaField(('Progress'), validators=[DataRequired()])
    p3 = TextAreaField(('Problem'), validators=[DataRequired()])
    p4 = TextAreaField(('Plan'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))


class EditPostForm(FlaskForm):
    p1new = TextAreaField(('Project'), validators=[DataRequired()])
    p2new = TextAreaField(('Progress'), validators=[DataRequired()])
    p3new = TextAreaField(('Problem'), validators=[DataRequired()])
    p4new = TextAreaField(('Plan'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

    def __init__(self, original_posts, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.original_posts = original_posts
