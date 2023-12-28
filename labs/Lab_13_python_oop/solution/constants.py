import os


CLIENTS = open(os.path.join(os.getcwd(), '..\clients.json'), 'r', encoding='utf-8')
PAYMENTS = open(os.path.join(os.getcwd(), '..\payments.json'), 'r', encoding='utf-8')