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

from Functions import HashFunctions


class DNIHashGenerator(HashFunctions):
    def __init__(self,
                 full_dni_string,
                 birth_date_string,
                 expiration_date_string):

        self.full_dni = full_dni_string.upper()
        self.birth_date = birth_date_string
        self.expiration_date = expiration_date_string

        self.__full_dni_hash = str(self.hash_string(self.full_dni))
        self.__birth_date_hash = str(self.hash_string(self.birth_date))
        self.__expiration_date_hash = str(self.hash_string(self.expiration_date))
        self.__final_hash = str(self.hash_string(self.full_dni +
                                                 self.full_dni_hash() +
                                                 self.birth_date +
                                                 self.birth_date_hash() +
                                                 self.expiration_date +
                                                 self.expiration_date_hash()))

    def __str__(self):
        return self.full_dni + " " + \
               self.full_dni_hash() + " " + \
               self.birth_date + " " + \
               self.birth_date_hash() + " " + \
               self.expiration_date + " " + \
               self.expiration_date_hash() + " " + \
               self.final_hash()

    def full_dni_hash(self):
        return self.__full_dni_hash

    def birth_date_hash(self):
        return self.__birth_date_hash

    def expiration_date_hash(self):
        return self.__expiration_date_hash

    def final_hash(self):
        return self.__final_hash
