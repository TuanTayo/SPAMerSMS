import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;        \SPAMerSMS/        ;
		;---------------------------;
		; Author : TuanTayo         ;
		; Gmail  :                  ;
                ; cyber.tuantayo@gmail.com  ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam TRI
2. Spam Grab
3. Spam HooqTV
4. Spam OYOROOMS
""")
		pilih=int(input('/TuanTayo: '))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.grab
		elif pilih == 3:
			import src.hooq
		elif pilih == 4:
			import src.oyo
		elif pilih == 5:
			import src.oyo
		
	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
