#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	firstName = name.split('-')[0]
	
	return 'Bonjour, ' + firstName.lower().capitalize()

def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd’hui, j’ai vu un {animals[random.randrange(0, len(animals))]} s’emparer d’un panier {adjectives[random.randrange(0, len(adjectives))]} plein de {fruits[random.randrange(0, len(fruits))]}."

def encrypt(text, shift):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	res = ''

	for i in text:
		if i.upper() in alphabet:
			res += alphabet[(alphabet.index(i.upper()) + shift) % len(alphabet)].upper()
		else:
			res += i


	return res

def decrypt(encrypted_text, shift):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	res = ''

	for i in encrypted_text:
		if i.upper() in alphabet:
			res += alphabet[(alphabet.index(i.upper()) - shift) % len(alphabet)].upper()
		else:
			res += i


	return res


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
