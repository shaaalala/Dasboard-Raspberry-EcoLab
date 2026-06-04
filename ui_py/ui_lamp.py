# -*- coding: utf-8 -*-

from PySide6.QtCore import (Qt, QMetaObject, QCoreApplication, QSize)
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QWidget,
    QToolButton, QSizePolicy, QSpacerItem,
    QGridLayout
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")

        Form.resize(1024, 600)
        Form.setMaximumSize(QSize(1024, 600))

        Form.setStyleSheet("""
        QWidget {
            background: transparent;
        }
        QToolButton {
            background-color: #7f8c8d;
            color: white;
            border-radius: 20px;
            font-size: 14px;
        }
        QToolButton:checked {
            background-color: #f39c12;
        }
        QToolButton:pressed {
            background-color: #626567;
        }
        """)

        # =========================
        # MAIN VERTICAL
        # =========================
        self.verticalLayout = QVBoxLayout(Form)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout.addItem(self.verticalSpacer)

        # =========================
        # TITLE
        # =========================
        self.label_title = QLabel(Form)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet("""
            color: #00C2FF;
            font-size: 40px;
            font-weight: bold;
            padding-bottom: 10px;
        """)
        self.verticalLayout.addWidget(self.label_title)

        # =========================
        # MAIN HORIZONTAL (MAP + CONTROL)
        # =========================
        self.mainLayout = QHBoxLayout()
        self.verticalLayout.addLayout(self.mainLayout)

        # =========================
        # LEFT: DENAH IMAGE
        # =========================
        self.mapLabel = QLabel(Form)

        pixmap = QPixmap("assets/DENAH.png")
        self.mapLabel.setPixmap(
            pixmap.scaled(
                420,
                420,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.mapLabel.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.mapLabel)

        # =========================
        # RIGHT: BUTTON GRID
        # =========================
        self.rightWidget = QWidget(Form)
        self.lampGrid = QGridLayout(self.rightWidget)
        self.lampGrid.setSpacing(20)

        icon = QIcon()
        icon.addFile("assets/LAMP OFF.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        # =========================
        # BUTTONS
        # =========================
        self.lamp1 = QToolButton(Form)
        self.lamp1.setIcon(icon)
        self.lamp1.setIconSize(QSize(70, 70))
        self.lamp1.setCheckable(True)
        self.lamp1.setText("Lamp 1\nOFF")

        self.lamp2 = QToolButton(Form)
        self.lamp2.setIcon(icon)
        self.lamp2.setIconSize(QSize(70, 70))
        self.lamp2.setCheckable(True)
        self.lamp2.setText("Lamp 2\nOFF")

        self.lamp3 = QToolButton(Form)
        self.lamp3.setIcon(icon)
        self.lamp3.setIconSize(QSize(70, 70))
        self.lamp3.setCheckable(True)
        self.lamp3.setText("Lamp 3\nOFF")

        self.lamp4 = QToolButton(Form)
        self.lamp4.setIcon(icon)
        self.lamp4.setIconSize(QSize(70, 70))
        self.lamp4.setCheckable(True)
        self.lamp4.setText("Lamp 4\nOFF")

        self.lamp5 = QToolButton(Form)
        self.lamp5.setIcon(icon)
        self.lamp5.setIconSize(QSize(70, 70))
        self.lamp5.setCheckable(True)
        self.lamp5.setText("Lamp 5\nOFF")

        # =========================
        # GRID LAYOUT (2-2-1)
        # =========================
        self.lampGrid.addWidget(self.lamp1, 0, 0)
        self.lampGrid.addWidget(self.lamp2, 0, 1)

        self.lampGrid.addWidget(self.lamp3, 1, 0)
        self.lampGrid.addWidget(self.lamp4, 1, 1)

        self.lampGrid.addWidget(self.lamp5, 2, 0, 1, 2)

        self.mainLayout.addWidget(self.rightWidget)

        # =========================
        # STATUS LABEL
        # =========================
        self.label_MCUA = QLabel(Form)
        self.label_MCUA.setAlignment(Qt.AlignCenter)
        self.label_MCUA.setStyleSheet("""
            color: red;
            font-weight: bold;
        """)
        self.verticalLayout.addWidget(self.label_MCUA)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        self.verticalLayout.addItem(self.verticalSpacer_2)

        # =========================
        # TEXT
        # =========================
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.label_title.setText(
            QCoreApplication.translate("Form", "LIGHTING CONTROL", None)
        )

        self.lamp1.setText("Lamp 1\nOFF")
        self.lamp2.setText("Lamp 2\nOFF")
        self.lamp3.setText("Lamp 3\nOFF")
        self.lamp4.setText("Lamp 4\nOFF")
        self.lamp5.setText("Lamp 5\nOFF")

        self.label_MCUA.setText(
            QCoreApplication.translate("Form", "MCU A: DISCONNECTED", None)
        )