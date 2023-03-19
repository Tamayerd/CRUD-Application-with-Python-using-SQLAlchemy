from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#SqlALchemy ve Python arasındaki ilişkiyi kuruyoruz.
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#ORM ve veri tabanı arasındaki ilişki kurulur.
connection = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/tamay/OneDrive/Masaüstü/SqlAlchemy/school.db'
engine = create_engine(connection, echo=True) #echo bak
session =sessionmaker()

Base=declarative_base()
db = SQLAlchemy(app)

app.app_context().push()


class  Student(db.Model) :
   
   __tablename__ = "School Table"
   
   id = Column( 'student_id' , db.Integer, primary_key = True ) 
   name = Column(String(100) , nullable = False) #name değeri boş kalamaz
   student_class = Column(String(4), nullable = False)
   teacher_name = Column(String(25),nullable=False)  
   student_not = Column(String(4))

   def __repr__(self):
         return f"<User name={self.name} student_class = {self.student_class} teachername = {self.teacher_name} student_not = {self.student_not} >"

#tabloyu oluşturmak için son adım terminale yazılabilir.
# from app import db
# db.create_all()
# exit()
