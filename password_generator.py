'''
created by: @Aisha
'''
import random
import string

class Generator:

    def __init__(self, size):
        self.size = size


    def genPass(self):
        #create character pool
        string1 = string.ascii_uppercase
        string2 = string.ascii_lowercase
        digits = string.digits
        pounctuation = string.punctuation

        #create password from all character pool
        generated_pass = list(string1 + string2 +pounctuation + digits)
        random.shuffle(generated_pass)

        result = random.choices(generated_pass, k=self.size)
        return ''.join(result)  #return it as string


    def verify(self):

            if self.size < 8:
                print("Please use a size of 8 or greater")
            else:
                print(f"Your generated password is: {self.genPass()}")


user1 = Generator(int(input("this is a password generator \nPlease input the size of the password: ")))
user1.verify()





