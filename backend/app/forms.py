#This file is for specifying forms
from app import db_manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextField, validators
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField

#get all tags from the db
all_tags1 = db_manager.mongo.db.tags.find()
all_tags2 = db_manager.mongo.db.tags.find()
all_tags3 = db_manager.mongo.db.tags.find()
all_tags4 = db_manager.mongo.db.tags.find()
all_tags5 = db_manager.mongo.db.tags.find()
all_tags6 = db_manager.mongo.db.tags.find()
#get all tag parameters
#all_tag_params = db_manager.mongo.db.
#get all attributes
all_attirb = db_manager.mongo.db.attrib_options.find()

#login form
class LoginForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

#new entry form
class newEntryForm(FlaskForm):
    title = StringField('Title',[validators.DataRequired()])
    author = StringField('Author',[validators.DataRequired()])
    selection = SelectField('Add a tag', choices=[(tag['name'], tag['name']) for tag in all_tags1])
    submit = SubmitField('Save')

#add a tag form
class addTagForm(FlaskForm):
    selection = SelectField('Add a tag', choices=[(tag['name'], tag['name']) for tag in all_tags2])
    submit = SubmitField('Save')

#add an instance form
class addInstanceForm(FlaskForm):
    uuid = StringField('UUID')
    damage_report = TextField('Damage report')
    selection = SelectField('Add a tag', choices=[(tag['name'], tag['name']) for tag in all_tags3])
    submit = SubmitField('Save')

#create a tag form
class createTagForm(FlaskForm):
    name = StringField('Tag name', [validators.DataRequired()])
    #select_parent = SelectField('Select its parent tag', choices=[(tag['name'], tag['name']) for tag in all_tags4 ] )
    select_child = SelectField('Select its child tag', choices=[(tag['name'], tag['name']) for tag in all_tags5])
    #paramValue = StringField('Tag paramter value (corresponds with the parameter type above)')
    submit = SubmitField('Add')

#add tag's param form
class addTagParamForm(FlaskForm):
    paramType = SelectField('Tag parameter type', choices=[('integer', 'integer'), ('real number', 'real number'),('range(integer)', 'range(integer)'), ('range(real)', 'range(real)'), ('enumerated', 'enumerated'), ('string', 'string')])
    #These two need to be conditional
    min_value = StringField('Min value', [validators.regexp('^-?[0-9]\d*(\.\d+)?$')])
    max_value = StringField('Max value', [validators.regexp('^-?[0-9]\d*(\.\d+)?$')])
    #also conditional
    enumerate_values1 = StringField('Enumerate values')
    enumerate_values2 = StringField('Enumerate values')
    enumerate_values3 = StringField('Enumerate values')
    submit = SubmitField('Add parameter')

#add tag's implications form
class addTagImplForm(FlaskForm):
    select_child = SelectField('Select its child tag', choices=[(tag['name'], tag['name']) for tag in all_tags6])
    submit = SubmitField('Add implication rule')

#add attribute to an item form
class addAttribForm(FlaskForm):
    attrib_name = SelectField('Select an attribute', choices=[(attrib['attribute_name'], attrib['attribute_name']) for attrib in all_attirb])
    attrib_value = StringField('Attribute value')
    submit = SubmitField('Add')

#update attribute for an item form
class updateAttribForm(FlaskForm):
    attrib_value = StringField('New attribute value')
    submit = SubmitField('Update')

#create a new attribute
class createAttribForm(FlaskForm):
    attrib_name = StringField('New attribute name')
    attrib_type = SelectField('Select attribute type', choices=[('Single-line string', 'Single-line string'), ('Multi-line string', 'Multi-line string'), ('Integer', 'Integer')])
    submit = SubmitField('Create')