# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'legendary.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_legendary_settings(object):
    def setupUi(self, legendary_settings):
        legendary_settings.setObjectName("legendary_settings")
        legendary_settings.resize(532, 383)
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settings)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gb_clean = QtWidgets.QGroupBox(self.settings)
        self.gb_clean.setObjectName("gb_clean")
        self.layout_clean = QtWidgets.QVBoxLayout(self.gb_clean)
        self.layout_clean.setObjectName("layout_clean")
        self.clean_button_without_manifests = QtWidgets.QPushButton(self.gb_clean)
        self.clean_button_without_manifests.setObjectName("clean_button_without_manifests")
        self.layout_clean.addWidget(self.clean_button_without_manifests)
        self.clean_button = QtWidgets.QPushButton(self.gb_clean)
        self.clean_button.setObjectName("clean_button")
        self.layout_clean.addWidget(self.clean_button)
        self.gridLayout_2.addWidget(self.gb_clean, 0, 1, 1, 1)
        self.egl_sync = QtWidgets.QGroupBox(self.settings)
        self.egl_sync.setObjectName("egl_sync")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.egl_sync)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sync_button = QtWidgets.QPushButton(self.egl_sync)
        self.sync_button.setObjectName("sync_button")
        self.verticalLayout.addWidget(self.sync_button)
        self.gridLayout_2.addWidget(self.egl_sync, 1, 1, 1, 1)
        self.gb_downloads = QtWidgets.QGroupBox(self.settings)
        self.gb_downloads.setObjectName("gb_downloads")
        self.layout_downloads = QtWidgets.QGridLayout(self.gb_downloads)
        self.layout_downloads.setObjectName("layout_downloads")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_downloads.addItem(spacerItem, 0, 4, 1, 1)
        self.max_worker_select = QtWidgets.QSpinBox(self.gb_downloads)
        self.max_worker_select.setObjectName("max_worker_select")
        self.layout_downloads.addWidget(self.max_worker_select, 0, 1, 1, 1)
        self.lbl_max_workers = QtWidgets.QLabel(self.gb_downloads)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_max_workers.sizePolicy().hasHeightForWidth())
        self.lbl_max_workers.setSizePolicy(sizePolicy)
        self.lbl_max_workers.setObjectName("lbl_max_workers")
        self.layout_downloads.addWidget(self.lbl_max_workers, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_max_workers_info = QtWidgets.QLabel(self.gb_downloads)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_max_workers_info.setFont(font)
        self.lbl_max_workers_info.setObjectName("lbl_max_workers_info")
        self.layout_downloads.addWidget(self.lbl_max_workers_info, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.gb_downloads, 1, 0, 1, 1)
        self.gb_install_dir = QtWidgets.QGroupBox(self.settings)
        self.gb_install_dir.setObjectName("gb_install_dir")
        self.layout_install_dir = QtWidgets.QVBoxLayout(self.gb_install_dir)
        self.layout_install_dir.setObjectName("layout_install_dir")
        self.gridLayout_2.addWidget(self.gb_install_dir, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        legendary_settings.addWidget(self.settings)
        self.egl_sync_page = QtWidgets.QWidget()
        self.egl_sync_page.setObjectName("egl_sync_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.egl_sync_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.back_button = QtWidgets.QPushButton(self.egl_sync_page)
        self.back_button.setObjectName("back_button")
        self.verticalLayout_2.addWidget(self.back_button)
        self.title = QtWidgets.QLabel(self.egl_sync_page)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title)
        self.pathedit_placeholder = QtWidgets.QVBoxLayout()
        self.pathedit_placeholder.setObjectName("pathedit_placeholder")
        self.verticalLayout_2.addLayout(self.pathedit_placeholder)
        self.path_info = QtWidgets.QLabel(self.egl_sync_page)
        self.path_info.setObjectName("path_info")
        self.verticalLayout_2.addWidget(self.path_info)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.exportable_games = QtWidgets.QGroupBox(self.egl_sync_page)
        self.exportable_games.setObjectName("exportable_games")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.exportable_games)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addWidget(self.exportable_games, 0, 0, 1, 1)
        self.importable_games = QtWidgets.QGroupBox(self.egl_sync_page)
        self.importable_games.setObjectName("importable_games")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.importable_games)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addWidget(self.importable_games, 0, 1, 1, 1)
        self.export_all_button = QtWidgets.QPushButton(self.egl_sync_page)
        self.export_all_button.setObjectName("export_all_button")
        self.gridLayout.addWidget(self.export_all_button, 1, 0, 1, 1)
        self.import_all_button = QtWidgets.QPushButton(self.egl_sync_page)
        self.import_all_button.setObjectName("import_all_button")
        self.gridLayout.addWidget(self.import_all_button, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(self.egl_sync_page)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sync_once_button = QtWidgets.QPushButton(self.groupBox)
        self.sync_once_button.setObjectName("sync_once_button")
        self.horizontalLayout.addWidget(self.sync_once_button)
        self.enable_sync_button = QtWidgets.QPushButton(self.groupBox)
        self.enable_sync_button.setObjectName("enable_sync_button")
        self.horizontalLayout.addWidget(self.enable_sync_button)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        legendary_settings.addWidget(self.egl_sync_page)

        self.retranslateUi(legendary_settings)
        legendary_settings.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(legendary_settings)

    def retranslateUi(self, legendary_settings):
        _translate = QtCore.QCoreApplication.translate
        legendary_settings.setWindowTitle(_translate("legendary_settings", "StackedWidget"))
        self.gb_clean.setTitle(_translate("legendary_settings", "Cleanup"))
        self.clean_button_without_manifests.setText(_translate("legendary_settings", "Clean, but keep manifests"))
        self.clean_button.setText(_translate("legendary_settings", "Remove everything"))
        self.egl_sync.setTitle(_translate("legendary_settings", "EGL Sync"))
        self.sync_button.setText(_translate("legendary_settings", "Sync Settings"))
        self.gb_downloads.setTitle(_translate("legendary_settings", "Download Settings"))
        self.lbl_max_workers.setText(_translate("legendary_settings", "Max Workers"))
        self.lbl_max_workers_info.setText(_translate("legendary_settings", "Less is slower (0: Default)"))
        self.gb_install_dir.setTitle(_translate("legendary_settings", "Default Installation Directory"))
        self.back_button.setText(_translate("legendary_settings", "Back"))
        self.title.setText(_translate("legendary_settings", "<h2>Sync Games with Epic Games Store</h2>"))
        self.path_info.setText(_translate("legendary_settings", "TextLabel"))
        self.exportable_games.setTitle(_translate("legendary_settings", "Exportable Games"))
        self.importable_games.setTitle(_translate("legendary_settings", "Importable"))
        self.export_all_button.setText(_translate("legendary_settings", "Export all Games"))
        self.import_all_button.setText(_translate("legendary_settings", "Import all Games"))
        self.groupBox.setTitle(_translate("legendary_settings", "Enable Sync"))
        self.sync_once_button.setText(_translate("legendary_settings", "Sync once"))
        self.enable_sync_button.setText(_translate("legendary_settings", "Enable automatic sync"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    legendary_settings = QtWidgets.QStackedWidget()
    ui = Ui_legendary_settings()
    ui.setupUi(legendary_settings)
    legendary_settings.show()
    sys.exit(app.exec_())
