from DNI.DNIeCodeGenerator import *
from DNI.NIEHashGenerator import NIEHashGenerator


class NIECodeGenerator(DNICodeGenerator, NIEHashGenerator):
    def __init__(self,
                 serial_number_string,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string,
                 sex_string="M",
                 nationality_string="ESP",
                 country_code_string="ESP",
                 document_type_string="IX"):
        NIEHashGenerator.__init__(self,
                                  serial_number_string,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string)
        DNICodeGenerator.__init__(self,
                                  full_dni_string,
                                  birth_date_string,
                                  expiration_date_string,
                                  sex_string,
                                  nationality_string,
                                  country_code_string,
                                  document_type_string)

    def line1_code_generator(self):
        return (self.document_type +
                self.country_code +
                self.serial_number().ljust(10, "<") +
                self.serial_number_hash() +
                self.full_dni()).ljust(30, "<")


xxx = NIECodeGenerator("E07275385", "X7665889", "800220", "110509", "M", "AUT")
print(xxx)