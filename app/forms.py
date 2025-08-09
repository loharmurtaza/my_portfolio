from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional, URL, NumberRange
from app.models import User, SkillCategory

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Send Message')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=200)])
    content = TextAreaField('Content', validators=[DataRequired()])
    excerpt = TextAreaField('Excerpt', validators=[Length(max=300)])
    published = BooleanField('Publish')
    submit = SubmitField('Save Post')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class SiteSettingsForm(FlaskForm):
    hero_name = StringField('Hero Name', validators=[Optional(), Length(max=120)])
    hero_title = StringField('Hero Title', validators=[Optional(), Length(max=200)])
    about_html = TextAreaField('About HTML', validators=[Optional()])
    email = StringField('Public Email', validators=[Optional(), Email()])
    github_url = StringField('GitHub URL', validators=[Optional(), URL()])
    linkedin_url = StringField('LinkedIn URL', validators=[Optional(), URL()])
    twitter_url = StringField('Twitter/X URL', validators=[Optional(), URL()])
    submit = SubmitField('Save Settings')

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[DataRequired()])
    technologies = StringField('Technologies (comma-separated)', validators=[Optional(), Length(max=500)])
    github_url = StringField('GitHub URL', validators=[Optional(), URL()])
    live_url = StringField('Live URL', validators=[Optional(), URL()])
    image = StringField('Image filename (optional)', validators=[Optional(), Length(max=255)])
    submit = SubmitField('Save Project')

class SkillCategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Save Category')

class SkillForm(FlaskForm):
    name = StringField('Skill', validators=[DataRequired(), Length(max=120)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save Skill')

    def set_category_choices(self):
        self.category_id.choices = [(c.id, c.name) for c in SkillCategory.query.order_by(SkillCategory.name).all()]

class PublicationForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=300)])
    authors = StringField('Authors', validators=[Optional(), Length(max=500)])
    venue = StringField('Venue/Journal', validators=[Optional(), Length(max=200)])
    year = IntegerField('Year', validators=[Optional(), NumberRange(min=1900, max=2100)])
    status = StringField('Status', validators=[Optional(), Length(max=100)])
    link = StringField('Link', validators=[Optional(), URL()])
    submit = SubmitField('Save Publication')
