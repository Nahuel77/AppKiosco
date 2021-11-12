from main import *

class Historial():

	def get_date(self):
			getdate = self.ui.calendar.selectedDate()
			date = getdate.toString('dd, MM, yyyy')
			self.ui.pruebacalendar.setText('Fecha seleccionada: {}'.format(date))
			return date

	def set_historial(self):
		self.get_historial_deudas()
		self.get_historial_ventas()

	def get_historial_deudas(self):
		date = self.get_date()
		query = 'SELECT id_deudah, fecha_deudah, horario_h, nombre_h, deuda_h, pago_h, detallado_h FROM historial_deudas WHERE fecha_deudah = ?'
		db_rows = self.run_query(query, (date,))
		self.ui.historial_deudas.setColumnCount(7)
		self.ui.historial_deudas.setRowCount(len(db_rows))
		self.ui.historial_deudas.setHorizontalHeaderLabels(['Id', 'Fecha', 'Horario', 'Cuenta', 'Deuda', 'Pago', 'Detallado'])
		self.ui.historial_deudas.setColumnHidden(0, True)
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.historial_deudas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)

	def get_historial_ventas(self):
		date = self.get_date()
		query = 'SELECT * FROM historial_ventas WHERE fecha_ventah = ?'
		db_rows = self.run_query(query, (date,))
		self.ui.historial_ventas.setColumnCount(5)
		self.ui.historial_ventas.setRowCount(len(db_rows))
		self.ui.historial_ventas.setHorizontalHeaderLabels(['Id', 'Fecha', 'Horario', 'Cuenta', 'Adicional'])
		self.ui.historial_ventas.setColumnHidden(0, True)
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.historial_ventas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)