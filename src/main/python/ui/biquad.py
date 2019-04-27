# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biquad.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_exportBiquadDialog(object):
    def setupUi(self, exportBiquadDialog):
        exportBiquadDialog.setObjectName("exportBiquadDialog")
        exportBiquadDialog.resize(691, 810)
        self.gridLayout = QtWidgets.QGridLayout(exportBiquadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.fs = QtWidgets.QComboBox(exportBiquadDialog)
        self.fs.setObjectName("fs")
        self.fs.addItem("")
        self.fs.addItem("")
        self.fs.addItem("")
        self.gridLayout.addWidget(self.fs, 2, 1, 1, 1)
        self.maxBiquadsLabel = QtWidgets.QLabel(exportBiquadDialog)
        self.maxBiquadsLabel.setObjectName("maxBiquadsLabel")
        self.gridLayout.addWidget(self.maxBiquadsLabel, 3, 0, 1, 1)
        self.fsLabel = QtWidgets.QLabel(exportBiquadDialog)
        self.fsLabel.setObjectName("fsLabel")
        self.gridLayout.addWidget(self.fsLabel, 2, 0, 1, 1)
        self.maxBiquads = QtWidgets.QSpinBox(exportBiquadDialog)
        self.maxBiquads.setMinimum(1)
        self.maxBiquads.setMaximum(100)
        self.maxBiquads.setProperty("value", 10)
        self.maxBiquads.setObjectName("maxBiquads")
        self.gridLayout.addWidget(self.maxBiquads, 3, 1, 1, 1)
        self.biquads = QtWidgets.QPlainTextEdit(exportBiquadDialog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.biquads.setFont(font)
        self.biquads.setReadOnly(True)
        self.biquads.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.biquads.setObjectName("biquads")
        self.gridLayout.addWidget(self.biquads, 4, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setDefaults = QtWidgets.QToolButton(exportBiquadDialog)
        self.setDefaults.setObjectName("setDefaults")
        self.horizontalLayout.addWidget(self.setDefaults)
        self.outputFormat = QtWidgets.QComboBox(exportBiquadDialog)
        self.outputFormat.setObjectName("outputFormat")
        self.outputFormat.addItem("")
        self.outputFormat.addItem("")
        self.outputFormat.addItem("")
        self.outputFormat.addItem("")
        self.horizontalLayout.addWidget(self.outputFormat)
        self.showHex = QtWidgets.QCheckBox(exportBiquadDialog)
        self.showHex.setChecked(False)
        self.showHex.setObjectName("showHex")
        self.horizontalLayout.addWidget(self.showHex)
        self.saveToFile = QtWidgets.QToolButton(exportBiquadDialog)
        self.saveToFile.setObjectName("saveToFile")
        self.horizontalLayout.addWidget(self.saveToFile)
        self.copyToClipboardBtn = QtWidgets.QToolButton(exportBiquadDialog)
        self.copyToClipboardBtn.setObjectName("copyToClipboardBtn")
        self.horizontalLayout.addWidget(self.copyToClipboardBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)

        self.retranslateUi(exportBiquadDialog)
        self.showHex.clicked.connect(exportBiquadDialog.updateBiquads)
        self.fs.currentIndexChanged['int'].connect(exportBiquadDialog.updateBiquads)
        self.maxBiquads.valueChanged['int'].connect(exportBiquadDialog.updateBiquads)
        self.setDefaults.clicked.connect(exportBiquadDialog.save)
        self.copyToClipboardBtn.clicked.connect(exportBiquadDialog.copyToClipboard)
        self.saveToFile.clicked.connect(exportBiquadDialog.export)
        self.outputFormat.currentTextChanged['QString'].connect(exportBiquadDialog.update_format)
        QtCore.QMetaObject.connectSlotsByName(exportBiquadDialog)

    def retranslateUi(self, exportBiquadDialog):
        _translate = QtCore.QCoreApplication.translate
        exportBiquadDialog.setWindowTitle(_translate("exportBiquadDialog", "Export Biquads"))
        self.fs.setItemText(0, _translate("exportBiquadDialog", "48000"))
        self.fs.setItemText(1, _translate("exportBiquadDialog", "96000"))
        self.fs.setItemText(2, _translate("exportBiquadDialog", "192000"))
        self.maxBiquadsLabel.setText(_translate("exportBiquadDialog", "Max Biquads"))
        self.fsLabel.setText(_translate("exportBiquadDialog", "Sample Rate (Hz)"))
        self.setDefaults.setText(_translate("exportBiquadDialog", "..."))
        self.outputFormat.setItemText(0, _translate("exportBiquadDialog", "Minidsp 2x4HD"))
        self.outputFormat.setItemText(1, _translate("exportBiquadDialog", "Minidsp 10x10HD"))
        self.outputFormat.setItemText(2, _translate("exportBiquadDialog", "Minidsp 2x4"))
        self.outputFormat.setItemText(3, _translate("exportBiquadDialog", "User Selected"))
        self.showHex.setText(_translate("exportBiquadDialog", "Show Hex Value?"))
        self.saveToFile.setText(_translate("exportBiquadDialog", "..."))
        self.copyToClipboardBtn.setText(_translate("exportBiquadDialog", "..."))


