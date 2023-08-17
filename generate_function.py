import firebase_admin
from firebase_admin import credentials, db, storage
import random
from docxtpl import DocxTemplate
import os


# class for question object
class Question:
    def __init__(self, bloom, map, question, marks=None):
        self.bloom = bloom
        self.map = map
        self.question = question
        self.marks = marks
        
        
# to retrieve the part a questions from database and return a list of all the questions
def retrieve_part_a(dept, year, subject, iat_no):
    
    if (iat_no == 1):
        units_for_iat = [1,2]
    elif (iat_no == 2):
        units_for_iat = [3,4]
    else:
        units_for_iat = [5]
        
    # iterate over the units for the particluar iat
    for unit in units_for_iat:
        database_path = f'/test/{dept}/{year}/even/{subject}/question_bank/part_A/Unit-{unit}'
        
        # get a reference to the database
        ref = db.reference(database_path)

        # retrieve the data as a dictionary
        part_a_questions_dict = ref.get()
        
        
    # list containing all part A questions
    part_a_questions = []

    # create question objects from dictionary and add them to the list
    for key, value in part_a_questions_dict.items():
        question = Question(bloom = value['bloom'],
                            map = value['map'],
                            question = value['question'])
        
        part_a_questions.append(question)
        
    return part_a_questions


# to retrieve the part b questions from database and return a list of all the questions
def retrieve_part_b(dept, year, subject, iat_no):
    
    if (iat_no == 1):
        units_for_iat = [1,2]
    elif (iat_no == 2):
        units_for_iat = [3,4]
    else:
        units_for_iat = [5]
        
    # iterate over the units for the particluar iat
    for unit in units_for_iat:
        database_path = f'/test/{dept}/{year}/even/{subject}/question_bank/part_B/Unit-{unit}'
        
        # get a reference to the database
        ref = db.reference(database_path)

        # retrieve the data as a dictionary
        part_b_questions_dict = ref.get()
        
        
    # list containing all part A questions
    part_b_questions = []

    # create question objects from dictionary and add them to the list
    for key, value in part_b_questions_dict.items():
        question = Question(bloom = value['bloom'],
                            map = value['map'],
                            question = value['question'],
                            marks= value['marks'])
        
        part_b_questions.append(question)
        
    return part_b_questions


# to randomly select questions and return the selected questions context
def select_questions(part_a_questions, part_b_questions):
    
    no_of_part_a_questions = 9
    no_of_part_b_questions = 4 #with choices
    
    
    # randomly select part A questions
    part_a_selected_questions = random.sample(part_a_questions, no_of_part_a_questions)

    # render part A context
    part_a_context = {}
    for i in range(1, no_of_part_a_questions + 1):
        part_a_context[f'a{i}_question'] = part_a_selected_questions[i-1].question
        part_a_context[f'a{i}_bloom'] = part_a_selected_questions[i-1].bloom
        part_a_context[f'a{i}_map'] = part_a_selected_questions[i-1].map
        
        
    # randomly select part B questions
    part_b_selected_questions = random.sample(part_b_questions, no_of_part_b_questions)

    # render part B context
    part_b_context = {}
    for i in range(1,no_of_part_b_questions + 1):
        part_b_context[f'b{i}_question'] = part_b_selected_questions[i-1].question
        part_b_context[f'b{i}_bloom'] = part_b_selected_questions[i-1].bloom
        part_b_context[f'b{i}_map'] = part_b_selected_questions[i-1].map
        

    questions_context = part_a_context | part_b_context  
    return questions_context


def render_question_paper(dept, iat_no, date, year, subject_name, questions_context):
    # question paper details
    department = dept
    subject_code = 'CS8601'
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
    
    total_context = questions_context | details_context

    doc = DocxTemplate('qp_format.docx')
    doc.render(total_context)

    filename = f'{subject_name} IAT-{iat_no} Question Paper.docx'
    doc.save(filename)


    bucket = storage.bucket()

    # specify file path and upload to storage
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    
    # move the file to desktop
    os.rename(filename, os.path.join("C:\\Users\\Admin\\Desktop", filename))
    
    
def generate_and_save_question_paper(dept, year, subject, iat_no, date):
    
    # retrieve part A and part B questions from database
    part_a_questions = retrieve_part_a(dept, year, subject, iat_no)
    part_b_questions = retrieve_part_b(dept, year, subject, iat_no)
    
    questions_context = select_questions(part_a_questions, part_b_questions)
    
    render_question_paper (dept, iat_no, date, year, subject, questions_context)
    

# initialize the Firebase app with your credentials
cred = credentials.Certificate('automatic-qp-generator-7d88c-firebase-adminsdk-r7dbq-2adaa3c8a5.json')


# initialize database and storage
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://automatic-qp-generator-7d88c-default-rtdb.firebaseio.com/',
    'storageBucket': 'automatic-qp-generator-7d88c.appspot.com'
    })