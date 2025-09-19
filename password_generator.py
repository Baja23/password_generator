import string
import secrets

class Password:
    def __init__ (self, total_chars = 0, digits = 0, uppercase = False, special_chars = False): #zastanów się nad sensem wszystkich atrybutów, zwłaszcza letters i lowercase
        self.total_chars = total_chars 
        self.digits = digits 
        self.uppercase = uppercase
        self.special_chars = special_chars 

    def get_total_chars_number_from_user(self):
        while True:
            user_answer = input('How many characters in total should your password contain? (Please type a digit)')
            try:
                self.total_chars = int(user_answer)
                break
            except ValueError:
                print('Please type a digit') 
        
    def get_digits_number_from_user(self):
        while True:
            user_answer = input('How many digits should your password contain? (Please type a digit)')
            try:
                self.digits = int(user_answer)
                if self.digits > self.total_chars:
                    print(f'The number of digits cannot be greater than the total number of characters ({self.total_chars}).')
                else:
                    break
            except ValueError:
                print('Please type a digit')
        
    def get_uppercase_choice(self):
        while True:
            user_answer = input('Should your password contain any uppercase letters? (Please type true or false)')
            self.uppercase = user_answer.lower()
            if self.uppercase == 'true' or self.uppercase == 't':
                break
            elif self.uppercase == 'false' or self.uppercase == 'f':
                break
            else:
                print('Please type either true or false')          
        
    def get_special_char_choice(self):
        while True:
            user_answer = input('Should your password contain any special characters? (Please type true or false)')
            self.special_chars = user_answer.lower()
            if self.special_chars == 'true' or self.special_chars == 't':
                break
            elif self.special_chars == 'false' or self.special_chars == 'f':
                break
            else:
                print('Please type either true or false')  
    def generate_password(self):
        alphabet = string.ascii_lowercase
        if self.digits > 0:
            alphabet += string.digits
        if self.uppercase == 't' or self.uppercase == 'true': 
            alphabet += string.ascii_uppercase
        if self.special_chars == 't' or self.special_chars == 'true':
            alphabet += string.punctuation
        while True: 
            password = ''.join(secrets.choice(alphabet) for i in range(self.total_chars))
            if (any(c.islower() for c in password)) and any(c.isupper() for c in password) and any(c in string.punctuation for c in password) and sum(c.isdigit() for c in password) >= self.digits:
                break
        return password
def get_password_requirements_from_user(password):
    password.get_total_chars_number_from_user()
    password.get_digits_number_from_user()
    password.get_uppercase_choice()
    password.get_special_char_choice()

def main():
    password1 = Password()
    get_password_requirements_from_user(password1)
    print(f'Password requirements:\n'
          f'Total characters number: {password1.total_chars}\n'
          f'Number of digits: {password1.digits}\n'
          f'Any uppercase: {password1.uppercase}\n'
          f'Any special characters: {password1.special_chars}')
    print(f'Your new password is: {password1.generate_password()}')
    input("Press any key to exit ")

main()