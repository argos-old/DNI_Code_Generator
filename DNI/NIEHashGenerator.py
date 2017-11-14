from DNI.DNIeHashGenerator import DNIeHashGenerator


class NIEHashGenerator(DNIeHashGenerator):
    def __init__(self,
                 serial_number_string,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string):
        DNIeHashGenerator.__init__(self,
                                   serial_number_string,
                                   full_dni_string,
                                   birth_date_string,
                                   expiration_date_string)
        self._serial_number = serial_number_string
        self._full_nie = full_dni_string

    def serial_number(self):
        return self._check_nie_serial_number_string(self._serial_number)

    def full_dni(self):
        return self._parser_full_nie_string(self._full_nie)
