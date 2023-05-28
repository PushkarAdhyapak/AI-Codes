# Importing necessary libraries
import random
import nltk
from nltk.chat.util import Chat, reflections

# Defining responses as patterns and their corresponding responses
responses = [
    (r'hi|hello|hola|wassup|namaste', ['Hello! How can I help you with your college admission process?']),
    (r'what are the admission requirements|requirements|what documents should I submit', ['To get admission, you need to have a high school diploma or equivalent, as well as meet the minimum GPA and test score requirements.']),
    (r'how do I apply|application|Steps to apply', ['You can apply online on the college\'s website or by submitting a paper application to the admissions office.']),
    (r'when is the deadline|deadline', ['The deadline for admission applications is usually in the early spring for the fall semester, but it can vary by college.']),
    (r'what about financial aid|financial aid', ['Financial aid is available to eligible students. You can fill out the FAFSA to apply for federal financial aid, and the college may also have its own financial aid programs.']),
    (r'how do I contact the admissions office|contact', ['You can contact the admissions office by phone or email to get more information about the college\'s admission process.']),
    (r'bye|goodbye|exit|quit', ['Thank you for using the chatbot. Good luck with your admission process!']),
    (r'.*', ['I\'m sorry, I don\'t understand. Can you please ask me another question?'])
]

# Defining and starting the chatbot


def chatbot():
    print("Welcome to the college admission process chatbot! How can I assist you?")
    chat = Chat(responses, reflections)
    chat.converse()

# Starting the chatbot
chatbot()
