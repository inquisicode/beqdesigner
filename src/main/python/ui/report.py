# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saveReportDialog(object):
    def setupUi(self, saveReportDialog):
        saveReportDialog.setObjectName("saveReportDialog")
        saveReportDialog.resize(1371, 801)
        self.gridLayout_2 = QtWidgets.QGridLayout(saveReportDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QLineEdit(saveReportDialog)
        self.image.setEnabled(False)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 1, 1, 1)
        self.imagePicker = QtWidgets.QToolButton(saveReportDialog)
        self.imagePicker.setObjectName("imagePicker")
        self.gridLayout.addWidget(self.imagePicker, 0, 2, 1, 1)
        self.imageSizeLabel = QtWidgets.QLabel(saveReportDialog)
        self.imageSizeLabel.setObjectName("imageSizeLabel")
        self.gridLayout.addWidget(self.imageSizeLabel, 9, 0, 1, 1)
        self.imageLabel = QtWidgets.QLabel(saveReportDialog)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(saveReportDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 2, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(saveReportDialog)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 2, 1, 1, 1)
        self.heightLabel = QtWidgets.QLabel(saveReportDialog)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 6, 0, 1, 1)
        self.heightPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.heightPixels.setMinimum(512)
        self.heightPixels.setMaximum(8192)
        self.heightPixels.setObjectName("heightPixels")
        self.gridLayout.addWidget(self.heightPixels, 6, 1, 1, 1)
        self.filterLocationX = QtWidgets.QComboBox(saveReportDialog)
        self.filterLocationX.setObjectName("filterLocationX")
        self.filterLocationX.addItem("")
        self.filterLocationX.addItem("")
        self.gridLayout.addWidget(self.filterLocationX, 10, 1, 1, 1)
        self.filterFontSizeLabel = QtWidgets.QLabel(saveReportDialog)
        self.filterFontSizeLabel.setObjectName("filterFontSizeLabel")
        self.gridLayout.addWidget(self.filterFontSizeLabel, 7, 0, 1, 1)
        self.titleFontSizeLabel = QtWidgets.QLabel(saveReportDialog)
        self.titleFontSizeLabel.setObjectName("titleFontSizeLabel")
        self.gridLayout.addWidget(self.titleFontSizeLabel, 8, 0, 1, 1)
        self.titleFontSize = QtWidgets.QSpinBox(saveReportDialog)
        self.titleFontSize.setObjectName("titleFontSize")
        self.gridLayout.addWidget(self.titleFontSize, 8, 1, 1, 1)
        self.imageIsBackground = QtWidgets.QCheckBox(saveReportDialog)
        self.imageIsBackground.setObjectName("imageIsBackground")
        self.gridLayout.addWidget(self.imageIsBackground, 1, 1, 1, 1)
        self.filterFontSize = QtWidgets.QSpinBox(saveReportDialog)
        self.filterFontSize.setObjectName("filterFontSize")
        self.gridLayout.addWidget(self.filterFontSize, 7, 1, 1, 1)
        self.imageRatio = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.imageRatio.setDecimals(2)
        self.imageRatio.setMinimum(0.1)
        self.imageRatio.setMaximum(10.0)
        self.imageRatio.setSingleStep(0.02)
        self.imageRatio.setProperty("value", 1.0)
        self.imageRatio.setObjectName("imageRatio")
        self.gridLayout.addWidget(self.imageRatio, 9, 1, 1, 1)
        self.widthLabel = QtWidgets.QLabel(saveReportDialog)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 5, 0, 1, 1)
        self.curves = QtWidgets.QListWidget(saveReportDialog)
        self.curves.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.curves.setObjectName("curves")
        self.gridLayout.addWidget(self.curves, 4, 1, 1, 1)
        self.curvesLabel = QtWidgets.QLabel(saveReportDialog)
        self.curvesLabel.setObjectName("curvesLabel")
        self.gridLayout.addWidget(self.curvesLabel, 4, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(saveReportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 13, 0, 1, 3)
        self.filterLocationLabel = QtWidgets.QLabel(saveReportDialog)
        self.filterLocationLabel.setObjectName("filterLocationLabel")
        self.gridLayout.addWidget(self.filterLocationLabel, 10, 0, 1, 1)
        self.widthPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.widthPixels.setMinimum(512)
        self.widthPixels.setMaximum(8192)
        self.widthPixels.setObjectName("widthPixels")
        self.gridLayout.addWidget(self.widthPixels, 5, 1, 1, 1)
        self.filterLocationY = QtWidgets.QComboBox(saveReportDialog)
        self.filterLocationY.setObjectName("filterLocationY")
        self.filterLocationY.addItem("")
        self.filterLocationY.addItem("")
        self.gridLayout.addWidget(self.filterLocationY, 11, 1, 1, 1)
        self.showLegend = QtWidgets.QCheckBox(saveReportDialog)
        self.showLegend.setObjectName("showLegend")
        self.gridLayout.addWidget(self.showLegend, 12, 1, 1, 2)
        self.limitsButton = QtWidgets.QToolButton(saveReportDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.gridLayout.addWidget(self.limitsButton, 5, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.preview = MplWidget(saveReportDialog)
        self.preview.setObjectName("preview")
        self.horizontalLayout.addWidget(self.preview)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(saveReportDialog)
        self.buttonBox.accepted.connect(saveReportDialog.accept)
        self.buttonBox.rejected.connect(saveReportDialog.reject)
        self.curves.itemSelectionChanged.connect(saveReportDialog.set_selected)
        self.widthPixels.valueChanged['int'].connect(saveReportDialog.update_height)
        self.showLegend.clicked.connect(saveReportDialog.redraw)
        self.imagePicker.clicked.connect(saveReportDialog.choose_image)
        self.title.textChanged['QString'].connect(saveReportDialog.set_title)
        self.imageIsBackground.clicked.connect(saveReportDialog.redraw_all_axes)
        self.filterFontSize.valueChanged['int'].connect(saveReportDialog.set_table_font_size)
        self.titleFontSize.valueChanged['int'].connect(saveReportDialog.set_title)
        self.imageRatio.valueChanged['double'].connect(saveReportDialog.redraw_all_axes)
        self.filterLocationX.currentIndexChanged['int'].connect(saveReportDialog.redraw_all_axes)
        self.filterLocationY.currentIndexChanged['int'].connect(saveReportDialog.redraw_all_axes)
        self.limitsButton.clicked.connect(saveReportDialog.show_limits)
        QtCore.QMetaObject.connectSlotsByName(saveReportDialog)

    def retranslateUi(self, saveReportDialog):
        _translate = QtCore.QCoreApplication.translate
        saveReportDialog.setWindowTitle(_translate("saveReportDialog", "Save Report"))
        self.imagePicker.setText(_translate("saveReportDialog", "..."))
        self.imageSizeLabel.setText(_translate("saveReportDialog", "Image Ratio"))
        self.imageLabel.setText(_translate("saveReportDialog", "Image"))
        self.titleLabel.setText(_translate("saveReportDialog", "Title"))
        self.heightLabel.setText(_translate("saveReportDialog", "Height"))
        self.filterLocationX.setItemText(0, _translate("saveReportDialog", "Right"))
        self.filterLocationX.setItemText(1, _translate("saveReportDialog", "Left"))
        self.filterFontSizeLabel.setText(_translate("saveReportDialog", "Filter Font Size"))
        self.titleFontSizeLabel.setText(_translate("saveReportDialog", "Title Font Size"))
        self.imageIsBackground.setText(_translate("saveReportDialog", "Use Image as Background"))
        self.widthLabel.setText(_translate("saveReportDialog", "Width"))
        self.curvesLabel.setText(_translate("saveReportDialog", "Curves"))
        self.filterLocationLabel.setText(_translate("saveReportDialog", "Filter Location"))
        self.filterLocationY.setItemText(0, _translate("saveReportDialog", "Top"))
        self.filterLocationY.setItemText(1, _translate("saveReportDialog", "Bottom"))
        self.showLegend.setText(_translate("saveReportDialog", "Show Legend?"))
        self.limitsButton.setText(_translate("saveReportDialog", "..."))

from mpl import MplWidget
