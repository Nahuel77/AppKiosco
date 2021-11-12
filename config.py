from main import *

class Config():

	def btn_email(self):
		if self.ui.btn_email.text() == 'Ok':
			self.save_email()
		else:
			self.change_email()

	def save_email(self):
		if len(self.ui.email_entry.text()) and len(self.ui.pass_entry.text()) == 0:
			self.ui.email_status.setText('Ingrese una direccion de gmail y un password')
		else:
			email = self.ui.email_entry.text()
			password = self.ui.pass_entry.text()
			verify = validate_email(email, check_mx=True, verify=True)
			if verify == True:
				self.ui.email_status.setText('Email {} actualmente guardado'.format(email))
				query = 'INSERT INTO config VALUES(?, ?)'
				parameters = (
					email,
					password
					)
				self.run_query(query, (parameters))

				self.ui.email_entry.setReadOnly(True)
				self.ui.email_entry.setStyleSheet("color: rgb(141, 141, 211); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 0), stop:1 rgba(0, 170, 			255, 155));")
				self.ui.email_entry.setGeometry(QRect(230, 180, 181, 41))
				self.ui.btn_email.setGeometry(QRect(430, 180, 221, 41))
				self.ui.btn_email.setText('Cambiar')

				self.ui.pass_entry.setReadOnly(True)
				self.ui.pass_entry.setStyleSheet("color: rgb(141, 141, 211); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 0), stop:1 rgba(0, 170, 			255, 155));")
				self.ui.pass_entry.setGeometry(QRect(230, 240, 181, 41))

			else:
				self.ui.email_status.setText('El email ingresado no existe')
				self.ui.email_entry.clear()

	def change_email(self):
		query = 'DELETE FROM config'
		self.run_query(query)
		self.ui.email_entry.setReadOnly(False)
		self.ui.email_entry.setStyleSheet("color: rgb(0, 0, 0); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));")
		self.ui.email_entry.setGeometry(QRect(230, 180, 301, 41))
		self.ui.btn_email.setGeometry(QRect(550, 180, 101, 41))
		self.ui.btn_email.setText('Ok')

		self.ui.pass_entry.setReadOnly(False)
		self.ui.pass_entry.setStyleSheet("color: rgb(0, 0, 0); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 255), stop:1 rgba(0, 170, 			255, 255));")
		self.ui.pass_entry.setGeometry(QRect(230, 240, 301, 41))

		self.ui.email_entry.clear()
		self.ui.pass_entry.clear()
		self.ui.email_status.setText('Ingrese una direccion de email')

	def remember_email(self):
		query = 'SELECT mail FROM config'
		result = self.run_query(query)
		if len(result) != 0:
			email = result[0][0]
			self.ui.email_entry.setReadOnly(True)
			self.ui.email_entry.setStyleSheet("color: rgb(141, 141, 211); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 0), stop:1 rgba(0, 170, 			255, 155));")
			self.ui.email_entry.setGeometry(QRect(230, 180, 181, 41))
			self.ui.btn_email.setGeometry(QRect(430, 180, 221, 41))
			self.ui.btn_email.setText('Cambiar')

			self.ui.pass_entry.setReadOnly(True)
			self.ui.pass_entry.setStyleSheet("color: rgb(141, 141, 211); background-color: qlineargradient(spread:pad, x1:0.522682, y1:1, 						x2:0.516682, y2:0.011, stop:0 rgba(0, 111, 166, 0), stop:1 rgba(0, 170, 			255, 155));")
			self.ui.pass_entry.setGeometry(QRect(230, 240, 181, 41))

			self.ui.email_status.setText('Email {} actualmente guardado'.format(email))
		else:
			self.ui.email_status.setText('Ingrese una direccion de email')

	def email_config(self):
		if self.ui.btn_email.text() == 'Cambiar':
			self.ui.label_backup.setText('Creando Backup. ¡Adios!')
			query = 'SELECT mail FROM config'
			result = self.run_query(query)
			EMAIL = result[0][0]
			query2 = 'SELECT pass FROM config'
			result2 = self.run_query(query2)
			PASSWORD = result2[0][0]
			
			msg = EmailMessage()
			msg['Subject'] = 'Kiosco database backup'
			msg['From'] = EMAIL
			msg['To'] = EMAIL
			msg.set_content('Backup correspondiente al dia {}'.format(self.time))

			with open('dbkiosco.db', 'rb') as f:
				file_data = f.read()
				file_name = f.name

			msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = 'dbkiosco.db')

			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				smtp.login(EMAIL, PASSWORD)
				smtp.send_message(msg)

	def close_db(self):
		self.email_config()
		self.close()