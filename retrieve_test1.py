import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initialize the Firebase app with your credentials
cred = credentials.Certificate('automatic-qp-generator-7d88c-firebase-adminsdk-r7dbq-2adaa3c8a5.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://automatic-qp-generator-7d88c-default-rtdb.firebaseio.com/'})

# get a reference to the database
ref = db.reference('/test/part_b')

# retrieve the data as a dictionary
all_questions_dict = ref.get()


# class for question object
class Question:
    def __init__(self, bloom, map, question, marks=None):
        self.bloom = bloom
        self.map = map
        self.question = question
        self.marks = marks


# list containing all questions
all_questions = []


# create question objects from dictionary and add them to the list
for key, value in all_questions_dict.items():
    question = Question(bloom = value['bloom'],
                        map = value['map'],
                        question = value['question'], 
                        marks = value['marks'])
    all_questions.append(question)