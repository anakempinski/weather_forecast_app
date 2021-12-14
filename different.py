# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
#
# # SQLite
#
# #create a model (what we're going to save to db)
# class Forecast(db.Model):
#     id = db.column(db.Integer, primary_key = True)
#     date = db.Column(db.String, nullable=True)
#     location = db.Column(db.String(50), unique=True)
#     temperature = db.Column(db.String(50))
#     humidity = db.Column(db.String(50))
#     wind_direction = db.Column(db.String(50))
#
#     def __inti__(self, date, location, temperature, humidity, wind_direction):
#         self.date = date
#         self.location = location
#         self.temperature = temperature
#         self.humidity = humidity
#         self.wind_direction = wind_direction
#
#     def __repr__(self):
#         return f"Weather conditions in {self.location} for {self.date}: \n" \
#                f"temperature {self.temperature} \n" \
#                f"humitity "
#
#
# # Users is going to inherit from db.Model, which provides it certain functionality
# class Users(db.Model):
#
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50), unique=True)
#     psw = db.Column(db.String(50), nullable=True)  # nullable=True -- field shouldn't be empty
#     date = db.Column(db.DateTime, default=datetime.utcnow)  # datetime.utcnow - current date
#
#
#     # how we're going to print user (for our conviniency only)
#     # self - current object, and we can get its attributes
#     def __repr__(self):
#         return f"<users {self.id}>"
#
#
#
# class Profiles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     old = db.Column(db.Integer)
#     city = db.Column(db.String(100))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def __repr__(self):
#         return f"profiles {self.id}>"
#
#
# @app.route("/register", methods=("POST", "GET"))
# def register():
#     return render_template("register.html", title="Registration")
#
#
# # 'page2.html' template will be uploaded as the answer to request "/index"
# #  html template should be located in templates package
# @app.route('/index')
# def index():
#     return render_template('page2.html', title='Main page', menu=menu)
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html', title='About Flask')
#
#
#
#
#
# #menu = ['apple', 'orange', 'lemon']
#
# # # '/'  -- main page of web site
# # @app.route('/')
# # def hello_world():
# #     return 'Hello World!'
# #