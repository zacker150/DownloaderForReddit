# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\settings\core_settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoreSettingsWidget(object):
    def setupUi(self, CoreSettingsWidget):
        CoreSettingsWidget.setObjectName("CoreSettingsWidget")
        CoreSettingsWidget.resize(906, 849)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(CoreSettingsWidget)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_group_box = QtWidgets.QGroupBox(CoreSettingsWidget)
        self.file_group_box.setFlat(False)
        self.file_group_box.setCheckable(False)
        self.file_group_box.setObjectName("file_group_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.file_group_box)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.file_group_box)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.file_group_box)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.user_save_dir_line_edit = QtWidgets.QLineEdit(self.file_group_box)
        self.user_save_dir_line_edit.setObjectName("user_save_dir_line_edit")
        self.horizontalLayout_8.addWidget(self.user_save_dir_line_edit)
        self.select_user_base_directory_button = QtWidgets.QToolButton(self.file_group_box)
        self.select_user_base_directory_button.setObjectName("select_user_base_directory_button")
        self.horizontalLayout_8.addWidget(self.select_user_base_directory_button)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.subreddit_save_dir_line_edit = QtWidgets.QLineEdit(self.file_group_box)
        self.subreddit_save_dir_line_edit.setObjectName("subreddit_save_dir_line_edit")
        self.horizontalLayout_9.addWidget(self.subreddit_save_dir_line_edit)
        self.select_subreddit_base_directory_button = QtWidgets.QToolButton(self.file_group_box)
        self.select_subreddit_base_directory_button.setObjectName("select_subreddit_base_directory_button")
        self.horizontalLayout_9.addWidget(self.select_subreddit_base_directory_button)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.file_group_box)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.match_date_modified_checkbox = QtWidgets.QCheckBox(self.file_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.match_date_modified_checkbox.sizePolicy().hasHeightForWidth())
        self.match_date_modified_checkbox.setSizePolicy(sizePolicy)
        self.match_date_modified_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.match_date_modified_checkbox.setText("")
        self.match_date_modified_checkbox.setObjectName("match_date_modified_checkbox")
        self.horizontalLayout.addWidget(self.match_date_modified_checkbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.file_group_box)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.rename_invalid_download_folders_checkbox = QtWidgets.QCheckBox(self.file_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_invalid_download_folders_checkbox.sizePolicy().hasHeightForWidth())
        self.rename_invalid_download_folders_checkbox.setSizePolicy(sizePolicy)
        self.rename_invalid_download_folders_checkbox.setText("")
        self.rename_invalid_download_folders_checkbox.setObjectName("rename_invalid_download_folders_checkbox")
        self.horizontalLayout_2.addWidget(self.rename_invalid_download_folders_checkbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.invalid_rename_label = QtWidgets.QLabel(self.file_group_box)
        self.invalid_rename_label.setObjectName("invalid_rename_label")
        self.horizontalLayout_3.addWidget(self.invalid_rename_label)
        self.invalid_rename_format_line_edit = QtWidgets.QLineEdit(self.file_group_box)
        self.invalid_rename_format_line_edit.setObjectName("invalid_rename_format_line_edit")
        self.horizontalLayout_3.addWidget(self.invalid_rename_format_line_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(66)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.example_label = QtWidgets.QLabel(self.file_group_box)
        self.example_label.setObjectName("example_label")
        self.horizontalLayout_4.addWidget(self.example_label)
        self.invalid_format_example_label = QtWidgets.QLabel(self.file_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invalid_format_example_label.sizePolicy().hasHeightForWidth())
        self.invalid_format_example_label.setSizePolicy(sizePolicy)
        self.invalid_format_example_label.setIndent(0)
        self.invalid_format_example_label.setObjectName("invalid_format_example_label")
        self.horizontalLayout_4.addWidget(self.invalid_format_example_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.file_group_box)
        self.download_group_box = QtWidgets.QGroupBox(CoreSettingsWidget)
        self.download_group_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.download_group_box.setFlat(False)
        self.download_group_box.setObjectName("download_group_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.download_group_box)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.download_group_box)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.extraction_thread_count_spinbox = QtWidgets.QSpinBox(self.download_group_box)
        self.extraction_thread_count_spinbox.setMaximumSize(QtCore.QSize(116, 16777215))
        self.extraction_thread_count_spinbox.setObjectName("extraction_thread_count_spinbox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.extraction_thread_count_spinbox)
        self.label_7 = QtWidgets.QLabel(self.download_group_box)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.download_thread_count_spinbox = QtWidgets.QSpinBox(self.download_group_box)
        self.download_thread_count_spinbox.setMaximumSize(QtCore.QSize(116, 16777215))
        self.download_thread_count_spinbox.setObjectName("download_thread_count_spinbox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.download_thread_count_spinbox)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.multi_part_download_groupbox = QtWidgets.QGroupBox(self.download_group_box)
        self.multi_part_download_groupbox.setCheckable(True)
        self.multi_part_download_groupbox.setObjectName("multi_part_download_groupbox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.multi_part_download_groupbox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.multi_part_download_groupbox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.multipart_threshold_spinbox = QtWidgets.QDoubleSpinBox(self.multi_part_download_groupbox)
        self.multipart_threshold_spinbox.setMinimumSize(QtCore.QSize(100, 0))
        self.multipart_threshold_spinbox.setMaximum(10000000000.99)
        self.multipart_threshold_spinbox.setObjectName("multipart_threshold_spinbox")
        self.horizontalLayout_7.addWidget(self.multipart_threshold_spinbox)
        self.threshold_size_combo = QtWidgets.QComboBox(self.multi_part_download_groupbox)
        self.threshold_size_combo.setObjectName("threshold_size_combo")
        self.horizontalLayout_7.addWidget(self.threshold_size_combo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.multi_part_download_groupbox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.multi_part_chunk_size_spinbox = QtWidgets.QDoubleSpinBox(self.multi_part_download_groupbox)
        self.multi_part_chunk_size_spinbox.setMinimumSize(QtCore.QSize(100, 0))
        self.multi_part_chunk_size_spinbox.setMaximum(10000000000.99)
        self.multi_part_chunk_size_spinbox.setObjectName("multi_part_chunk_size_spinbox")
        self.horizontalLayout_11.addWidget(self.multi_part_chunk_size_spinbox)
        self.chunk_size_combo = QtWidgets.QComboBox(self.multi_part_download_groupbox)
        self.chunk_size_combo.setObjectName("chunk_size_combo")
        self.horizontalLayout_11.addWidget(self.chunk_size_combo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.multi_part_download_groupbox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.multi_part_thread_count_spinbox = QtWidgets.QSpinBox(self.multi_part_download_groupbox)
        self.multi_part_thread_count_spinbox.setMinimumSize(QtCore.QSize(100, 0))
        self.multi_part_thread_count_spinbox.setObjectName("multi_part_thread_count_spinbox")
        self.horizontalLayout_10.addWidget(self.multi_part_thread_count_spinbox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addWidget(self.multi_part_download_groupbox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.download_group_box)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.download_on_add_checkbox = QtWidgets.QCheckBox(self.download_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_on_add_checkbox.sizePolicy().hasHeightForWidth())
        self.download_on_add_checkbox.setSizePolicy(sizePolicy)
        self.download_on_add_checkbox.setText("")
        self.download_on_add_checkbox.setObjectName("download_on_add_checkbox")
        self.horizontalLayout_5.addWidget(self.download_on_add_checkbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.download_group_box)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.finish_incomplete_extractions_checkbox = QtWidgets.QCheckBox(self.download_group_box)
        self.finish_incomplete_extractions_checkbox.setText("")
        self.finish_incomplete_extractions_checkbox.setObjectName("finish_incomplete_extractions_checkbox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.finish_incomplete_extractions_checkbox)
        self.label_11 = QtWidgets.QLabel(self.download_group_box)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.finish_incomplete_downloads_checkbox = QtWidgets.QCheckBox(self.download_group_box)
        self.finish_incomplete_downloads_checkbox.setText("")
        self.finish_incomplete_downloads_checkbox.setObjectName("finish_incomplete_downloads_checkbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.finish_incomplete_downloads_checkbox)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.download_group_box)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.download_reddit_hosted_videos_checkbox = QtWidgets.QCheckBox(self.download_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_reddit_hosted_videos_checkbox.sizePolicy().hasHeightForWidth())
        self.download_reddit_hosted_videos_checkbox.setSizePolicy(sizePolicy)
        self.download_reddit_hosted_videos_checkbox.setText("")
        self.download_reddit_hosted_videos_checkbox.setObjectName("download_reddit_hosted_videos_checkbox")
        self.horizontalLayout_6.addWidget(self.download_reddit_hosted_videos_checkbox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.extractor_list_group_box = QtWidgets.QGroupBox(self.download_group_box)
        self.extractor_list_group_box.setObjectName("extractor_list_group_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.extractor_list_group_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.extractor_list_widget = QtWidgets.QListWidget(self.extractor_list_group_box)
        self.extractor_list_widget.setObjectName("extractor_list_widget")
        self.verticalLayout_5.addWidget(self.extractor_list_widget)
        self.verticalLayout_3.addWidget(self.extractor_list_group_box)
        self.verticalLayout_4.addWidget(self.download_group_box)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.label_3.setBuddy(self.match_date_modified_checkbox)
        self.label_4.setBuddy(self.rename_invalid_download_folders_checkbox)
        self.label_9.setBuddy(self.download_on_add_checkbox)
        self.label_10.setBuddy(self.finish_incomplete_extractions_checkbox)
        self.label_11.setBuddy(self.finish_incomplete_downloads_checkbox)

        self.retranslateUi(CoreSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(CoreSettingsWidget)

    def retranslateUi(self, CoreSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        CoreSettingsWidget.setWindowTitle(_translate("CoreSettingsWidget", "Core Settings"))
        self.file_group_box.setTitle(_translate("CoreSettingsWidget", "Files"))
        self.label.setToolTip(_translate("CoreSettingsWidget", "The base directory that user content will be saved to"))
        self.label.setText(_translate("CoreSettingsWidget", "User Base Save Directory:"))
        self.label_2.setToolTip(_translate("CoreSettingsWidget", "The base directory that subreddit content will be saved to"))
        self.label_2.setText(_translate("CoreSettingsWidget", "Subreddit Base Save Directory:"))
        self.select_user_base_directory_button.setText(_translate("CoreSettingsWidget", "Select Folder"))
        self.select_subreddit_base_directory_button.setText(_translate("CoreSettingsWidget", "Select Folder"))
        self.label_3.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>If selected, the date modified property of the downloaded file will be matched with the post date of the post that it was extracted from</p></body></html>"))
        self.label_3.setText(_translate("CoreSettingsWidget", "&Match file date modified to post date:"))
        self.label_4.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>If selected, when a user deletes their account or becmes inactive the name of their folder will be changed according to the rename format settings</p></body></html>"))
        self.label_4.setText(_translate("CoreSettingsWidget", "Rename folders of invalid or deleted users/subreddits:"))
        self.invalid_rename_label.setText(_translate("CoreSettingsWidget", "Rename format:"))
        self.example_label.setText(_translate("CoreSettingsWidget", "Example:"))
        self.invalid_format_example_label.setText(_translate("CoreSettingsWidget", "example_path"))
        self.download_group_box.setTitle(_translate("CoreSettingsWidget", "Download"))
        self.label_6.setText(_translate("CoreSettingsWidget", "Extraction thread count:"))
        self.label_7.setText(_translate("CoreSettingsWidget", "Download thread count:"))
        self.multi_part_download_groupbox.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>When enabled, large files (over the set threshold size) will be downloaded in multiple part simultaneously.  This will increase download speeds for downloads containing many large files.</p></body></html>"))
        self.multi_part_download_groupbox.setTitle(_translate("CoreSettingsWidget", "Multi-Part Download"))
        self.label_8.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>The size threshold at which a file is downloaded in parts in multiple threads.  Carefully adjust this number as there is a definite point of diminishing returns depending on your internet connection.</p></body></html>"))
        self.label_8.setText(_translate("CoreSettingsWidget", "Multi-part download threshold:"))
        self.label_13.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>The size threshold at which a file is downloaded in parts in multiple threads.  Carefully adjust this number as there is a definite point of diminishing returns depending on your internet connection.</p></body></html>"))
        self.label_13.setText(_translate("CoreSettingsWidget", "Multi-part download chunk size:"))
        self.label_12.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>The number of threads that will be used for multi-part downloads.  This count should balance with the extraction and download thread counts you have set.</p></body></html>"))
        self.label_12.setText(_translate("CoreSettingsWidget", "Multi-part thread count:"))
        self.label_9.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>When selected, users or subreddits will be downloaded immediately upon being added</p></body></html>"))
        self.label_9.setWhatsThis(_translate("CoreSettingsWidget", "When checked, users or subreddits will be downloaded immediately upon being added"))
        self.label_9.setText(_translate("CoreSettingsWidget", "Download on add:"))
        self.download_on_add_checkbox.setToolTip(_translate("CoreSettingsWidget", "When checked, users or subreddits will be downloaded immediately upon being added"))
        self.download_on_add_checkbox.setWhatsThis(_translate("CoreSettingsWidget", "When checked, users or subreddits will be downloaded immediately upon being added"))
        self.label_10.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>If selected, downloads which are not complete will be downloaded at the start of each download session</p></body></html>"))
        self.label_10.setText(_translate("CoreSettingsWidget", "Finish incomplete downloads at start of session:"))
        self.label_11.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>If selected, posts that have not been extracted will be extracted then downloaded at the start of each download session</p></body></html>"))
        self.label_11.setText(_translate("CoreSettingsWidget", "Finish incomplete extractions at start of session:"))
        self.label_5.setToolTip(_translate("CoreSettingsWidget", "<html><head/><body><p>Videos hosted on reddit are downloaded in two parts and must be joined after the download session is complete.</p><p>Because of this extra step, downloading these videos is optional</p></body></html>"))
        self.label_5.setText(_translate("CoreSettingsWidget", "Download reddit hosted videos:"))
        self.extractor_list_group_box.setTitle(_translate("CoreSettingsWidget", "Extractor List"))
