# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmContour.ui'
#
# Created: Tue Jan 11 14:31:54 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ContourDialog(object):
    def setupUi(self, ContourDialog):
        ContourDialog.setObjectName("ContourDialog")
        ContourDialog.setWindowModality(QtCore.Qt.NonModal)
        ContourDialog.resize(506, 508)
        ContourDialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtGui.QGridLayout(ContourDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtGui.QGroupBox(ContourDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.uLayerName = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLayerName.sizePolicy().hasHeightForWidth())
        self.uLayerName.setSizePolicy(sizePolicy)
        self.uLayerName.setStatusTip("")
        self.uLayerName.setObjectName("uLayerName")
        self.horizontalLayout_4.addWidget(self.uLayerName)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.uFieldName = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uFieldName.sizePolicy().hasHeightForWidth())
        self.uFieldName.setSizePolicy(sizePolicy)
        self.uFieldName.setObjectName("uFieldName")
        self.horizontalLayout_5.addWidget(self.uFieldName)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.uLayerDescription = QtGui.QLabel(self.groupBox_2)
        self.uLayerDescription.setText("")
        self.uLayerDescription.setObjectName("uLayerDescription")
        self.gridLayout.addWidget(self.uLayerDescription, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(ContourDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uLinesContours = QtGui.QRadioButton(self.groupBox)
        self.uLinesContours.setObjectName("uLinesContours")
        self.horizontalLayout_7.addWidget(self.uLinesContours)
        self.uFilledContours = QtGui.QRadioButton(self.groupBox)
        self.uFilledContours.setObjectName("uFilledContours")
        self.horizontalLayout_7.addWidget(self.uFilledContours)
        self.uBoth = QtGui.QRadioButton(self.groupBox)
        self.uBoth.setObjectName("uBoth")
        self.horizontalLayout_7.addWidget(self.uBoth)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 3)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.uLevelsNumber = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLevelsNumber.sizePolicy().hasHeightForWidth())
        self.uLevelsNumber.setSizePolicy(sizePolicy)
        self.uLevelsNumber.setMinimum(1)
        self.uLevelsNumber.setMaximum(999)
        self.uLevelsNumber.setObjectName("uLevelsNumber")
        self.gridLayout_2.addWidget(self.uLevelsNumber, 1, 1, 1, 1)
        self.uLevelsList = QtGui.QListWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uLevelsList.sizePolicy().hasHeightForWidth())
        self.uLevelsList.setSizePolicy(sizePolicy)
        self.uLevelsList.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uLevelsList.setObjectName("uLevelsList")
        self.gridLayout_2.addWidget(self.uLevelsList, 1, 2, 5, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.uMinContour = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMinContour.sizePolicy().hasHeightForWidth())
        self.uMinContour.setSizePolicy(sizePolicy)
        self.uMinContour.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uMinContour.setDecimals(4)
        self.uMinContour.setMinimum(-999999999.0)
        self.uMinContour.setMaximum(999999999.0)
        self.uMinContour.setObjectName("uMinContour")
        self.gridLayout_2.addWidget(self.uMinContour, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.uMaxContour = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMaxContour.sizePolicy().hasHeightForWidth())
        self.uMaxContour.setSizePolicy(sizePolicy)
        self.uMaxContour.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uMaxContour.setDecimals(4)
        self.uMaxContour.setMinimum(-999999999.0)
        self.uMaxContour.setMaximum(999999999.0)
        self.uMaxContour.setObjectName("uMaxContour")
        self.gridLayout_2.addWidget(self.uMaxContour, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.uExtend = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uExtend.sizePolicy().hasHeightForWidth())
        self.uExtend.setSizePolicy(sizePolicy)
        self.uExtend.setObjectName("uExtend")
        self.uExtend.addItem("")
        self.uExtend.addItem("")
        self.uExtend.addItem("")
        self.uExtend.addItem("")
        self.gridLayout_2.addWidget(self.uExtend, 4, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.uMethod = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uMethod.sizePolicy().hasHeightForWidth())
        self.uMethod.setSizePolicy(sizePolicy)
        self.uMethod.setObjectName("uMethod")
        self.uMethod.addItem("")
        self.uMethod.addItem("")
        self.gridLayout_2.addWidget(self.uMethod, 5, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(ContourDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.uOutputName = QtGui.QLineEdit(self.groupBox_3)
        self.uOutputName.setObjectName("uOutputName")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.uOutputName)
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.uPrecision = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uPrecision.sizePolicy().hasHeightForWidth())
        self.uPrecision.setSizePolicy(sizePolicy)
        self.uPrecision.setMinimum(0)
        self.uPrecision.setMaximum(4)
        self.uPrecision.setProperty("value", 4)
        self.uPrecision.setObjectName("uPrecision")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.uPrecision)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(ContourDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 1)
        self.uButtonBox = QtGui.QDialogButtonBox(ContourDialog)
        self.uButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.uButtonBox.setObjectName("uButtonBox")
        self.gridLayout_3.addWidget(self.uButtonBox, 3, 1, 1, 1)
        self.label_3.setBuddy(self.uLayerName)
        self.label_4.setBuddy(self.uFieldName)
        self.label.setBuddy(self.uLevelsNumber)

        self.retranslateUi(ContourDialog)
        QtCore.QObject.connect(self.uButtonBox, QtCore.SIGNAL("accepted()"), ContourDialog.accept)
        QtCore.QObject.connect(self.uButtonBox, QtCore.SIGNAL("rejected()"), ContourDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ContourDialog)
        ContourDialog.setTabOrder(self.uLayerName, self.uFieldName)
        ContourDialog.setTabOrder(self.uFieldName, self.uLinesContours)
        ContourDialog.setTabOrder(self.uLinesContours, self.uFilledContours)
        ContourDialog.setTabOrder(self.uFilledContours, self.uBoth)
        ContourDialog.setTabOrder(self.uBoth, self.uLevelsNumber)
        ContourDialog.setTabOrder(self.uLevelsNumber, self.uMinContour)
        ContourDialog.setTabOrder(self.uMinContour, self.uMaxContour)
        ContourDialog.setTabOrder(self.uMaxContour, self.uLevelsList)
        ContourDialog.setTabOrder(self.uLevelsList, self.uButtonBox)

    def retranslateUi(self, ContourDialog):
        ContourDialog.setWindowTitle(QtGui.QApplication.translate("ContourDialog", "Contour", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ContourDialog", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ContourDialog", "Vector layer", None, QtGui.QApplication.UnicodeUTF8))
        self.uLayerName.setToolTip(QtGui.QApplication.translate("ContourDialog", "WHere to take the input datas. Select a point shapefile in the list...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ContourDialog", "Data field   ", None, QtGui.QApplication.UnicodeUTF8))
        self.uFieldName.setToolTip(QtGui.QApplication.translate("ContourDialog", "Which attribute stores the input datas?", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ContourDialog", "Contouring", None, QtGui.QApplication.UnicodeUTF8))
        self.uLinesContours.setText(QtGui.QApplication.translate("ContourDialog", "contour lines", None, QtGui.QApplication.UnicodeUTF8))
        self.uFilledContours.setText(QtGui.QApplication.translate("ContourDialog", "filled contours", None, QtGui.QApplication.UnicodeUTF8))
        self.uBoth.setText(QtGui.QApplication.translate("ContourDialog", "both", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ContourDialog", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.uLevelsNumber.setStatusTip(QtGui.QApplication.translate("ContourDialog", "Number of levels between min and max value (from data field)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ContourDialog", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ContourDialog", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ContourDialog", "Extend", None, QtGui.QApplication.UnicodeUTF8))
        self.uExtend.setItemText(0, QtGui.QApplication.translate("ContourDialog", "neither", None, QtGui.QApplication.UnicodeUTF8))
        self.uExtend.setItemText(1, QtGui.QApplication.translate("ContourDialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.uExtend.setItemText(2, QtGui.QApplication.translate("ContourDialog", "max", None, QtGui.QApplication.UnicodeUTF8))
        self.uExtend.setItemText(3, QtGui.QApplication.translate("ContourDialog", "both", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ContourDialog", "Method", None, QtGui.QApplication.UnicodeUTF8))
        self.uMethod.setItemText(0, QtGui.QApplication.translate("ContourDialog", "Equal", None, QtGui.QApplication.UnicodeUTF8))
        self.uMethod.setItemText(1, QtGui.QApplication.translate("ContourDialog", "Quantile", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ContourDialog", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ContourDialog", "Layer name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ContourDialog", "Label precision", None, QtGui.QApplication.UnicodeUTF8))
        self.uPrecision.setStatusTip(QtGui.QApplication.translate("ContourDialog", "Number of levels between min and max value (from data field)", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc