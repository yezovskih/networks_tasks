class Mail():

    def __init__(self):
        self.mailFrom = input("From: ")
        self.mailTo = None
        self.message = None
        self.subj = None

    def ask_mail_to(self):
        self.mailTo = input("To: ")

    def ask_message(self):
        self.message = input("Message: ")

    def ask_subject(self):
        self.subj = input("Subject: ")

    def create(self):
        self.ask_mail_to()
        self.ask_subject()
        self.ask_message()
