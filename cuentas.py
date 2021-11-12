from main import *

class Cuentas():

	def get_cuentas(self):
		query = 'SELECT id_cuenta, nombre_cuenta FROM cuentas'
		db_rows = self.run_query(query)
		self.ui.listaCuentas.setColumnCount(2)
		self.ui.listaCuentas.setRowCount(len(db_rows))
		self.ui.listaCuentas.setHorizontalHeaderLabels(['Id', 'Nombre'])
		for row in range(len(db_rows)):
			for column in range(len(db_rows[0])):
				self.ui.listaCuentas.setItem(
					row,
					column,
					QTableWidgetItem(str(db_rows[row][column]))
				)

	def current_cuenta(self):
		if self.ui.listaCuentas.selectedItems():
			row = self.ui.listaCuentas.currentRow()
			return self.ui.listaCuentas.item(row, 0).text()

	def current_deuda(self):
		if self.ui.listaDeudas.selectedItems():
			row = self.ui.listaDeudas.currentRow()
			return self.ui.listaDeudas.item(row, 0).text()

	def get_deudas(self):
		if self.current_cuenta():
			query = 'SELECT id_deuda, fecha_monto, horario_monto, monto_deuda, pago_deuda, detallado FROM deuda WHERE id_cuenta1 = ?'
			db_rows = self.run_query(query, (self.current_cuenta(),))
			self.ui.listaDeudas.setColumnCount(6)
			self.ui.listaDeudas.setRowCount(len(db_rows))
			self.ui.listaDeudas.setHorizontalHeaderLabels(['Id', 'Fecha', 'Horario', 'Deuda', 'Pago', 'Detallado'])
			self.ui.listaDeudas.setColumnHidden(0, True)
			self.subtotal()
			for row in range(len(db_rows)):
				for column in range(len(db_rows[0])):
					self.ui.listaDeudas.setItem(
						row,
						column,
						QTableWidgetItem(str(db_rows[row][column]))
					)
		else:
			self.ui.status_Cuenta.setText('Seleccione un nombre de cuenta')

	def agregar_deuda(self):
		if self.current_cuenta():
			if len(self.ui.montodeuda_entry.text()) or len(self.ui.pagodeuda_entry.text()) != 0:
				query = 'INSERT INTO deuda VALUES(NULL, ?, ?, ?, ?, ?, ?)'
				parameters = (
					self.time,
					self.get_time(),
					self.ui.montodeuda_entry.text(),
					self.ui.pagodeuda_entry.text(),
					self.ui.productodeuda_entry.text(),
					self.current_cuenta()
					)
				self.run_query(query, (parameters))

				# Hacia el historial de Cuentas

				query2 = 'SELECT nombre_cuenta FROM cuentas WHERE id_cuenta = ?'
				result = self.run_query(query2, (self.current_cuenta(),))
				cuenta = result[0][0]
				query3 = 'INSERT INTO historial_deudas VALUES(NULL, ?, ?, ?, ?, ?, ?)'
				parameters2 = (
					self.time,
					self.get_time(),
					cuenta,
					self.ui.montodeuda_entry.text(),
					self.ui.pagodeuda_entry.text(),
					self.ui.productodeuda_entry.text()
					)
				self.run_query(query3, (parameters2))
				self.ui.montodeuda_entry.clear()
				self.ui.pagodeuda_entry.clear()
				self.get_historial_deudas()
				self.get_deudas()
			else:
				self.ui.status_Cuenta.setText('Debe ingresar el monto de deuda o pago')
		else:
			self.ui.status_Cuenta.setText('Seleccione un nombre de cuenta')

	def subtotal(self):
		query = 'SELECT SUM(monto_deuda) FROM deuda WHERE id_cuenta1 = ?'
		deuda = self.run_query(query, (self.current_cuenta(),))
		res = deuda[0]
		total_deuda = ''.join(str(v) for v in res)
		query2 = 'SELECT SUM(pago_deuda) FROM deuda WHERE id_cuenta1 = ?'
		pago = self.run_query(query2, (self.current_cuenta(),))
		res2 = pago[0]
		pago_total = ''.join(str(v) for v in res2)
		if total_deuda != 'None':
			total = float(total_deuda)- float(pago_total)
			self.ui.total_deuda.setText('Deuda total: {}'.format(total))
			if total == 0:
				query3 = 'DELETE FROM deuda WHERE id_cuenta1 = ?'
				self.run_query(query3, (self.current_cuenta(),))
		else:
			self.ui.total_deuda.setText('No acredita deuda')

	def borrar_deuda(self):
		if self.current_deuda():
			query = 'DELETE FROM deuda WHERE id_deuda = ?'
			self.run_query(query, (self.current_deuda(),))
			self.get_deudas()
		else:
			self.ui.status_Cuenta.setText('Seleccione un registro de deuda')

	def buscar_cuenta(self):
		if len(self.ui.buscarcuenta_entry.text()) != 0:
			cuenta = self.ui.buscarcuenta_entry.text()
			query = 'SELECT * FROM cuentas WHERE nombre_cuenta LIKE ?'
			db_rows = self.run_query(query, (cuenta,))
			self.ui.buscarcuenta_entry.clear()
			self.ui.listaCuentas.setColumnCount(2)
			self.ui.listaCuentas.setRowCount(len(db_rows))
			self.ui.listaCuentas.setHorizontalHeaderLabels(['Id', 'Nombre'])
			for row in range(len(db_rows)):
				for column in range(len(db_rows[0])):
					self.ui.listaCuentas.setItem(
						row,
						column,
						QTableWidgetItem(str(db_rows[row][column]))
					)
			self.ui.buscarcuenta_entry.setGeometry(QRect(30, 70, 71, 41))
			self.ui.btn_buscarcuenta.setGeometry(QRect(120, 70, 141, 41))
			self.ui.btn_buscarcuenta.setText('Volver')
			if len(db_rows) == 0:
				self.ui.status_Cuenta.setText('No se encontraron resultados')
		else:
			self.ui.status_Cuenta.setText('Ingrese el nombre de cuenta')

	def volver(self):
		if self.ui.btn_buscarcuenta.clicked:
			self.get_cuentas()
			self.ui.buscarcuenta_entry.setGeometry(QRect(30, 70, 171, 41))
			self.ui.btn_buscarcuenta.setGeometry(QRect(220, 70, 41, 41))
			self.ui.btn_buscarcuenta.setText('Ok')

	def btn_status(self):
		if self.ui.btn_buscarcuenta.text() == 'Ok':
			self.buscar_cuenta()
		else:
			self.volver()

	def agregar_cuenta(self):
		if len(self.ui.nuevacuenta_entry.text()) != 0:
			nombre = self.ui.nuevacuenta_entry.text()
			query = 'SELECT nombre_cuenta FROM cuentas WHERE nombre_cuenta LIKE ?'
			cuenta = self.run_query(query, (nombre,))
			if len(cuenta) != 0:
				self.ui.status_Cuenta.setText('El nombre ya existe en el registro')
				self.ui.nuevacuenta_entry.clear()
			else:
				query2 = 'INSERT INTO cuentas VALUES(NULL, ?)'
				self.run_query(query2, (nombre,))
				self.ui.status_Cuenta.setText('Cuenta agregada')
				self.get_cuentas()
				self.ui.nuevacuenta_entry.clear()
		else:
			self.ui.status_Cuenta.setText('Ingrese el nombre de la nueva cuenta')

	def borrar_cuenta(self):
		if self.current_cuenta():
			query = 'DELETE FROM deuda WHERE id_cuenta1 = ?'
			query1 = 'DELETE FROM cuentas WHERE id_cuenta = ?'
			self.run_query(query, (self.current_cuenta(),))
			self.run_query(query1, (self.current_cuenta(),))
			self.ui.status_Cuenta.setText('Cuenta borrada')
			self.ui.listaDeudas.setRowCount(0)
			self.get_cuentas()
			self.get_deudas()