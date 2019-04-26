import email
import imaplib


class ReadMail:
    def __init__(self):
        self.ORG_EMAIL = ""
        self.EMAIL_USERNAME = ""
        self.EMAIL_PWD = ""
        self.SUBJECT = ""
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self.email_body = "r"
        self.get_mail_configurations()

    def get_mail_configurations(self):
        self.ORG_EMAIL = 'gmail'
        # self.EMAIL_USERNAME = 'k.narendra234@gmail.com' #+ self.ORG_EMAIL
        # self.EMAIL_PWD = 'gma@nani.760'
        self.EMAIL_USERNAME = 'narendra.kommoju@ggktech.com' #+ self.ORG_EMAIL
        self.EMAIL_PWD = 'ggk@nani_731'

    def read_mail_from_gmail_imap(self):
        try:
            print("Trying to login,", self.ORG_EMAIL, self.EMAIL_USERNAME, self.EMAIL_PWD
                  , self.SUBJECT)
            self.imap.login(self.EMAIL_USERNAME, self.EMAIL_PWD)
        except imaplib.IMAP4.error:
            print("LOGIN FAILED!!! ")
            # ... exit or deal with failure...

        # Set the email box to open one of the mailboxes/labels
        rv, data = self.imap.select("INBOX")

        if rv == 'OK':
            print("Processing mailbox...\n")
            self.process_mailbox(self.imap)
            self.imap.close()
        self.imap.logout()

    def process_mailbox(self, imap):
        # Searching for UNSEEN mails
        status, data = imap.search(None, '(UNSEEN)')
        for mailID in data[0].split():
            status, data = imap.fetch(mailID, '(RFC822)')
            if status != 'OK':
                print("ERROR getting message", mailID)
                return

            # Parse the actual message data from fetch() using 'email' module which returns data in dictionary
            msg = email.message_from_string(str(data[0][1].decode('utf-8')))

            # print('msg', msg['Subject'], msg)
            if msg['Subject']:
                self.email_body = msg.get_payload()

                print("The body of the email is:\n", self.email_body)


if __name__ == '__main__':
    # while True:
    re = ReadMail()
    re.read_mail_from_gmail_imap()