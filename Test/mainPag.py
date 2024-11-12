from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication([])

# Crear ventana principal
window = QWidget()
window.setWindowTitle("Mi Primera App con PyQt")
window.setGeometry(100, 100, 400, 200)

# Configurar el diseño de la ventana
layout = QVBoxLayout()
label = QLabel("¡Hola, PyQt!")
label.setStyleSheet("font-size: 20px; color: #3498db;")
layout.addWidget(label)

window.setLayout(layout)
window.show()

# Ejecutar la aplicación solo para ver si funciona xd
app.exec_()
