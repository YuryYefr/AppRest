"""Client to start app"""
import sys
from id import AgentName  # To gain employee id
import rest_design  # Table build
from PyQt5 import QtWidgets, QtCore
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from db_conn import create_connection, create_table, insert_table, update_task, select_all_cells


class RestApp(QtWidgets.QMainWindow, rest_design.Ui_Rest):
    """This is a main table"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.click_btn_need_a_rest)
        self.radioButton.clicked.connect(self.click_ready)
        self.radioButton_2.clicked.connect(self.click_rest)

    def search_label(self):
        """To define name of table instance"""
        for column in range(self.tableWidget.columnCount()):
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, column)
                if item and item.text() == self.label.text():
                    return item

    def queue_rest_column(self):
        """To check pending employee"""
        column = [self.tableWidget.item(0, 0).text(),
                  self.tableWidget.item(1, 0).text(),
                  self.tableWidget.item(2, 0).text(),
                  self.tableWidget.item(3, 0).text(),
                  self.tableWidget.item(4, 0).text()]
        return column

    def rest_column(self):
        """To check employee already in rest"""
        column = [self.tableWidget.item(0, 1).text(),
                  self.tableWidget.item(1, 1).text(),
                  self.tableWidget.item(2, 1).text(),
                  self.tableWidget.item(3, 1).text(),
                  self.tableWidget.item(4, 1).text()]
        return column

    def retrieve_from_db_table(self):
        """Synchronizing clients"""
        inject = select_all_cells(conn)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][1]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][2]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][3]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][4]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][5]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][6]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][7]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][8]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][9]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText(f'{inject[0][10]}')
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(4, 1, item)

    def change_name(self, name):
        """Defining employee name"""
        return self.label.setText(f"{name}")

    def click_btn_need_a_rest(self):
        """Starts waiting in queue"""
        item = QtWidgets.QTableWidgetItem()
        item.setText(f"{self.label.text()}")
        item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        try:
            if self.label.text() not in self.queue_rest_column() and self.label.text() not in self.rest_column():
                rows = self.tableWidget.rowCount()
                for i in range(rows):
                    it = self.tableWidget.item(i, 0)
                    if it.text():
                        continue
                    elif not it.text():
                        self.tableWidget.setItem(i, 0, item)
                        client_socket.send(bytes(self.label.text(), 'utf8'))  # Sends data through network
                        conn = create_connection(database)
                        with conn:
                            update_task(conn, self.current_table_save())
                        break
                    else:
                        alert = QtWidgets.QMessageBox()
                        alert.result()
                        alert.setText('Sorry, no place for you, try later')
                        alert.exec_()

            elif self.label.text() in self.queue_rest_column():
                alert = QtWidgets.QMessageBox()
                alert.result()
                alert.setText('Already in queue')
                alert.exec_()
            elif self.label.text() in self.rest_column():
                alert = QtWidgets.QMessageBox()
                alert.result()
                alert.setText('Already in rest')
                alert.exec_()
        except Exception as e:
            print(e)

    def click_rest(self):
        """Moving employee from pending to rest"""
        if self.label.text() in self.queue_rest_column():
            col = self.search_label().column()
            row = self.search_label().row()
            item = self.tableWidget.takeItem(row, col)
            rows = self.tableWidget.rowCount()
            for i in range(rows):
                it = self.tableWidget.item(i, 1)
                if not it.text():
                    self.tableWidget.setItem(i, 1, item)
                    break
            item = QtWidgets.QTableWidgetItem()
            item.setText("")
            item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row, col, item)
            client_socket.send(bytes(self.label.text(), 'utf8'))
            with conn:
                update_task(conn, self.current_table_save())

        elif self.label.text() in self.rest_column():
            """Catch if employee already in rest status"""
            alert = QtWidgets.QMessageBox()
            alert.result()
            alert.setText('Already in rest, click ready')
            alert.exec_()
        else:
            """Catch if employee forgot to add him to pending list"""
            alert = QtWidgets.QMessageBox()
            alert.result()
            alert.setText('Put yourself in queue first')
            alert.exec_()

    def click_ready(self):
        """Removing employee from pending status to rest"""
        if self.label.text() in self.rest_column():
            emp_item = self.search_label()
            item = QtWidgets.QTableWidgetItem()
            item.setText("")
            item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(emp_item.row(), emp_item.column(), item)
            client_socket.send(bytes(self.label.text(), 'utf8'))
            with conn:
                update_task(conn, self.current_table_save())
        else:
            """Catch if employee forgot to move himself in pending"""
            alert = QtWidgets.QMessageBox()
            alert.result()
            alert.setText('Put yourself in rest first')
            alert.exec_()

    def receive(self):
        """Handles receiving of messages."""
        client_socket.send(self.label.text().encode('utf8'))  # ID to network
        while True:
            try:
                network_item = client_socket.recv(1024).decode('utf8')
                new_item = QtWidgets.QTableWidgetItem()
                new_item.setText(f"{network_item}")
                new_item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                if new_item.text() not in self.queue_rest_column() and new_item.text() not in self.rest_column() \
                        and new_item.text() != self.label.text():
                    """Adding ID from network to table"""
                    rows = self.tableWidget.rowCount()
                    for i in range(rows):
                        it = self.tableWidget.item(i, 0)
                        if not it.text():
                            self.tableWidget.setItem(i, 0, new_item)
                            break
                elif new_item.text() in self.queue_rest_column() and new_item.text() != self.label.text():
                    """Moving network ID in table from pending to rest"""

                    def search_incoming():
                        for column in range(self.tableWidget.columnCount()):
                            for row in range(self.tableWidget.rowCount()):
                                item = self.tableWidget.item(row, column)
                                if item and item.text() == new_item.text():
                                    return item

                    col = search_incoming().column()
                    row = search_incoming().row()
                    item = self.tableWidget.takeItem(row, col)
                    item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    rows = self.tableWidget.rowCount()
                    for i in range(rows):
                        it = self.tableWidget.item(i, 1)
                        if not it.text():
                            self.tableWidget.setItem(i, 1, new_item)
                            break
                    item = QtWidgets.QTableWidgetItem()
                    item.setText("")
                    item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(row, col, item)
                elif new_item.text() in self.rest_column() and new_item.text() != self.label.text():
                    """Replacing ID status from rest to empty cell"""

                    def search_incoming():
                        for column in range(self.tableWidget.columnCount()):
                            for row in range(self.tableWidget.rowCount()):
                                item = self.tableWidget.item(row, column)
                                if item and item.text() == new_item.text():
                                    return item

                    emp_item = search_incoming()
                    item = QtWidgets.QTableWidgetItem()
                    item.setText("")
                    item.setFlags(QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(emp_item.row(), emp_item.column(), item)
            except OSError:  # Client logout
                break

    def current_table_save(self):
        """To rewrite db"""
        current_table = (self.tableWidget.item(0, 0).text(),
                         self.tableWidget.item(1, 0).text(),
                         self.tableWidget.item(2, 0).text(),
                         self.tableWidget.item(3, 0).text(),
                         self.tableWidget.item(4, 0).text(),
                         self.tableWidget.item(0, 1).text(),
                         self.tableWidget.item(1, 1).text(),
                         self.tableWidget.item(2, 1).text(),
                         self.tableWidget.item(3, 1).text(),
                         self.tableWidget.item(4, 1).text())
        return current_table


sql_table = """ CREATE TABLE IF NOT EXISTS Rest_table (
                                    id integer PRIMARY KEY,
                                    col1 text NOT NULL,
                                    col2 text NOT NULL,
                                    col3 text NOT NULL,
                                    col4 text NOT NULL,
                                    col5 text NOT NULL,
                                    col6 text NOT NULL,
                                    col7 text NOT NULL,
                                    col8 text NOT NULL,
                                    col9 text NOT NULL,
                                    col10 text NOT NULL); """
HOST = 'localhost'  # server ip
PORT = 35000  # Check if equal open port on server
SERVER_ID = (HOST, PORT)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(SERVER_ID)
database = ""  # Don't forget to place your path
conn = create_connection(database)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RestApp()
    app.setStyle('Fusion')
    window.change_name(AgentName().define_user())
    window.show()
    create_table(conn, sql_table)
    with conn:
        insert_table(conn, window.current_table_save())
    window.retrieve_from_db_table()
    Thread(target=window.receive, daemon=True).start()  # Starts loop in background
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
