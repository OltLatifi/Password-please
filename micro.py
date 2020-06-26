import random
import string
import sqlite3
import secrets
from tkinter import *


class passwordStorer:
	def __init__(self):
		self.some_strings = ['q','qw','ol','g','h','J','L','A','a','V']
		self.password = ''
		self.platforma = ''
		self.passw_to_edit = ''
		self.connect = sqlite3.connect('passw.db', isolation_level=None)
		self.cursor = self.connect.cursor()
		self.code = False
		self.please = False

		self.listboxi = []



	# creates the same frame evrytime we need a blank page
	def make_frame(self):
		self.frm = Frame(self.root)
		self.frm.place(x=0, y=0, width = 500, height=250)
	def username_exists(self):
		self.make_frame()
		Label(text = 'This username already exists, change it to continue.').place(x=120, y = 100)
		btn = Button(self.frm, text = 'Go back!', command = self.sign_up_gui)
		btn.place(x=120,y=130, width = 275)

	def sign_up(self):

		emri = self.emri_ent.get()
		mbiemri = self.mbiemri_ent.get()
		username = self.username_ent.get()
		passwordd = self.password_ent_s.get()

		# if the username already exists
		self.cursor.execute("""SELECT username, password FROM users;""")
		self.userat = self.cursor.fetchall()
		print(self.userat)
		
		if username in self.userat[0][0]:
			self.username_exists()
		else:
			self.cursor.execute(" INSERT INTO users VALUES(null,?,?,?,?)", (emri, mbiemri,username, passwordd,))
			self.create_gui()
		


	def sign_up_gui(self):
		self.make_frame()
		self.please = True

		# the entry-input frame
		self.entry_input = Frame(self.frm, bg = 'lightgray')
		self.entry_input.place(x = 20, y = 20 , width = 460, height = 210)

		# the entries

		self.emri_ent = Entry(self.entry_input, justify = 'center', font=('Consolas',10))
		self.mbiemri_ent = Entry(self.entry_input, justify = 'center', font=('Consolas',10))
		self.username_ent = Entry(self.entry_input, justify = 'center', font=('Consolas',10))
		self.password_ent_s = Entry(self.entry_input, justify = 'center', font=('Consolas',10), show = '*')

		self.emri_ent.place(x=230,y=15,width=150,height=25)
		self.mbiemri_ent.place(x=230,y=55,width=150,height=25)
		self.username_ent.place(x=230,y=95,width=150,height=25)
		self.password_ent_s.place(x=230,y=135,width=150,height=25)


		# the labels
		self.emri_lbl = Label(self.entry_input, text = 'First name:', font=('Consolas',14), fg='black', bg = 'white').place(x=80, y=15, height=25, width=150)
		self.mbiemri_lbl = Label(self.entry_input, text = 'Last name:', font=('Consolas',14), fg='black', bg = 'white').place(x=80, y=55, height=25, width=150)
		self.user_lbl = Label(self.entry_input, text = 'User name:', font=('Consolas',14), fg='black', bg = 'white').place(x=80, y=95, height=25, width=150)
		self.password_lbl = Label(self.entry_input, text = 'Password:', font=('Consolas',14), fg='black', bg = 'white').place(x=80, y=135, height=25, width=150)

		self.create_the_damn_account = Button(self.entry_input, text = 'Sign up!', command = self.sign_up)
		self.create_the_damn_account.place(x=80,y=170, width = 149)

		self.go_the_fuck_back = Button(self.entry_input, text = 'Go back!', command = self.create_gui, bg = 'lightgray')
		self.go_the_fuck_back.place(x=232,y=170, width = 149)

	def create_gui(self):
		if not self.please:
			self.root = Tk()
			self.root.title('Password manager')
			self.root.geometry('500x250')
			self.root.iconbitmap('favicon.ico')

			self.make_frame()

		self.entry_input = Frame(self.frm, bg = 'lightgray')
		self.entry_input.place(x = 20, y = 20 , width = 460, height = 210)


		self.name_lbl = Label(self.entry_input, text = 'Username', font=('Consolas',14,'bold'), fg='gray', bg = 'lightgray').place(x=30, y=7, height=20)
		self.password_lbl = Label(self.entry_input, text = 'Password', font=('Consolas',14,'bold'), fg='gray', bg = 'lightgray').place(x=30, y=67, height=20)

		self.name_ent = Entry(self.entry_input, justify = 'center', font=('Consolas',14))
		self.name_ent.place(x=30,y=32,width=400,height=30)

		self.password_ent = Entry(self.entry_input, show='*', justify = 'center', font=('Consolas',14))
		self.password_ent.place(x=30,y=94,width=400,height=30)

		self.login = Button(self.entry_input, text = 'Log in!', command = self.logged_in)
		self.login.place(x=30,y=156, width = 199)

		self.create = Button(self.entry_input, text = 'Create account!', command = self.sign_up_gui, bg = 'lightgray')
		self.create.place(x=231,y=156, width = 199)

		if not self.please:
			self.root.mainloop()
	def logged_in(self):

		# the values inputted
		userN = self.name_ent.get()
		passW = self.password_ent.get()

		tupleInputted = (userN, passW)

		# the values from the database
		self.cursor.execute("""SELECT username, password FROM users;""")
		self.usersAll = self.cursor.fetchall()


		# the login
		if tupleInputted in self.usersAll or self.code == True:


			# the user if he creates something
			self.UserForeignK = userN
			self.PassForeignK = passW 



			self.code = True
			self.make_frame()

			self.names = ['Enter platform','Get password','Edit password','Delete password','Log out']
			self.btns = []
			ypos = 20
			for i in range(len(self.names)):
				self.btns.append(Button(text=self.names[i], bg='lightgray', font=('Consolas',12), command = lambda x = self.names[i] : self.second_step(x)))
				self.btns[i].place(x = 20, y = ypos, width = 460, height = 35)
				ypos += 45
			self.btns[4].config(bg = '#ede3e3')
	def second_step(self, index):

		self.make_frame()

		if index == self.names[0]:
			self.platform_lbl = Label(self.frm, text = 'Platform', font=('arial',12,'bold'), fg='gray').place(x=40, y=15, height=20)
			
			self.platforma_ent = Entry(self.frm, justify = 'center', font=('Consolas',14))
			self.platforma_ent.place(x= 40, y = 40, width=420, height = 30)


			self.filler = Frame(self.frm, bg = '#dee4ed')
			self.filler.place(x = 40, y = 80, width = 420, height = 140)

			self.enter = Button(self.filler, text = 'Submit!', command = self.get_platform, justify = 'center', font=('Consolas',14))
			self.enter.place(x=20,y=20,width=380,height=40)

			self.back = Button(self.filler, text = 'Go back!', command = self.logged_in, bg = 'lightgray', justify = 'center', font=('Consolas',14))
			self.back.place(x=20,y=80,width=380,height=40)

		elif index == self.names[1] or index == self.names[2] or index == self.names[3]:
			self.select()

			self.list_p = Listbox(self.frm, bg='lightgray', font=('courier', 10), bd=2, highlightcolor='gray', selectmode = SINGLE)
			self.list_p.place(x = 39,y = 40,height = 160, width = 422)


			self.back = Button(self.frm, text = 'Go back!', command = self.logged_in, bg = 'lightgray')
			self.back.place(x=251,y=215,width=209,height=25)

			if index == self.names[1]:
				self.copy = Button(self.frm, text='Copy!', command = self.copy)
				self.copy.place(x=40,y=215,width=209,height=25)
			elif index == self.names[2]:
				self.edit_pass_entry = Entry(self.frm, justify = 'center', font=('Consolas',14), state = 'disabled')
				self.edit_pass_entry.place(x= 40, y = 40, width=420, height = 30)


				self.edit_btn = Button(self.frm, text = 'Edit!', command = self.edit_passw, justify = 'center', font=('Consolas',14))
				self.edit_btn.place(x=40,y=215,width=209,height=25)

				self.list_p.place(x = 39,y = 80,height = 120, width = 422)
				self.back.place(x=251,y=215,width=209,height=25)

				# listbox selection with double click
				self.list_p.bind("<Double-Button-1>", self.chose_passw)
			elif index == self.names[3]:
				# print('this')
				self.delete = Button(self.frm, text='Delete!', command = self.delete, bg = 'lightgray')
				self.delete.place(x=40,y=215,width=209,height=25)

			# adds content on the listbox
			self.add_read()


		


			# self.list_p = Listbox(self.frm, bg='lightgray', font=('courier', 10), bd=2, highlightcolor='gray', selectmode = SINGLE)
			# self.list_p.place(x=40, y=80, width=420, height=130)


			# adds content on the listbox


		elif index == self.names[4]:
			self.code = False
			self.please = True
			self.create_gui()

	def select(self):
		self.cursor.execute("SELECT emri, password FROM platforma WHERE user = ?", (self.UserForeignK,))
		self.plats = self.cursor.fetchall()
		print(self.plats)
		
	def add_read(self):
		self.list_p.delete(0,1000000000)
		self.listboxi = []

		for i in range(len(self.plats)):
			the_text = 'Platforma:\t|' + self.plats[i][0] + '| \tPasswordi:\t| ' + self.plats[i][1]

			self.list_p.insert(END, the_text)
			self.listboxi.append(the_text)

	def chose_passw(self, event):
		# this is a selection of the platform we request
		self.selection = self.list_p.curselection()[0]
		#turn the entry back to normal and 
		self.edit_pass_entry.config(state = 'normal')
		if self.edit_pass_entry.get() != '':
			self.edit_pass_entry.delete(0, 500)

		self.edit_pass_entry.insert(0, self.plats[self.selection][1])
		

	def edit_passw(self):
		# grab the edited password
		the_current_password = self.edit_pass_entry.get()
		self.edit_pass_entry.delete(0, 500)


		for i in range(len(self.plats)):
			print(self.plats[self.selection], self.plats[i])
			if self.plats[self.selection] == self.plats[i]:
				platforma = self.plats[i][0]
				print(platforma,self.selection)
				
				self.cursor.execute("DELETE from platforma where emri = ?",(platforma,))
				self.cursor.execute("INSERT INTO platforma VALUES(null,?,?,?)", (platforma, the_current_password,self.UserForeignK,))
				self.select()
				self.add_read()


		
		


	def get_platform(self):
		passwordi = self.create_password()
		platforma = self.platforma_ent.get()
		self.cursor.execute(" INSERT INTO platforma VALUES(null,?,?,?)", (platforma, passwordi, self.UserForeignK))
		self.platforma_ent.delete(0, 500)
		
	def create_password(self):
		self.password = ''
		for i in range(len(self.some_strings)):
			self.password += random.choice(self.some_strings)

		self.password += str(hash(random.randint(1,10000000000000)))
		return self.password


	def delete(self):
		print('qkado')
		print(self.list_p.selection_get())


		selected = self.list_p.selection_get()
		for i in range(len(self.plats)):
			if selected == self.listboxi[i]:
				platforma = self.plats[i][0]
				print(selected, platforma)
				
				self.cursor.execute("DELETE from platforma where emri = ?",(platforma,))
				self.select()
				self.add_read()

	def copy(self):
		try:
			selected = self.list_p.selection_get()

			for i in range(len(self.listboxi)):
				if selected == self.listboxi[i]:
					
						self.root.withdraw()
						self.root.clipboard_clear()
						self.root.clipboard_append(self.plats[i][1])
						self.root.update()
		except:
			pass


test = passwordStorer()
test.create_gui()
