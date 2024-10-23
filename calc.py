import sys  # Importa o módulo 'sys', que nos ajuda a usar funções do sistema.
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy  # Importa as classes necessárias para a interface gráfica.


# Cria uma nova classe chamada 'Calculadora' que herda de 'QMainWindow'
class Calculadora(QMainWindow):
    def __init__(self, parent=None):  # Método que é chamado quando criamos a calculadora
        super().__init__(parent)  # Chama o construtor da classe pai (QMainWindow)

        
        # Configurações da Janela
        self.setWindowTitle("CALCULADORA DO RUAN")  # Define o título da janela da calculadora
        self.setFixedSize(400, 400)  # Define o tamanho da janela como 400x400 pixels


        # Widgets e Layout
        self.cw = QWidget()  # Cria um widget (uma área para colocar coisas)
        self.grid = QGridLayout(self.cw)  # Cria uma grade onde vamos organizar os botões e a tela

        
        # Display da Calculadora
        self.display = QLineEdit()  # Cria uma caixa onde vamos mostrar os números
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # Adiciona a caixa à grade (linha 0, coluna 0, ocupa 1 linha e 5 colunas)
        

        # Estilo e Comportamento
        self.display.setDisabled(True)  # Desabilita a edição na caixa (não vamos usar agora)
        self.display.setStyleSheet(
            "* {background: white; color: #000; font-size: 30px;}"  # Fundo branco, texto preto e tamanho da letra 30
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Define como a caixa se comporta ao redimensionar

        
        # Adicionando os botões
        self.add_btn(QPushButton("7"), 1, 0, 1, 1)
        self.add_btn(QPushButton("8"), 1, 1, 1, 1)
        self.add_btn(QPushButton("9"), 1, 2, 1, 1)
        self.add_btn(QPushButton("+"), 1, 3, 1, 1)
        self.add_btn(
            QPushButton("C"), 1, 4, 1, 1,
            lambda: self.display.setText(""),
            "background: #d5580d; color: #fff; font-weight: 700;"
            )

        self.add_btn(QPushButton("4"), 2, 0, 1, 1)
        self.add_btn(QPushButton("5"), 2, 1, 1, 1)
        self.add_btn(QPushButton("6"), 2, 2, 1, 1)
        self.add_btn(QPushButton("-"), 2, 3, 1, 1)
        self.add_btn(
            QPushButton("<-"), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            "background: #13823a; color: #fff; font-weight: 700;"
            )

        self.add_btn(QPushButton("1"), 3, 0, 1, 1)
        self.add_btn(QPushButton("2"), 3, 1, 1, 1)
        self.add_btn(QPushButton("3"), 3, 2, 1, 1)
        self.add_btn(QPushButton("/"), 3, 3, 1, 1)
        self.add_btn(QPushButton(""), 3, 4, 1, 1)  # Você pode colocar um espaço em branco ou removê-lo.

        self.add_btn(QPushButton("."), 4, 0, 1, 1)
        self.add_btn(QPushButton("0"), 4, 1, 1, 1)
        self.add_btn(QPushButton(""), 4, 2, 1, 1)  # Você pode colocar um espaço em branco ou removê-lo.
        self.add_btn(QPushButton("*"), 4, 3, 1, 1)
        self.add_btn(
            QPushButton("="), 4, 4, 1, 1,
            self.eval_igual,
            "background: #095177; color: #fff; font-weight: 700;"
            )
        
        # Definindo o Widget Principal
        self.setCentralWidget(self.cw)  # Define o widget principal da janela

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style = None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)  # Adiciona o botão à grade na posição especificada

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                self.display.text() + btn.text()  # Adiciona o texto do botão à caixa de exibição
                )
            )
        else:
            btn.clicked.connect(funcao)


        if style:
            btn.setStyleSheet(style)


        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Define como o botão se comporta ao redimensionar
    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText("Conta Invalidada")
            pass    

# Esta parte do código é executada quando abrimos o programa
if __name__ == '__main__':
    qt = QApplication(sys.argv)  # Cria uma aplicação Qt (a base do programa)
    calc = Calculadora()  # Cria uma nova calculadora
    calc.show()  # Mostra a calculadora na tela
    qt.exec_()  # Inicia o loop da aplicação (faz com que a janela fique aberta e responda)