import pandas as pd
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    SelectField,
    SubmitField,
    TextAreaField,
    IntegerField,
    DateField,
    TimeField
)


# Getting the data
train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField("Airline", 
                          choices=X_data.airline.unique(),
                          validators=[DataRequired()])
    doj = DateField("Date of Journey", validators=[DataRequired()])
    source = SelectField("Source", choices=X_data.source.unique(), validators=[DataRequired()])
    destination = SelectField("Destination", choices=X_data.destination.unique(), validators=[DataRequired()])
    total_stops = IntegerField("Stops",  validators=[DataRequired()])
    arrival_time = TimeField("Arrival Time", validators=[DataRequired()])
    departure_time = TimeField("Departure Time", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    additional_info = SelectField(
        label="Additional Info",
        choices=X_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )
    
    submit = SubmitField("Submit", validators=[DataRequired()], render_kw={"class": "btn btn-primary btn-block"})