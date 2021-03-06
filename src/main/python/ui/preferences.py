# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.resize(375, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(preferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panes = QtWidgets.QVBoxLayout()
        self.panes.setObjectName("panes")
        self.toolBox = QtWidgets.QToolBox(preferencesDialog)
        self.toolBox.setObjectName("toolBox")
        self.binariesPage = QtWidgets.QWidget()
        self.binariesPage.setGeometry(QtCore.QRect(0, 0, 152, 86))
        self.binariesPage.setObjectName("binariesPage")
        self.binariesPane = QtWidgets.QGridLayout(self.binariesPage)
        self.binariesPane.setObjectName("binariesPane")
        self.ffmpegDirectory = QtWidgets.QLineEdit(self.binariesPage)
        self.ffmpegDirectory.setEnabled(False)
        self.ffmpegDirectory.setObjectName("ffmpegDirectory")
        self.binariesPane.addWidget(self.ffmpegDirectory, 0, 1, 1, 1)
        self.ffmpegLabel = QtWidgets.QLabel(self.binariesPage)
        self.ffmpegLabel.setObjectName("ffmpegLabel")
        self.binariesPane.addWidget(self.ffmpegLabel, 0, 0, 1, 1)
        self.ffmpegDirectoryPicker = QtWidgets.QToolButton(self.binariesPage)
        self.ffmpegDirectoryPicker.setObjectName("ffmpegDirectoryPicker")
        self.binariesPane.addWidget(self.ffmpegDirectoryPicker, 0, 2, 1, 1)
        self.ffprobeLabel = QtWidgets.QLabel(self.binariesPage)
        self.ffprobeLabel.setObjectName("ffprobeLabel")
        self.binariesPane.addWidget(self.ffprobeLabel, 1, 0, 1, 1)
        self.ffprobeDirectory = QtWidgets.QLineEdit(self.binariesPage)
        self.ffprobeDirectory.setEnabled(False)
        self.ffprobeDirectory.setObjectName("ffprobeDirectory")
        self.binariesPane.addWidget(self.ffprobeDirectory, 1, 1, 1, 1)
        self.ffprobeDirectoryPicker = QtWidgets.QToolButton(self.binariesPage)
        self.ffprobeDirectoryPicker.setObjectName("ffprobeDirectoryPicker")
        self.binariesPane.addWidget(self.ffprobeDirectoryPicker, 1, 2, 1, 1)
        self.toolBox.addItem(self.binariesPage, "")
        self.analysisPage = QtWidgets.QWidget()
        self.analysisPage.setGeometry(QtCore.QRect(0, 0, 185, 158))
        self.analysisPage.setObjectName("analysisPage")
        self.analysisPane = QtWidgets.QGridLayout(self.analysisPage)
        self.analysisPane.setObjectName("analysisPane")
        self.peakAnalysisWindow = QtWidgets.QComboBox(self.analysisPage)
        self.peakAnalysisWindow.setObjectName("peakAnalysisWindow")
        self.analysisPane.addWidget(self.peakAnalysisWindow, 3, 1, 1, 1)
        self.peakAnalysisWindowLabel = QtWidgets.QLabel(self.analysisPage)
        self.peakAnalysisWindowLabel.setObjectName("peakAnalysisWindowLabel")
        self.analysisPane.addWidget(self.peakAnalysisWindowLabel, 3, 0, 1, 1)
        self.avgAnalysisWindowLabel = QtWidgets.QLabel(self.analysisPage)
        self.avgAnalysisWindowLabel.setObjectName("avgAnalysisWindowLabel")
        self.analysisPane.addWidget(self.avgAnalysisWindowLabel, 2, 0, 1, 1)
        self.avgAnalysisWindow = QtWidgets.QComboBox(self.analysisPage)
        self.avgAnalysisWindow.setObjectName("avgAnalysisWindow")
        self.analysisPane.addWidget(self.avgAnalysisWindow, 2, 1, 1, 1)
        self.targetFsLabel = QtWidgets.QLabel(self.analysisPage)
        self.targetFsLabel.setObjectName("targetFsLabel")
        self.analysisPane.addWidget(self.targetFsLabel, 0, 0, 1, 1)
        self.targetFs = QtWidgets.QComboBox(self.analysisPage)
        self.targetFs.setObjectName("targetFs")
        self.targetFs.addItem("")
        self.targetFs.addItem("")
        self.targetFs.addItem("")
        self.targetFs.addItem("")
        self.targetFs.addItem("")
        self.targetFs.addItem("")
        self.analysisPane.addWidget(self.targetFs, 0, 1, 1, 1)
        self.resolutionLabel = QtWidgets.QLabel(self.analysisPage)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.analysisPane.addWidget(self.resolutionLabel, 1, 0, 1, 1)
        self.resolutionSelect = QtWidgets.QComboBox(self.analysisPage)
        self.resolutionSelect.setObjectName("resolutionSelect")
        self.resolutionSelect.addItem("")
        self.resolutionSelect.addItem("")
        self.resolutionSelect.addItem("")
        self.resolutionSelect.addItem("")
        self.resolutionSelect.addItem("")
        self.analysisPane.addWidget(self.resolutionSelect, 1, 1, 1, 1)
        self.analysisPane.setColumnStretch(1, 1)
        self.toolBox.addItem(self.analysisPage, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 344, 146))
        self.widget.setObjectName("widget")
        self.extractPane = QtWidgets.QGridLayout(self.widget)
        self.extractPane.setObjectName("extractPane")
        self.defaultOutputDirectoryLabel = QtWidgets.QLabel(self.widget)
        self.defaultOutputDirectoryLabel.setObjectName("defaultOutputDirectoryLabel")
        self.extractPane.addWidget(self.defaultOutputDirectoryLabel, 0, 0, 1, 1)
        self.defaultOutputDirectory = QtWidgets.QLineEdit(self.widget)
        self.defaultOutputDirectory.setEnabled(False)
        self.defaultOutputDirectory.setObjectName("defaultOutputDirectory")
        self.extractPane.addWidget(self.defaultOutputDirectory, 0, 1, 1, 1)
        self.defaultOutputDirectoryPicker = QtWidgets.QToolButton(self.widget)
        self.defaultOutputDirectoryPicker.setObjectName("defaultOutputDirectoryPicker")
        self.extractPane.addWidget(self.defaultOutputDirectoryPicker, 0, 2, 1, 1)
        self.extractCompleteAudioFileLabel = QtWidgets.QLabel(self.widget)
        self.extractCompleteAudioFileLabel.setObjectName("extractCompleteAudioFileLabel")
        self.extractPane.addWidget(self.extractCompleteAudioFileLabel, 1, 0, 1, 1)
        self.extractCompleteAudioFile = QtWidgets.QLineEdit(self.widget)
        self.extractCompleteAudioFile.setEnabled(False)
        self.extractCompleteAudioFile.setObjectName("extractCompleteAudioFile")
        self.extractPane.addWidget(self.extractCompleteAudioFile, 1, 1, 1, 1)
        self.extractCompleteAudioFilePicker = QtWidgets.QToolButton(self.widget)
        self.extractCompleteAudioFilePicker.setObjectName("extractCompleteAudioFilePicker")
        self.extractPane.addWidget(self.extractCompleteAudioFilePicker, 1, 2, 1, 1)
        self.extractOptions1 = QtWidgets.QHBoxLayout()
        self.extractOptions1.setObjectName("extractOptions1")
        self.includeOriginal = QtWidgets.QCheckBox(self.widget)
        self.includeOriginal.setObjectName("includeOriginal")
        self.extractOptions1.addWidget(self.includeOriginal)
        self.compress = QtWidgets.QCheckBox(self.widget)
        self.compress.setObjectName("compress")
        self.extractOptions1.addWidget(self.compress)
        self.extractPane.addLayout(self.extractOptions1, 2, 0, 1, 3)
        self.extractOptions2 = QtWidgets.QHBoxLayout()
        self.extractOptions2.setObjectName("extractOptions2")
        self.monoMix = QtWidgets.QCheckBox(self.widget)
        self.monoMix.setObjectName("monoMix")
        self.extractOptions2.addWidget(self.monoMix)
        self.decimate = QtWidgets.QCheckBox(self.widget)
        self.decimate.setObjectName("decimate")
        self.extractOptions2.addWidget(self.decimate)
        self.includeSubtitles = QtWidgets.QCheckBox(self.widget)
        self.includeSubtitles.setObjectName("includeSubtitles")
        self.extractOptions2.addWidget(self.includeSubtitles)
        self.extractPane.addLayout(self.extractOptions2, 3, 0, 1, 3)
        self.toolBox.addItem(self.widget, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setGeometry(QtCore.QRect(0, 0, 222, 100))
        self.widget1.setObjectName("widget1")
        self.stylePane = QtWidgets.QGridLayout(self.widget1)
        self.stylePane.setObjectName("stylePane")
        self.themeLabel = QtWidgets.QLabel(self.widget1)
        self.themeLabel.setObjectName("themeLabel")
        self.stylePane.addWidget(self.themeLabel, 0, 0, 1, 1)
        self.themePicker = QtWidgets.QComboBox(self.widget1)
        self.themePicker.setObjectName("themePicker")
        self.themePicker.addItem("")
        self.stylePane.addWidget(self.themePicker, 0, 1, 1, 1)
        self.speclabLineStyle = QtWidgets.QCheckBox(self.widget1)
        self.speclabLineStyle.setObjectName("speclabLineStyle")
        self.stylePane.addWidget(self.speclabLineStyle, 1, 1, 1, 1)
        self.smoothGraphs = QtWidgets.QCheckBox(self.widget1)
        self.smoothGraphs.setObjectName("smoothGraphs")
        self.stylePane.addWidget(self.smoothGraphs, 2, 1, 1, 1)
        self.stylePane.setColumnStretch(1, 1)
        self.toolBox.addItem(self.widget1, "")
        self.graphPage = QtWidgets.QWidget()
        self.graphPage.setGeometry(QtCore.QRect(0, 0, 239, 130))
        self.graphPage.setObjectName("graphPage")
        self.graphPane = QtWidgets.QVBoxLayout(self.graphPage)
        self.graphPane.setObjectName("graphPane")
        self.freqIsLogScale = QtWidgets.QCheckBox(self.graphPage)
        self.freqIsLogScale.setChecked(True)
        self.freqIsLogScale.setObjectName("freqIsLogScale")
        self.graphPane.addWidget(self.freqIsLogScale)
        self.precalcSmoothing = QtWidgets.QCheckBox(self.graphPage)
        self.precalcSmoothing.setChecked(True)
        self.precalcSmoothing.setObjectName("precalcSmoothing")
        self.graphPane.addWidget(self.precalcSmoothing)
        self.expandYLimits = QtWidgets.QCheckBox(self.graphPage)
        self.expandYLimits.setObjectName("expandYLimits")
        self.graphPane.addWidget(self.expandYLimits)
        self.xminmaxLayout = QtWidgets.QHBoxLayout()
        self.xminmaxLayout.setObjectName("xminmaxLayout")
        self.xminmaxLabel = QtWidgets.QLabel(self.graphPage)
        self.xminmaxLabel.setObjectName("xminmaxLabel")
        self.xminmaxLayout.addWidget(self.xminmaxLabel)
        self.xmin = QtWidgets.QSpinBox(self.graphPage)
        self.xmin.setMinimum(1)
        self.xmin.setMaximum(23999)
        self.xmin.setProperty("value", 2)
        self.xmin.setObjectName("xmin")
        self.xminmaxLayout.addWidget(self.xmin)
        self.xmax = QtWidgets.QSpinBox(self.graphPage)
        self.xmax.setMinimum(2)
        self.xmax.setMaximum(24000)
        self.xmax.setProperty("value", 160)
        self.xmax.setObjectName("xmax")
        self.xminmaxLayout.addWidget(self.xmax)
        self.graphPane.addLayout(self.xminmaxLayout)
        self.toolBox.addItem(self.graphPage, "")
        self.filterPage = QtWidgets.QWidget()
        self.filterPage.setGeometry(QtCore.QRect(0, 0, 173, 120))
        self.filterPage.setObjectName("filterPage")
        self.filterPane = QtWidgets.QGridLayout(self.filterPage)
        self.filterPane.setObjectName("filterPane")
        self.filterQLabel = QtWidgets.QLabel(self.filterPage)
        self.filterQLabel.setObjectName("filterQLabel")
        self.filterPane.addWidget(self.filterQLabel, 0, 0, 1, 1)
        self.bmlpfFreq = QtWidgets.QSpinBox(self.filterPage)
        self.bmlpfFreq.setMinimum(20)
        self.bmlpfFreq.setMaximum(160)
        self.bmlpfFreq.setProperty("value", 80)
        self.bmlpfFreq.setObjectName("bmlpfFreq")
        self.filterPane.addWidget(self.bmlpfFreq, 2, 1, 1, 1)
        self.filterFreq = QtWidgets.QSpinBox(self.filterPage)
        self.filterFreq.setMinimum(1)
        self.filterFreq.setMaximum(24000)
        self.filterFreq.setObjectName("filterFreq")
        self.filterPane.addWidget(self.filterFreq, 1, 1, 1, 1)
        self.filterQ = QtWidgets.QDoubleSpinBox(self.filterPage)
        self.filterQ.setDecimals(3)
        self.filterQ.setMinimum(0.001)
        self.filterQ.setSingleStep(0.001)
        self.filterQ.setObjectName("filterQ")
        self.filterPane.addWidget(self.filterQ, 0, 1, 1, 1)
        self.filterFreqLabel = QtWidgets.QLabel(self.filterPage)
        self.filterFreqLabel.setObjectName("filterFreqLabel")
        self.filterPane.addWidget(self.filterFreqLabel, 1, 0, 1, 1)
        self.bmlpfLabel = QtWidgets.QLabel(self.filterPage)
        self.bmlpfLabel.setObjectName("bmlpfLabel")
        self.filterPane.addWidget(self.bmlpfLabel, 2, 0, 1, 1)
        self.filterPane.setColumnStretch(1, 1)
        self.toolBox.addItem(self.filterPage, "")
        self.systemPage = QtWidgets.QWidget()
        self.systemPage.setGeometry(QtCore.QRect(0, 0, 225, 62))
        self.systemPage.setObjectName("systemPage")
        self.systemPane = QtWidgets.QGridLayout(self.systemPage)
        self.systemPane.setObjectName("systemPane")
        self.checkForBetaUpdates = QtWidgets.QCheckBox(self.systemPage)
        self.checkForBetaUpdates.setObjectName("checkForBetaUpdates")
        self.systemPane.addWidget(self.checkForBetaUpdates, 1, 0, 1, 1)
        self.checkForUpdates = QtWidgets.QCheckBox(self.systemPage)
        self.checkForUpdates.setChecked(True)
        self.checkForUpdates.setObjectName("checkForUpdates")
        self.systemPane.addWidget(self.checkForUpdates, 0, 0, 1, 1)
        self.toolBox.addItem(self.systemPage, "")
        self.beqPage = QtWidgets.QWidget()
        self.beqPage.setGeometry(QtCore.QRect(0, 0, 361, 175))
        self.beqPage.setObjectName("beqPage")
        self.beqPane = QtWidgets.QGridLayout(self.beqPage)
        self.beqPane.setObjectName("beqPane")
        self.beqDirectoryLabel = QtWidgets.QLabel(self.beqPage)
        self.beqDirectoryLabel.setObjectName("beqDirectoryLabel")
        self.beqPane.addWidget(self.beqDirectoryLabel, 0, 0, 1, 1)
        self.beqFiltersDir = QtWidgets.QLineEdit(self.beqPage)
        self.beqFiltersDir.setReadOnly(True)
        self.beqFiltersDir.setObjectName("beqFiltersDir")
        self.beqPane.addWidget(self.beqFiltersDir, 0, 1, 1, 1)
        self.beqDirectoryPicker = QtWidgets.QToolButton(self.beqPage)
        self.beqDirectoryPicker.setObjectName("beqDirectoryPicker")
        self.beqPane.addWidget(self.beqDirectoryPicker, 0, 2, 1, 1)
        self.repoURLLabel = QtWidgets.QLabel(self.beqPage)
        self.repoURLLabel.setObjectName("repoURLLabel")
        self.beqPane.addWidget(self.repoURLLabel, 1, 0, 1, 1)
        self.repoURL = QtWidgets.QLineEdit(self.beqPage)
        self.repoURL.setObjectName("repoURL")
        self.beqPane.addWidget(self.repoURL, 1, 1, 1, 1)
        self.addRepoButton = QtWidgets.QToolButton(self.beqPage)
        self.addRepoButton.setObjectName("addRepoButton")
        self.beqPane.addWidget(self.addRepoButton, 1, 2, 1, 1)
        self.beqRepos = QtWidgets.QComboBox(self.beqPage)
        self.beqRepos.setObjectName("beqRepos")
        self.beqPane.addWidget(self.beqRepos, 2, 1, 1, 1)
        self.deleteRepoButton = QtWidgets.QToolButton(self.beqPage)
        self.deleteRepoButton.setObjectName("deleteRepoButton")
        self.beqPane.addWidget(self.deleteRepoButton, 2, 2, 1, 1)
        self.filteredLoadedLabel = QtWidgets.QLabel(self.beqPage)
        self.filteredLoadedLabel.setObjectName("filteredLoadedLabel")
        self.beqPane.addWidget(self.filteredLoadedLabel, 3, 0, 1, 1)
        self.beqFiltersCount = QtWidgets.QSpinBox(self.beqPage)
        self.beqFiltersCount.setEnabled(False)
        self.beqFiltersCount.setMaximum(100000)
        self.beqFiltersCount.setObjectName("beqFiltersCount")
        self.beqPane.addWidget(self.beqFiltersCount, 3, 1, 1, 1)
        self.refreshBeq = QtWidgets.QToolButton(self.beqPage)
        self.refreshBeq.setObjectName("refreshBeq")
        self.beqPane.addWidget(self.refreshBeq, 3, 2, 1, 1)
        self.beqReposLabel = QtWidgets.QLabel(self.beqPage)
        self.beqReposLabel.setObjectName("beqReposLabel")
        self.beqPane.addWidget(self.beqReposLabel, 2, 0, 1, 1)
        self.toolBox.addItem(self.beqPage, "")
        self.panes.addWidget(self.toolBox)
        self.verticalLayout.addLayout(self.panes)
        self.buttonBox = QtWidgets.QDialogButtonBox(preferencesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(preferencesDialog)
        self.toolBox.setCurrentIndex(7)
        self.buttonBox.accepted.connect(preferencesDialog.accept)
        self.buttonBox.rejected.connect(preferencesDialog.reject)
        self.ffmpegDirectoryPicker.clicked.connect(preferencesDialog.showFfmpegDirectoryPicker)
        self.ffprobeDirectoryPicker.clicked.connect(preferencesDialog.showFfprobeDirectoryPicker)
        self.defaultOutputDirectoryPicker.clicked.connect(preferencesDialog.showDefaultOutputDirectoryPicker)
        self.extractCompleteAudioFilePicker.clicked.connect(preferencesDialog.showExtractCompleteSoundPicker)
        self.beqDirectoryPicker.clicked.connect(preferencesDialog.showBeqDirectoryPicker)
        self.refreshBeq.clicked.connect(preferencesDialog.updateBeq)
        self.addRepoButton.clicked.connect(preferencesDialog.add_beq_repo)
        self.deleteRepoButton.clicked.connect(preferencesDialog.remove_beq_repo)
        self.repoURL.textChanged['QString'].connect(preferencesDialog.validate_beq_repo)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)
        preferencesDialog.setTabOrder(self.ffmpegDirectory, self.ffmpegDirectoryPicker)
        preferencesDialog.setTabOrder(self.ffmpegDirectoryPicker, self.ffprobeDirectory)
        preferencesDialog.setTabOrder(self.ffprobeDirectory, self.ffprobeDirectoryPicker)
        preferencesDialog.setTabOrder(self.ffprobeDirectoryPicker, self.targetFs)
        preferencesDialog.setTabOrder(self.targetFs, self.resolutionSelect)
        preferencesDialog.setTabOrder(self.resolutionSelect, self.avgAnalysisWindow)
        preferencesDialog.setTabOrder(self.avgAnalysisWindow, self.peakAnalysisWindow)
        preferencesDialog.setTabOrder(self.peakAnalysisWindow, self.defaultOutputDirectory)
        preferencesDialog.setTabOrder(self.defaultOutputDirectory, self.defaultOutputDirectoryPicker)
        preferencesDialog.setTabOrder(self.defaultOutputDirectoryPicker, self.extractCompleteAudioFile)
        preferencesDialog.setTabOrder(self.extractCompleteAudioFile, self.extractCompleteAudioFilePicker)
        preferencesDialog.setTabOrder(self.extractCompleteAudioFilePicker, self.includeOriginal)
        preferencesDialog.setTabOrder(self.includeOriginal, self.compress)
        preferencesDialog.setTabOrder(self.compress, self.monoMix)
        preferencesDialog.setTabOrder(self.monoMix, self.decimate)
        preferencesDialog.setTabOrder(self.decimate, self.includeSubtitles)
        preferencesDialog.setTabOrder(self.includeSubtitles, self.themePicker)
        preferencesDialog.setTabOrder(self.themePicker, self.speclabLineStyle)
        preferencesDialog.setTabOrder(self.speclabLineStyle, self.smoothGraphs)
        preferencesDialog.setTabOrder(self.smoothGraphs, self.freqIsLogScale)
        preferencesDialog.setTabOrder(self.freqIsLogScale, self.precalcSmoothing)
        preferencesDialog.setTabOrder(self.precalcSmoothing, self.expandYLimits)
        preferencesDialog.setTabOrder(self.expandYLimits, self.xmin)
        preferencesDialog.setTabOrder(self.xmin, self.xmax)
        preferencesDialog.setTabOrder(self.xmax, self.filterQ)
        preferencesDialog.setTabOrder(self.filterQ, self.filterFreq)
        preferencesDialog.setTabOrder(self.filterFreq, self.bmlpfFreq)
        preferencesDialog.setTabOrder(self.bmlpfFreq, self.checkForUpdates)
        preferencesDialog.setTabOrder(self.checkForUpdates, self.checkForBetaUpdates)
        preferencesDialog.setTabOrder(self.checkForBetaUpdates, self.beqFiltersDir)
        preferencesDialog.setTabOrder(self.beqFiltersDir, self.beqDirectoryPicker)
        preferencesDialog.setTabOrder(self.beqDirectoryPicker, self.beqFiltersCount)
        preferencesDialog.setTabOrder(self.beqFiltersCount, self.refreshBeq)

    def retranslateUi(self, preferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        preferencesDialog.setWindowTitle(_translate("preferencesDialog", "Preferences"))
        self.ffmpegLabel.setText(_translate("preferencesDialog", "ffmpeg"))
        self.ffmpegDirectoryPicker.setText(_translate("preferencesDialog", "..."))
        self.ffprobeLabel.setText(_translate("preferencesDialog", "ffprobe"))
        self.ffprobeDirectoryPicker.setText(_translate("preferencesDialog", "..."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.binariesPage), _translate("preferencesDialog", "Binaries"))
        self.peakAnalysisWindowLabel.setText(_translate("preferencesDialog", "Peak Window"))
        self.avgAnalysisWindowLabel.setText(_translate("preferencesDialog", "Avg Window"))
        self.targetFsLabel.setText(_translate("preferencesDialog", "Target Fs"))
        self.targetFs.setItemText(0, _translate("preferencesDialog", "250 Hz"))
        self.targetFs.setItemText(1, _translate("preferencesDialog", "500 Hz"))
        self.targetFs.setItemText(2, _translate("preferencesDialog", "1000 Hz"))
        self.targetFs.setItemText(3, _translate("preferencesDialog", "2000 Hz"))
        self.targetFs.setItemText(4, _translate("preferencesDialog", "4000 Hz"))
        self.targetFs.setItemText(5, _translate("preferencesDialog", "8000 Hz"))
        self.resolutionLabel.setText(_translate("preferencesDialog", "Resolution"))
        self.resolutionSelect.setCurrentText(_translate("preferencesDialog", "0.25 Hz"))
        self.resolutionSelect.setItemText(0, _translate("preferencesDialog", "0.25 Hz"))
        self.resolutionSelect.setItemText(1, _translate("preferencesDialog", "0.5 Hz"))
        self.resolutionSelect.setItemText(2, _translate("preferencesDialog", "1.0 Hz"))
        self.resolutionSelect.setItemText(3, _translate("preferencesDialog", "2.0 Hz"))
        self.resolutionSelect.setItemText(4, _translate("preferencesDialog", "4.0 Hz"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.analysisPage), _translate("preferencesDialog", "Analysis"))
        self.defaultOutputDirectoryLabel.setText(_translate("preferencesDialog", "Default Output Directory"))
        self.defaultOutputDirectoryPicker.setText(_translate("preferencesDialog", "..."))
        self.extractCompleteAudioFileLabel.setText(_translate("preferencesDialog", "Extract Complete Sound"))
        self.extractCompleteAudioFilePicker.setText(_translate("preferencesDialog", "..."))
        self.includeOriginal.setText(_translate("preferencesDialog", "Add Original Audio?"))
        self.compress.setText(_translate("preferencesDialog", "Compress Audio?"))
        self.monoMix.setText(_translate("preferencesDialog", "Mix to mono?"))
        self.decimate.setText(_translate("preferencesDialog", "Decimate?"))
        self.includeSubtitles.setText(_translate("preferencesDialog", "Add Subtitles?"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), _translate("preferencesDialog", "Extraction"))
        self.themeLabel.setText(_translate("preferencesDialog", "Theme"))
        self.themePicker.setItemText(0, _translate("preferencesDialog", "default"))
        self.speclabLineStyle.setText(_translate("preferencesDialog", "Speclab Line Colours?"))
        self.smoothGraphs.setText(_translate("preferencesDialog", "Smooth?"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget1), _translate("preferencesDialog", "Style"))
        self.freqIsLogScale.setText(_translate("preferencesDialog", "Frequency Axis Log Scale?"))
        self.precalcSmoothing.setText(_translate("preferencesDialog", "Precalculate Octave Smoothing?"))
        self.expandYLimits.setText(_translate("preferencesDialog", "Auto Expand Y Limits?"))
        self.xminmaxLabel.setText(_translate("preferencesDialog", "x min/max"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.graphPage), _translate("preferencesDialog", "Graph"))
        self.filterQLabel.setText(_translate("preferencesDialog", "Default Q"))
        self.bmlpfFreq.setSuffix(_translate("preferencesDialog", " Hz"))
        self.filterFreqLabel.setText(_translate("preferencesDialog", "Default Freq"))
        self.bmlpfLabel.setText(_translate("preferencesDialog", "BM LPF"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.filterPage), _translate("preferencesDialog", "Filters"))
        self.checkForBetaUpdates.setText(_translate("preferencesDialog", "Include Beta Versions?"))
        self.checkForUpdates.setText(_translate("preferencesDialog", "Check for Updates on startup?"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.systemPage), _translate("preferencesDialog", "System"))
        self.beqDirectoryLabel.setText(_translate("preferencesDialog", "Directory"))
        self.beqDirectoryPicker.setText(_translate("preferencesDialog", "..."))
        self.repoURLLabel.setText(_translate("preferencesDialog", "New Repo"))
        self.addRepoButton.setText(_translate("preferencesDialog", "..."))
        self.deleteRepoButton.setText(_translate("preferencesDialog", "..."))
        self.filteredLoadedLabel.setText(_translate("preferencesDialog", "Filter Count"))
        self.refreshBeq.setText(_translate("preferencesDialog", "..."))
        self.beqReposLabel.setText(_translate("preferencesDialog", "Repos"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.beqPage), _translate("preferencesDialog", "BEQ"))
