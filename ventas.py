from main import *

class Ventas():

	def get_ventas(self):
		query = 'SELECT id, horario, valor, adicional FROM ventas WHERE today = ?'
		db_rows = self.run_query(query, (self.time,))
		self.ui.listaVentas.setColumnCount(4)
		self.ui.listaVentas.setRowCount(len(db_rows))
		self.ui.listaVentas.setHorizontalHeaderLabels(['id', 'Horario','Monto','Adicional'])
		self.ui.listaVentas.setColumnHidden(0, True)
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.listaVentas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)
		query2 = 'DELETE FROM ventas WHERE today != ?'
		self.run_query(query2, (self.time,))

	def validation(self):
		return len(self.ui.ingreso_entry.text()) != 0

	def add_venta(self):
		if self.validation():
		#	self.get_time()#
			query = 'INSERT INTO ventas VALUES(NULL, ?, ?, ?, ?)'
			parameters = (
				self.time,
				self.get_time(),
				self.ui.ingreso_entry.text(),
				self.ui.adicional_entry.text()
				)
			self.run_query(query, parameters)
			self.ui.label_status.setText('Ingreso agregado')

			# Hacia el historial de Ventas

			query2 = 'INSERT INTO historial_ventas VALUES(NULL, ?, ?, ?, ?)'
			self.run_query(query2, (parameters))
			self.get_historial_ventas()
			self.ui.ingreso_entry.clear()
			self.ui.adicional_entry.clear()
			self.get_ventas()
			self.total_dia()
			
		else: self.ui.label_status.setText('Ingrese el valor de venta')

	def delete_venta(self):
		row = self.current_item()
		cell_id = self.ui.listaVentas.item(row, 0).text()
		query = 'DELETE FROM ventas WHERE id = ?'
		self.run_query(query, (cell_id, ))
		self.get_ventas()
		self.total_dia()
		self.ui.label_status.setText('Registro eliminado')

	def current_item(self):
		if self.ui.listaVentas.selectedItems():
			row = self.ui.listaVentas.currentRow()
			self.ui.label_status.setText('')
			return row
		else: self.ui.label_status.setText('Seleccione un registro')

	def total_dia(self):
		query = 'SELECT SUM(valor) FROM ventas'
		result = self.run_query(query)
		res = result[0]
		total = ''.join(str(v) for v in res)
		self.ui.label_dia.setText('Total del dia: {}'.format(total))