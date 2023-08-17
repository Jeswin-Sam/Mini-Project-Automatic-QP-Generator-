import firebase_admin
from firebase_admin import credentials, db, storage

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
        # /test/ECE/3rd Year/even/Subject 1/question_bank/part_A/Unit-1
        database_path = f'/test/{dept}/{year}/"even"/{subject}/question_bank/part_A/Unit-{unit}'
        
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


# initialize the Firebase app with your credentials
cred = credentials.Certificate('automatic-qp-generator-7d88c-firebase-adminsdk-r7dbq-2adaa3c8a5.json')


# initialize database and storage
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://automatic-qp-generator-7d88c-default-rtdb.firebaseio.com/',
    'storageBucket': 'automatic-qp-generator-7d88c.appspot.com'
    })


print(retrieve_part_a("ECE", "3rd Year", "Subject 1", "Unit-1"))