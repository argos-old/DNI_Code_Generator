#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# DNI_Code_Generator is licensed under the:
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned
# on making available complete source code of licensed works
# and modifications, which include larger works using a licensed
# work, under the same license. Copyright and license notices
# must be preserved. Contributors provide an express grant of
# patent rights.
#
# For more information on this, and how to apply and follow the
# GNU GPL, see http://www.gnu.org/licenses
#
# Iván Rincón 2017


class HashFunctions:

    @staticmethod
    def hash_string(string):
        from string import ascii_uppercase
        if string.isalnum():
            weight = [7, 3, 1]
            hsh = 0
            for i in range(len(string)):
                c = list(string)[i]
                if c.isdigit():
                    hsh += int(c) * weight[i % 3]
                else:
                    hsh += list(ascii_uppercase).index(c.upper()) * weight[i % 3]
            return str(hsh % 10)
        else:
            return None

    def hash_is_ok(self, string, hsh_int):
        return True if self.hash_string(string) is hsh_int else False

    @staticmethod
    def hash_dni(dni_number_int):
        # TODO: to pass raise exception to StringCheckers class
        if dni_number_int > 99999999 or dni_number_int < 1:
            raise ValueError("Invalid value. The value must be an integer between 1 and 9999999")

        return "TRWAGMYFPDXBNJZSQVHLCKE"[dni_number_int % 23]

    def hash_dni_is_ok(self, full_dni_string):
        lnif = list(full_dni_string)
        letter = lnif.pop(len(full_dni_string) - 1)

        return True if self.hash_dni(int("".join(lnif))) is letter else False


class StringCheckers:
    @staticmethod
    def _check_date_string(value):
        try:
            from datetime import datetime
            datetime.strptime(value, "%y%m%d").strftime("%y%m%d")
        except ValueError:
            raise ValueError("String was not recognized as a valid date. It should be 'YYMMDD'", value)
        else:
            return value

    @staticmethod
    def _check_dni_serial_number_string(value):
        if len(value) == 9:
            from string import ascii_uppercase
            lvalue = list(value)
            for char in lvalue[:3]:
                if not char.upper() in ascii_uppercase:
                    lvalue.remove(char)
            for char in lvalue[3:]:
                if not char.isdigit():
                    lvalue.remove(char)
            if len(lvalue) == 9:
                return value.upper()
        raise ValueError("String was not recognized as a valid serial number. "
                         "It should be 3 ascii letters and 6 digits", value)

    @staticmethod
    def _check_nif_number(value, letter="", nie=""):
        if int(value) > (99999999 if nie is "" else 9999999):
            raise ValueError("Invalid value. The value must be an integer between 1 and 9999999", value)
        return nie, str(value).zfill(8 if nie is "" else 7), HashFunctions().hash_dni(value) if letter is "" else letter

    def _parser_full_nif_string(self, value):
        from string import ascii_letters
        lvalue = list(value)
        letter = ""
        nie = ""

        if lvalue[0].isalpha():
            nie = lvalue.pop(0).upper()
            if nie not in "XY":
                raise ValueError("String was not recognized as a valid NIF. "
                                 "It should start with a digit or, in case of NIE, 'X' or 'Y'", nie)

        if not lvalue[len(lvalue) - 1].isdigit():
            letter = lvalue.pop(len(value) - 1).upper()
            if letter not in ascii_letters:
                raise ValueError("String was not recognized as a valid NIF. "
                                 "It should end with a digit or a ASCII letter", letter)

        for n in lvalue:
            if not n.isdigit():
                raise ValueError("String was not recognized as a valid NIF. "
                                 "The DNI number should not contain letters inside", n)

        return "".join(self._check_nif_number(int("".join(lvalue)), letter, nie))
