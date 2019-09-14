# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'postbuilder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_postbuilder(object):
    def setupUi(self, postbuilder):
        postbuilder.setObjectName("postbuilder")
        postbuilder.resize(628, 715)
        self.gridLayout = QtWidgets.QGridLayout(postbuilder)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonGrid = QtWidgets.QGridLayout()
        self.buttonGrid.setObjectName("buttonGrid")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonGrid.addItem(spacerItem, 0, 2, 1, 1)
        self.closeButton = QtWidgets.QPushButton(postbuilder)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setObjectName("closeButton")
        self.buttonGrid.addWidget(self.closeButton, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonGrid.addItem(spacerItem1, 0, 0, 1, 1)
        self.generateButton = QtWidgets.QPushButton(postbuilder)
        self.generateButton.setAutoDefault(False)
        self.generateButton.setObjectName("generateButton")
        self.buttonGrid.addWidget(self.generateButton, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.buttonGrid, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(postbuilder)
        self.comboBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.dataGrid = QtWidgets.QGridLayout()
        self.dataGrid.setObjectName("dataGrid")
        self.spectrumLabel = QtWidgets.QLabel(postbuilder)
        self.spectrumLabel.setObjectName("spectrumLabel")
        self.dataGrid.addWidget(self.spectrumLabel, 8, 0, 1, 1)
        self.postTextEdit = QtWidgets.QPlainTextEdit(postbuilder)
        self.postTextEdit.setObjectName("postTextEdit")
        self.dataGrid.addWidget(self.postTextEdit, 11, 2, 1, 2)
        self.sourcePicker = QtWidgets.QComboBox(postbuilder)
        self.sourcePicker.setObjectName("sourcePicker")
        self.sourcePicker.addItem("")
        self.sourcePicker.addItem("")
        self.sourcePicker.addItem("")
        self.sourcePicker.addItem("")
        self.dataGrid.addWidget(self.sourcePicker, 6, 2, 1, 2)
        self.pvaValid = QtWidgets.QToolButton(postbuilder)
        self.pvaValid.setEnabled(True)
        self.pvaValid.setText("")
        self.pvaValid.setObjectName("pvaValid")
        self.dataGrid.addWidget(self.pvaValid, 7, 3, 1, 1)
        self.pvaField = QtWidgets.QLineEdit(postbuilder)
        self.pvaField.setObjectName("pvaField")
        self.dataGrid.addWidget(self.pvaField, 7, 2, 1, 1)
        self.warningField = QtWidgets.QLineEdit(postbuilder)
        self.warningField.setObjectName("warningField")
        self.dataGrid.addWidget(self.warningField, 5, 2, 1, 2)
        self.postLabel = QtWidgets.QLabel(postbuilder)
        self.postLabel.setObjectName("postLabel")
        self.dataGrid.addWidget(self.postLabel, 11, 0, 1, 1)
        self.seasonLabel = QtWidgets.QLabel(postbuilder)
        self.seasonLabel.setObjectName("seasonLabel")
        self.dataGrid.addWidget(self.seasonLabel, 3, 0, 1, 1)
        self.noteField = QtWidgets.QLineEdit(postbuilder)
        self.noteField.setObjectName("noteField")
        self.dataGrid.addWidget(self.noteField, 4, 2, 1, 2)
        self.spectrumValid = QtWidgets.QToolButton(postbuilder)
        self.spectrumValid.setEnabled(True)
        self.spectrumValid.setText("")
        self.spectrumValid.setObjectName("spectrumValid")
        self.dataGrid.addWidget(self.spectrumValid, 8, 3, 1, 1)
        self.yearLabel = QtWidgets.QLabel(postbuilder)
        self.yearLabel.setObjectName("yearLabel")
        self.dataGrid.addWidget(self.yearLabel, 1, 0, 1, 1)
        self.editionField = QtWidgets.QLineEdit(postbuilder)
        self.editionField.setObjectName("editionField")
        self.dataGrid.addWidget(self.editionField, 2, 2, 1, 2)
        self.label = QtWidgets.QLabel(postbuilder)
        self.label.setObjectName("label")
        self.dataGrid.addWidget(self.label, 12, 0, 1, 1)
        self.pvaLabel = QtWidgets.QLabel(postbuilder)
        self.pvaLabel.setObjectName("pvaLabel")
        self.dataGrid.addWidget(self.pvaLabel, 7, 0, 1, 1)
        self.formatLabel = QtWidgets.QLabel(postbuilder)
        self.formatLabel.setObjectName("formatLabel")
        self.dataGrid.addWidget(self.formatLabel, 10, 0, 1, 1)
        self.warningLabel = QtWidgets.QLabel(postbuilder)
        self.warningLabel.setObjectName("warningLabel")
        self.dataGrid.addWidget(self.warningLabel, 5, 0, 1, 1)
        self.noteLabel = QtWidgets.QLabel(postbuilder)
        self.noteLabel.setObjectName("noteLabel")
        self.dataGrid.addWidget(self.noteLabel, 4, 0, 1, 1)
        self.editionLabel = QtWidgets.QLabel(postbuilder)
        self.editionLabel.setObjectName("editionLabel")
        self.dataGrid.addWidget(self.editionLabel, 2, 0, 1, 1)
        self.spectrumField = QtWidgets.QLineEdit(postbuilder)
        self.spectrumField.setObjectName("spectrumField")
        self.dataGrid.addWidget(self.spectrumField, 8, 2, 1, 1)
        self.seasonField = QtWidgets.QLineEdit(postbuilder)
        self.seasonField.setObjectName("seasonField")
        self.dataGrid.addWidget(self.seasonField, 3, 2, 1, 2)
        self.titleLabel = QtWidgets.QLabel(postbuilder)
        self.titleLabel.setObjectName("titleLabel")
        self.dataGrid.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.sourceLabel = QtWidgets.QLabel(postbuilder)
        self.sourceLabel.setObjectName("sourceLabel")
        self.dataGrid.addWidget(self.sourceLabel, 6, 0, 1, 1)
        self.fileName = QtWidgets.QLineEdit(postbuilder)
        self.fileName.setReadOnly(True)
        self.fileName.setObjectName("fileName")
        self.dataGrid.addWidget(self.fileName, 12, 2, 1, 2)
        self.titleField = QtWidgets.QLineEdit(postbuilder)
        self.titleField.setObjectName("titleField")
        self.dataGrid.addWidget(self.titleField, 0, 2, 1, 1)
        self.yearField = QtWidgets.QLineEdit(postbuilder)
        self.yearField.setObjectName("yearField")
        self.dataGrid.addWidget(self.yearField, 1, 2, 1, 1)
        self.titleValid = QtWidgets.QToolButton(postbuilder)
        self.titleValid.setText("")
        self.titleValid.setObjectName("titleValid")
        self.dataGrid.addWidget(self.titleValid, 0, 3, 1, 1)
        self.yearValid = QtWidgets.QToolButton(postbuilder)
        self.yearValid.setEnabled(True)
        self.yearValid.setText("")
        self.yearValid.setObjectName("yearValid")
        self.dataGrid.addWidget(self.yearValid, 1, 3, 1, 1)
        self.formatGrid = QtWidgets.QGridLayout()
        self.formatGrid.setObjectName("formatGrid")
        self.ddCheckBox = QtWidgets.QCheckBox(postbuilder)
        self.ddCheckBox.setObjectName("ddCheckBox")
        self.formatGrid.addWidget(self.ddCheckBox, 4, 2, 1, 1)
        self.dts71CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.dts71CheckBox.setObjectName("dts71CheckBox")
        self.formatGrid.addWidget(self.dts71CheckBox, 3, 1, 1, 1)
        self.truehd51CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.truehd51CheckBox.setObjectName("truehd51CheckBox")
        self.formatGrid.addWidget(self.truehd51CheckBox, 0, 2, 1, 1)
        self.ddPlusCheckBox = QtWidgets.QCheckBox(postbuilder)
        self.ddPlusCheckBox.setObjectName("ddPlusCheckBox")
        self.formatGrid.addWidget(self.ddPlusCheckBox, 4, 1, 1, 1)
        self.lpcm51CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.lpcm51CheckBox.setObjectName("lpcm51CheckBox")
        self.formatGrid.addWidget(self.lpcm51CheckBox, 5, 1, 1, 1)
        self.dts61CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.dts61CheckBox.setObjectName("dts61CheckBox")
        self.formatGrid.addWidget(self.dts61CheckBox, 3, 2, 1, 1)
        self.lpcm71CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.lpcm71CheckBox.setObjectName("lpcm71CheckBox")
        self.formatGrid.addWidget(self.lpcm71CheckBox, 5, 0, 1, 1)
        self.truehd71CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.truehd71CheckBox.setObjectName("truehd71CheckBox")
        self.formatGrid.addWidget(self.truehd71CheckBox, 0, 1, 1, 1)
        self.ddAtmosCheckBox = QtWidgets.QCheckBox(postbuilder)
        self.ddAtmosCheckBox.setObjectName("ddAtmosCheckBox")
        self.formatGrid.addWidget(self.ddAtmosCheckBox, 4, 0, 1, 1)
        self.atmosCheckBox = QtWidgets.QCheckBox(postbuilder)
        self.atmosCheckBox.setObjectName("atmosCheckBox")
        self.formatGrid.addWidget(self.atmosCheckBox, 0, 0, 1, 1)
        self.dtsxCheckBox = QtWidgets.QCheckBox(postbuilder)
        self.dtsxCheckBox.setObjectName("dtsxCheckBox")
        self.formatGrid.addWidget(self.dtsxCheckBox, 3, 0, 1, 1)
        self.dts51CheckBox = QtWidgets.QCheckBox(postbuilder)
        self.dts51CheckBox.setObjectName("dts51CheckBox")
        self.formatGrid.addWidget(self.dts51CheckBox, 3, 3, 1, 1)
        self.dataGrid.addLayout(self.formatGrid, 10, 2, 1, 1)
        self.audioValid = QtWidgets.QToolButton(postbuilder)
        self.audioValid.setText("")
        self.audioValid.setObjectName("audioValid")
        self.dataGrid.addWidget(self.audioValid, 10, 3, 1, 1)
        self.gridLayout.addLayout(self.dataGrid, 1, 0, 1, 1)

        self.retranslateUi(postbuilder)
        self.closeButton.clicked.connect(postbuilder.close)
        self.generateButton.clicked.connect(postbuilder.generate_avs_post)
        self.titleField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.yearField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.editionField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.seasonField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.noteField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.warningField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.pvaField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.sourcePicker.currentIndexChanged['QString'].connect(postbuilder.build_avs_post)
        self.spectrumField.textChanged['QString'].connect(postbuilder.build_avs_post)
        self.atmosCheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.dtsxCheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.ddAtmosCheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.lpcm71CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.truehd71CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.dts71CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.ddPlusCheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.lpcm51CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.truehd51CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.dts61CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.ddCheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.dts51CheckBox.toggled['bool'].connect(postbuilder.build_avs_post)
        self.comboBox.currentIndexChanged['int'].connect(postbuilder.post_type_changed)
        QtCore.QMetaObject.connectSlotsByName(postbuilder)
        postbuilder.setTabOrder(self.titleField, self.yearField)
        postbuilder.setTabOrder(self.yearField, self.editionField)
        postbuilder.setTabOrder(self.editionField, self.seasonField)
        postbuilder.setTabOrder(self.seasonField, self.noteField)
        postbuilder.setTabOrder(self.noteField, self.warningField)
        postbuilder.setTabOrder(self.warningField, self.sourcePicker)
        postbuilder.setTabOrder(self.sourcePicker, self.pvaField)
        postbuilder.setTabOrder(self.pvaField, self.spectrumField)
        postbuilder.setTabOrder(self.spectrumField, self.atmosCheckBox)
        postbuilder.setTabOrder(self.atmosCheckBox, self.truehd71CheckBox)
        postbuilder.setTabOrder(self.truehd71CheckBox, self.truehd51CheckBox)
        postbuilder.setTabOrder(self.truehd51CheckBox, self.dtsxCheckBox)
        postbuilder.setTabOrder(self.dtsxCheckBox, self.dts71CheckBox)
        postbuilder.setTabOrder(self.dts71CheckBox, self.dts61CheckBox)
        postbuilder.setTabOrder(self.dts61CheckBox, self.dts51CheckBox)
        postbuilder.setTabOrder(self.dts51CheckBox, self.ddAtmosCheckBox)
        postbuilder.setTabOrder(self.ddAtmosCheckBox, self.ddPlusCheckBox)
        postbuilder.setTabOrder(self.ddPlusCheckBox, self.ddCheckBox)
        postbuilder.setTabOrder(self.ddCheckBox, self.lpcm71CheckBox)
        postbuilder.setTabOrder(self.lpcm71CheckBox, self.lpcm51CheckBox)
        postbuilder.setTabOrder(self.lpcm51CheckBox, self.postTextEdit)
        postbuilder.setTabOrder(self.postTextEdit, self.generateButton)
        postbuilder.setTabOrder(self.generateButton, self.closeButton)

    def retranslateUi(self, postbuilder):
        _translate = QtCore.QCoreApplication.translate
        postbuilder.setWindowTitle(_translate("postbuilder", "AVS Post Builder"))
        self.closeButton.setText(_translate("postbuilder", "Close"))
        self.generateButton.setText(_translate("postbuilder", "Generate 2x4HD XML File"))
        self.comboBox.setItemText(0, _translate("postbuilder", "Movie"))
        self.comboBox.setItemText(1, _translate("postbuilder", "TV Show"))
        self.spectrumLabel.setText(_translate("postbuilder", "Spectrum URL"))
        self.sourcePicker.setItemText(0, _translate("postbuilder", "Disc"))
        self.sourcePicker.setItemText(1, _translate("postbuilder", "Amazon Prime"))
        self.sourcePicker.setItemText(2, _translate("postbuilder", "iTunes"))
        self.sourcePicker.setItemText(3, _translate("postbuilder", "Netflix"))
        self.postLabel.setText(_translate("postbuilder", "BEQ Post"))
        self.seasonLabel.setText(_translate("postbuilder", "TV Season"))
        self.yearLabel.setText(_translate("postbuilder", "Year"))
        self.label.setText(_translate("postbuilder", "XML File Name"))
        self.pvaLabel.setText(_translate("postbuilder", "PvA Graph URL"))
        self.formatLabel.setText(_translate("postbuilder", "Audio Format"))
        self.warningLabel.setText(_translate("postbuilder", "Warning"))
        self.noteLabel.setText(_translate("postbuilder", "Note"))
        self.editionLabel.setText(_translate("postbuilder", "Edition"))
        self.titleLabel.setText(_translate("postbuilder", "Title"))
        self.sourceLabel.setText(_translate("postbuilder", "Source"))
        self.ddCheckBox.setText(_translate("postbuilder", "DD"))
        self.dts71CheckBox.setText(_translate("postbuilder", "DTS-HD MA 7.1"))
        self.truehd51CheckBox.setText(_translate("postbuilder", "TrueHD 5.1"))
        self.ddPlusCheckBox.setText(_translate("postbuilder", "DD+"))
        self.lpcm51CheckBox.setText(_translate("postbuilder", "LPCM 5.1"))
        self.dts61CheckBox.setText(_translate("postbuilder", "DTS-HD MA 6.1"))
        self.lpcm71CheckBox.setText(_translate("postbuilder", "LPCM 7.1"))
        self.truehd71CheckBox.setText(_translate("postbuilder", "TrueHD 7.1"))
        self.ddAtmosCheckBox.setText(_translate("postbuilder", "DD+ Atmos"))
        self.atmosCheckBox.setText(_translate("postbuilder", "Atmos"))
        self.dtsxCheckBox.setText(_translate("postbuilder", "DTS:X"))
        self.dts51CheckBox.setText(_translate("postbuilder", "DTS-HD MA 5.1"))
