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
            return hsh % 10
        else:
            return None

    def hash_is_ok(self, string, hsh_int):
        return True if self.hash_string(string) is hsh_int else False

    @staticmethod
    def hash_dni(dni_number_int):

        if dni_number_int > 99999999 or dni_number_int < 1:
            raise ValueError("Invalid value. The value must be an integer between 1 and 9999999")

        return "TRWAGMYFPDXBNJZSQVHLCKE"[dni_number_int % 23]

    def hash_dni_is_ok(self, full_dni_string):
        lnif = list(full_dni_string)
        letter = lnif.pop(len(full_dni_string) - 1)

        return True if self.hash_dni(int("".join(lnif))) is letter else False

