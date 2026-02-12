from abc import ABC ,abstractmethod
import string
import random
class password_genarator_abstract(ABC):
    @abstractmethod
    def generate_password(self,length=8):
        pass

class numeric_password_genarteor(password_genarator_abstract):
    letters=string.digits
    def generate_password(self,length=8):
        return "".join(str(random.choice(self.letters))for _ in range(length))
class letter_password_generate(password_genarator_abstract):
    letters=string.ascii_letters
    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters)))
    
    generator=numeric_password_genarteor()
    print(generator.generate_password())
