from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit
from backend import Chatbot
import sys
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        #Chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        #Input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        #Button
        self.button = QPushButton("Chat!", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()
    def send_message(self):
        user_inputs = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'> <b>Me: </b> {user_inputs}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_inputs,))
        thread.start()

    def get_bot_response(self, user_inputs):
        response = self.chatbot.get_response(user_input=user_inputs)
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'> <b>Bot: </b>{response}</p>")
#Execute app
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())