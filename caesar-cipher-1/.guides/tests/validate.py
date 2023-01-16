#!/usr/bin/env python3
import random

def validate():
	try:
		import caesar
	except ImportError:
		print("Could not import homework file 'caesar.py'")
		raise ImportError("Could not import homework file 'caesar.py'")

	required_methods = ["encrypt","decrypt"]
	for m in required_methods:
		if m not in dir(caesar):
			print( "%s not defined"%m )
			return 0

	num_tests = 5
	num_passed = 0
	LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(num_tests):
			print("=========== Running test %d ==========="%(i+1))
			key = random.SystemRandom().randint(0,25)
			plaintext = "".join( [random.SystemRandom().choice(LETTERS) for _ in range(32)] )
			try:
				ciphertext = caesar.encrypt(key,plaintext)
			except Exception as e:
				print( f"ERROR: encrypt({key},{plaintext})failed" )
				continue
			print( "SUCCESS: encrypt ran without errors" )
			try:
				decryption = caesar.decrypt(key,ciphertext)
			except Exception as e:
				print( f"ERROR: decrypt({key},{ciphertext}) failed" )
				continue
			print( "SUCCESS: decrypt ran without errors" )
			if plaintext == decryption:
				print( "SUCCESS: Decryption correctly inverted encryption" )
				num_passed = num_passed + 1
			else:
				print( "ERROR: Decryption failed" )
				print( f"plaintext = {plaintext}" )
				print( f"decryption = {decryption}" )
	
	keys = [8,11]
	plaintexts = ["SATOSHI","NAKAMOTO"]
	ciphertexts = ["AIBWAPQ","YLVLXZEZ"]

	for key,plaintext,ciphertext in zip(keys,plaintexts,ciphertexts):
			try:
				student_ciphertext= caesar.encrypt(key,plaintext)
			except Exception as e:
				print( f"ERROR: encrypt({key},{plaintext})failed" )
				continue
			if student_ciphertext == ciphertext:
				print( f"Success: correctly encrypted {plaintext}" )
			else:
				print( f"ERROR: encrypt({key},{plaintext}) = {student_ciphertext} (Expected: {ciphertext})" )
		

if __name__ == "__main__":
	validate()
