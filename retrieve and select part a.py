import firebase_admin
from firebase_admin import credentials, db, storage
import random
from docxtpl import DocxTemplate

# initialize the Firebase app with your credentials
cred = credentials.Certificate('automatic-qp-generator-7d88c-firebase-adminsdk-r7dbq-2adaa3c8a5.json')
# initialize database and storage
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://automatic-qp-generator-7d88c-default-rtdb.firebaseio.com/',
    'storageBucket': 'automatic-qp-generator-7d88c.appspot.com'
    })

current_sem = 'even'

dept = 'CSE'
year = '3rd year'
subject = 'Distributed Systems'
unit = 'Unit-1'
database_path = f'/test/{dept}/{year}/{current_sem}/{subject}/question_bank/part_a/{unit}'

# get a reference to the database
ref = db.reference(database_path)

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
                        question = value['question'])
    
    all_questions.append(question)


no_of_questions = 9
    
# randomly select 3 questions
part_a_selected_questions = random.sample(all_questions, no_of_questions)

part_a_context = {}
for i in range(1,no_of_questions + 1):
    part_a_context[f'a{i}_question'] = part_a_selected_questions[i-1].question
    part_a_context[f'a{i}_bloom'] = part_a_selected_questions[i-1].bloom
    part_a_context[f'a{i}_map'] = part_a_selected_questions[i-1].map
    

# question paper details
department = 'COMPUTER SCIENCE'
iat_no = '2'
date = '20.04.2023'
year = "III"
subject_code = 'CS8601'
subject_name = 'Distributed Systems'
semester = 'VI'
set_no = '1'

details_context = {'department': department,
                   'iat_no': iat_no,
                   'date': date,
                   'year': year,
                   'subject_code': subject_code,
                   'subject_name': subject_name,
                   'semester': semester,
                   'set_no': set_no}

total_context = details_context | part_a_context  
    
doc = DocxTemplate('qp_format.docx')
doc.render(total_context)

filename = f'ZZZ {subject_code} IAT-{iat_no} Set-{set_no}.docx'
doc.save(filename)


bucket = storage.bucket()

# specify file path and upload to storage
blob = bucket.blob(filename)
blob.upload_from_filename(filename)

print("Question paper generated successfully!")