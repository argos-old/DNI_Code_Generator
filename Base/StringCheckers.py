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

from Base.Functions import HashFunctions
from string import ascii_uppercase


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
            lvalue = list(value)
            for char in lvalue[:3]:
                if not char.upper() in ascii_uppercase:
                    lvalue.remove(char)
            for char in lvalue[3:]:
                if not char.isdigit():
                    lvalue.remove(char)
            if len(lvalue) == 9:
                return value.upper()
        raise ValueError("String was not recognized as a valid DNI serial number. "
                         "It should be 3 ascii letters and 6 digits", value)

    @staticmethod
    def _check_nie_serial_number_string(value):
        if len(value) == 9 and value[0].upper() == "E" and value[1:9].isdigit():
            return value.upper()
        raise ValueError("String was not recognized as a valid NIE serial number. "
                         "It should be 'E' and 8 digits", value)

    @staticmethod
    def _check_nif_number(value, nie=None):
        if int(value) > (99999999 if nie is None else 9999999):
            raise ValueError("Invalid value. The value must be an integer between 1 and 99999999", value)
        return value

    def _parser_full_nif_string(self, value):
        lvalue = list(value)
        letter = ""

        if not lvalue[0].isdigit():
            raise ValueError("String was not recognized as a valid NIF. "
                             "It should start with a digit", lvalue[0])

        if not lvalue[len(lvalue) - 1].isdigit():
            letter = lvalue.pop(len(value) - 1).upper()
            if letter.upper() not in ascii_uppercase:
                raise ValueError("String was not recognized as a valid NIF. "
                                 "It should end with a digit or a ASCII letter", letter)

        for n in lvalue:
            if not n.isdigit():
                raise ValueError("String was not recognized as a valid NIF. "
                                 "The DNI number should not contain letters inside", n)
        value = self._check_nif_number(int("".join(lvalue)))
        return str(value).zfill(8) + (HashFunctions().hash_dni(value) if letter is "" else letter)

    def _parser_full_nie_string(self, value):
        lvalue = list(value)
        letter = ""
        nie = lvalue.pop(0).upper()

        if nie not in "XYZ":
            raise ValueError("String was not recognized as a valid NIE. "
                             "It should start with 'X', 'Y' or 'Z'", nie)

        if not lvalue[len(lvalue) - 1].isdigit():
            letter = lvalue.pop(len(lvalue) - 1).upper()
            if letter not in ascii_uppercase:
                raise ValueError("String was not recognized as a valid NIE. "
                                 "It should end with a digit or a ASCII letter", letter)

        for n in lvalue:
            if not n.isdigit():
                raise ValueError("String was not recognized as a valid NIE. "
                                 "The NIE number should not contain letters inside", n)

        value = self._check_nif_number(int("".join(lvalue)), nie)
        value += 0 if nie == "X" else 10000000 if nie == "Y" else 20000000
        return str(value).zfill(8) + (HashFunctions().hash_dni(value) if letter is "" else letter)
