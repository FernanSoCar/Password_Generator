import os
import random
import string
import PySimpleGUI as sg


class PasswordGenerator:
    def __init__(self):
        sg.theme('DarkAmber')
        layout = [
            [sg.Text('Site/Software', font=('Helvetica', 15), size=(14, 1)), 
             sg.Input(key='site', font=('Helvetica', 15), size=(20, 1))],
            [sg.Text('Email/Username', font=('Helvetica', 15), size=(14, 1)),
             sg.Input(key='email', font=('Helvetica', 15), size=(20, 1))],
            [sg.Text('Password Length', font=('Helvetica', 15), size=(14, 1)),
             sg.Input(key='total_chars', font=('Helvetica', 15), size=(20, 1))],
            [sg.Output(size=(34, 5) , font=('Helvetica', 15))],
            [sg.Button('Generate Password')]
        ]

        self.window = sg.Window('Password Generator',  layout, icon='internet_lock_locked_padlock_password_secure_security_icon_127100.ico')
      

    def start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Generate Password':
                site = values['site']
                email = values['email']
                total_chars = int(values['total_chars'])
                password = self.generate_password(total_chars)
                self.save_password(site, email, password)
                print(f'Site/Software: {site}')
                print(f'Email/Username: {email}')
                print(f'Generated Password: {password}')


    def generate_password(self, total_chars):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(total_chars))
        return password
    

    def save_password(self, site, email, password):
        with open('passwords.txt', 'a') as file:
            file.write(f'Site/Software: {site}\n')
            file.write(f'Email/Username: {email}\n')
            file.write(f'Generated Password: {password}\n\n')


if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.start()