# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\ui_files\widgets\object_settings_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ObjectSettingsWidget(object):
    def setupUi(self, ObjectSettingsWidget):
        ObjectSettingsWidget.setObjectName("ObjectSettingsWidget")
        ObjectSettingsWidget.resize(536, 1073)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ObjectSettingsWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.core_settings_vbox = QtWidgets.QVBoxLayout()
        self.core_settings_vbox.setObjectName("core_settings_vbox")
        self.label = QtWidgets.QLabel(ObjectSettingsWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.core_settings_vbox.addWidget(self.label)
        self.lock_settings_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.lock_settings_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lock_settings_checkbox.setObjectName("lock_settings_checkbox")
        self.core_settings_vbox.addWidget(self.lock_settings_checkbox)
        self.enable_download_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.enable_download_checkbox.setObjectName("enable_download_checkbox")
        self.core_settings_vbox.addWidget(self.enable_download_checkbox)
        self.verticalLayout.addLayout(self.core_settings_vbox)
        self.line = QtWidgets.QFrame(ObjectSettingsWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.post_download_form = QtWidgets.QFormLayout()
        self.post_download_form.setObjectName("post_download_form")
        self.line_2 = QtWidgets.QFrame(ObjectSettingsWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.post_download_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_2)
        self.label_19 = QtWidgets.QLabel(ObjectSettingsWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.post_download_form.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_19)
        self.label_7 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_7.setObjectName("label_7")
        self.post_download_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.post_limit_spinbox = QtWidgets.QSpinBox(ObjectSettingsWidget)
        self.post_limit_spinbox.setMaximum(1000)
        self.post_limit_spinbox.setObjectName("post_limit_spinbox")
        self.horizontalLayout_3.addWidget(self.post_limit_spinbox)
        self.post_limit_max_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.post_limit_max_button.setObjectName("post_limit_max_button")
        self.horizontalLayout_3.addWidget(self.post_limit_max_button)
        self.post_download_form.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_9 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_9.setObjectName("label_9")
        self.post_download_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.score_limit_spinbox = QtWidgets.QSpinBox(ObjectSettingsWidget)
        self.score_limit_spinbox.setMaximum(10000000)
        self.score_limit_spinbox.setObjectName("score_limit_spinbox")
        self.post_download_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.score_limit_spinbox)
        self.label_11 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_11.setObjectName("label_11")
        self.post_download_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.score_limit_operator_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.score_limit_operator_combo.setObjectName("score_limit_operator_combo")
        self.post_download_form.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.score_limit_operator_combo)
        self.date_limit_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.date_limit_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.date_limit_checkbox.setObjectName("date_limit_checkbox")
        self.post_download_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.date_limit_checkbox)
        self.date_limit_edit = QtWidgets.QDateTimeEdit(ObjectSettingsWidget)
        self.date_limit_edit.setDateTime(QtCore.QDateTime(QtCore.QDate(2005, 6, 23), QtCore.QTime(14, 43, 53)))
        self.date_limit_edit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2005, 6, 23), QtCore.QTime(14, 43, 53)))
        self.date_limit_edit.setObjectName("date_limit_edit")
        self.post_download_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.date_limit_edit)
        self.label_12 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_12.setObjectName("label_12")
        self.post_download_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.avoid_duplicates_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.avoid_duplicates_checkbox.setText("")
        self.avoid_duplicates_checkbox.setObjectName("avoid_duplicates_checkbox")
        self.post_download_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.avoid_duplicates_checkbox)
        self.label_30 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_30.setObjectName("label_30")
        self.post_download_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.extract_self_post_content_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.extract_self_post_content_checkbox.setText("")
        self.extract_self_post_content_checkbox.setObjectName("extract_self_post_content_checkbox")
        self.post_download_form.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.extract_self_post_content_checkbox)
        self.label_15 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_15.setObjectName("label_15")
        self.post_download_form.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.download_self_post_text_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.download_self_post_text_checkbox.setText("")
        self.download_self_post_text_checkbox.setObjectName("download_self_post_text_checkbox")
        self.post_download_form.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.download_self_post_text_checkbox)
        self.label_31 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_31.setObjectName("label_31")
        self.post_download_form.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.self_post_file_format_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.self_post_file_format_combo.setObjectName("self_post_file_format_combo")
        self.post_download_form.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.self_post_file_format_combo)
        self.label_13 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_13.setObjectName("label_13")
        self.post_download_form.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.download_videos_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.download_videos_checkbox.setText("")
        self.download_videos_checkbox.setObjectName("download_videos_checkbox")
        self.post_download_form.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.download_videos_checkbox)
        self.label_14 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_14.setObjectName("label_14")
        self.post_download_form.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.download_images_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.download_images_checkbox.setText("")
        self.download_images_checkbox.setObjectName("download_images_checkbox")
        self.post_download_form.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.download_images_checkbox)
        self.label_29 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_29.setObjectName("label_29")
        self.post_download_form.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.download_gifs_checkbox = QtWidgets.QCheckBox(ObjectSettingsWidget)
        self.download_gifs_checkbox.setText("")
        self.download_gifs_checkbox.setObjectName("download_gifs_checkbox")
        self.post_download_form.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.download_gifs_checkbox)
        self.label_28 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_28.setObjectName("label_28")
        self.post_download_form.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.nsfw_filter_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.nsfw_filter_combo.setObjectName("nsfw_filter_combo")
        self.post_download_form.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.nsfw_filter_combo)
        self.label_16 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_16.setObjectName("label_16")
        self.post_download_form.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.post_sort_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.post_sort_combo.setObjectName("post_sort_combo")
        self.post_download_form.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.post_sort_combo)
        self.post_download_naming_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.post_download_naming_label.setObjectName("post_download_naming_label")
        self.post_download_form.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.post_download_naming_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.post_download_naming_line_edit = QtWidgets.QLineEdit(ObjectSettingsWidget)
        self.post_download_naming_line_edit.setObjectName("post_download_naming_line_edit")
        self.horizontalLayout_2.addWidget(self.post_download_naming_line_edit)
        self.post_download_naming_available_tokens_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.post_download_naming_available_tokens_button.setObjectName("post_download_naming_available_tokens_button")
        self.horizontalLayout_2.addWidget(self.post_download_naming_available_tokens_button)
        self.post_download_form.setLayout(18, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.post_save_structure_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.post_save_structure_label.setObjectName("post_save_structure_label")
        self.post_download_form.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.post_save_structure_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.post_save_path_structure_line_edit = QtWidgets.QLineEdit(ObjectSettingsWidget)
        self.post_save_path_structure_line_edit.setObjectName("post_save_path_structure_line_edit")
        self.horizontalLayout_5.addWidget(self.post_save_path_structure_line_edit)
        self.post_save_structure_available_tokens_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.post_save_structure_available_tokens_button.setObjectName("post_save_structure_available_tokens_button")
        self.horizontalLayout_5.addWidget(self.post_save_structure_available_tokens_button)
        self.post_download_form.setLayout(19, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.post_path_example_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.post_path_example_label.setObjectName("post_path_example_label")
        self.post_download_form.setWidget(20, QtWidgets.QFormLayout.SpanningRole, self.post_path_example_label)
        self.verticalLayout.addLayout(self.post_download_form)
        self.line_3 = QtWidgets.QFrame(ObjectSettingsWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.comment_download_form = QtWidgets.QFormLayout()
        self.comment_download_form.setObjectName("comment_download_form")
        self.label_20 = QtWidgets.QLabel(ObjectSettingsWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.comment_download_form.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_20)
        self.label_22 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_22.setObjectName("label_22")
        self.comment_download_form.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.comment_download_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.comment_download_combo.setObjectName("comment_download_combo")
        self.comment_download_form.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comment_download_combo)
        self.label_21 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_21.setObjectName("label_21")
        self.comment_download_form.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.comment_content_download_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.comment_content_download_combo.setObjectName("comment_content_download_combo")
        self.comment_download_form.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comment_content_download_combo)
        self.label_23 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_23.setObjectName("label_23")
        self.comment_download_form.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_24.setObjectName("label_24")
        self.comment_download_form.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.comment_score_limit_spinbox = QtWidgets.QSpinBox(ObjectSettingsWidget)
        self.comment_score_limit_spinbox.setMaximum(10000000)
        self.comment_score_limit_spinbox.setObjectName("comment_score_limit_spinbox")
        self.comment_download_form.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comment_score_limit_spinbox)
        self.label_25 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_25.setObjectName("label_25")
        self.comment_download_form.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.comment_score_operator_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.comment_score_operator_combo.setObjectName("comment_score_operator_combo")
        self.comment_download_form.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comment_score_operator_combo)
        self.label_18 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_18.setObjectName("label_18")
        self.comment_download_form.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.comment_sort_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.comment_sort_combo.setObjectName("comment_sort_combo")
        self.comment_download_form.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comment_sort_combo)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comment_limit_spinbox = QtWidgets.QSpinBox(ObjectSettingsWidget)
        self.comment_limit_spinbox.setMaximum(10000)
        self.comment_limit_spinbox.setObjectName("comment_limit_spinbox")
        self.horizontalLayout_4.addWidget(self.comment_limit_spinbox)
        self.comment_limit_max_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.comment_limit_max_button.setObjectName("comment_limit_max_button")
        self.horizontalLayout_4.addWidget(self.comment_limit_max_button)
        self.comment_download_form.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_32 = QtWidgets.QLabel(ObjectSettingsWidget)
        self.label_32.setObjectName("label_32")
        self.comment_download_form.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.comment_extract_combo = QtWidgets.QComboBox(ObjectSettingsWidget)
        self.comment_extract_combo.setObjectName("comment_extract_combo")
        self.comment_download_form.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comment_extract_combo)
        self.comment_download_naming_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.comment_download_naming_label.setObjectName("comment_download_naming_label")
        self.comment_download_form.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.comment_download_naming_label)
        self.comment_save_structure_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.comment_save_structure_label.setObjectName("comment_save_structure_label")
        self.comment_download_form.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.comment_save_structure_label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.comment_download_naming_line_edit = QtWidgets.QLineEdit(ObjectSettingsWidget)
        self.comment_download_naming_line_edit.setObjectName("comment_download_naming_line_edit")
        self.horizontalLayout_6.addWidget(self.comment_download_naming_line_edit)
        self.comment_download_naming_available_tokens_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.comment_download_naming_available_tokens_button.setObjectName("comment_download_naming_available_tokens_button")
        self.horizontalLayout_6.addWidget(self.comment_download_naming_available_tokens_button)
        self.comment_download_form.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comment_save_path_structure_line_edit = QtWidgets.QLineEdit(ObjectSettingsWidget)
        self.comment_save_path_structure_line_edit.setObjectName("comment_save_path_structure_line_edit")
        self.horizontalLayout_7.addWidget(self.comment_save_path_structure_line_edit)
        self.comment_save_structure_available_tokens_button = QtWidgets.QToolButton(ObjectSettingsWidget)
        self.comment_save_structure_available_tokens_button.setObjectName("comment_save_structure_available_tokens_button")
        self.horizontalLayout_7.addWidget(self.comment_save_structure_available_tokens_button)
        self.comment_download_form.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.comment_path_example_label = QtWidgets.QLabel(ObjectSettingsWidget)
        self.comment_path_example_label.setObjectName("comment_path_example_label")
        self.comment_download_form.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.comment_path_example_label)
        self.verticalLayout.addLayout(self.comment_download_form)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ObjectSettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(ObjectSettingsWidget)

    def retranslateUi(self, ObjectSettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        ObjectSettingsWidget.setWindowTitle(_translate("ObjectSettingsWidget", "Settings"))
        self.label.setText(_translate("ObjectSettingsWidget", "Core Settings:"))
        self.lock_settings_checkbox.setToolTip(_translate("ObjectSettingsWidget", "When checked, the settings in this window will not be overwritten due to changes in the main settings window"))
        self.lock_settings_checkbox.setText(_translate("ObjectSettingsWidget", "Lock Settings"))
        self.enable_download_checkbox.setText(_translate("ObjectSettingsWidget", "Download Enabled"))
        self.label_19.setText(_translate("ObjectSettingsWidget", "Post Download Settings:"))
        self.label_7.setText(_translate("ObjectSettingsWidget", "Post Limit:"))
        self.post_limit_max_button.setText(_translate("ObjectSettingsWidget", "Max"))
        self.label_9.setText(_translate("ObjectSettingsWidget", "Score Limit:"))
        self.label_11.setText(_translate("ObjectSettingsWidget", "Score Limit Eval:"))
        self.date_limit_checkbox.setText(_translate("ObjectSettingsWidget", "Date Limit:    "))
        self.label_12.setText(_translate("ObjectSettingsWidget", "Avoid Duplicates:"))
        self.label_30.setText(_translate("ObjectSettingsWidget", "Extract Self Post Content:"))
        self.label_15.setText(_translate("ObjectSettingsWidget", "Download Self Post Text:"))
        self.label_31.setText(_translate("ObjectSettingsWidget", "Self Post File Format:"))
        self.label_13.setText(_translate("ObjectSettingsWidget", "Download Videos:"))
        self.label_14.setText(_translate("ObjectSettingsWidget", "Download Images:"))
        self.label_29.setText(_translate("ObjectSettingsWidget", "Download Gifs:"))
        self.label_28.setText(_translate("ObjectSettingsWidget", "NSFW Filter:"))
        self.label_16.setText(_translate("ObjectSettingsWidget", "Sort Posts By:"))
        self.post_download_naming_label.setText(_translate("ObjectSettingsWidget", "Download Naming:"))
        self.post_download_naming_line_edit.setPlaceholderText(_translate("ObjectSettingsWidget", "----"))
        self.post_download_naming_available_tokens_button.setToolTip(_translate("ObjectSettingsWidget", "See available tokens"))
        self.post_download_naming_available_tokens_button.setText(_translate("ObjectSettingsWidget", "..."))
        self.post_save_structure_label.setText(_translate("ObjectSettingsWidget", "Save Path Structure:"))
        self.post_save_path_structure_line_edit.setPlaceholderText(_translate("ObjectSettingsWidget", "----"))
        self.post_save_structure_available_tokens_button.setToolTip(_translate("ObjectSettingsWidget", "See available tokens"))
        self.post_save_structure_available_tokens_button.setText(_translate("ObjectSettingsWidget", "..."))
        self.post_path_example_label.setText(_translate("ObjectSettingsWidget", "Post path example"))
        self.label_20.setText(_translate("ObjectSettingsWidget", "Comment Download Settings:"))
        self.label_22.setText(_translate("ObjectSettingsWidget", "Download:"))
        self.label_21.setText(_translate("ObjectSettingsWidget", "Download Links"))
        self.label_23.setText(_translate("ObjectSettingsWidget", "Comment Limit:"))
        self.label_24.setText(_translate("ObjectSettingsWidget", "Score Limit:"))
        self.label_25.setText(_translate("ObjectSettingsWidget", "Score Limit Eval:"))
        self.label_18.setText(_translate("ObjectSettingsWidget", "Sort Comments By:"))
        self.comment_limit_spinbox.setToolTip(_translate("ObjectSettingsWidget", "Only limits top level comment.  May pull more comments depending on replies"))
        self.comment_limit_max_button.setText(_translate("ObjectSettingsWidget", "Max"))
        self.label_32.setText(_translate("ObjectSettingsWidget", "Extract:"))
        self.comment_download_naming_label.setText(_translate("ObjectSettingsWidget", "Download Naming:"))
        self.comment_save_structure_label.setText(_translate("ObjectSettingsWidget", "Save Path Structure:"))
        self.comment_download_naming_line_edit.setPlaceholderText(_translate("ObjectSettingsWidget", "----"))
        self.comment_download_naming_available_tokens_button.setToolTip(_translate("ObjectSettingsWidget", "See available tokens"))
        self.comment_download_naming_available_tokens_button.setText(_translate("ObjectSettingsWidget", "..."))
        self.comment_save_path_structure_line_edit.setPlaceholderText(_translate("ObjectSettingsWidget", "----"))
        self.comment_save_structure_available_tokens_button.setToolTip(_translate("ObjectSettingsWidget", "See available tokens"))
        self.comment_save_structure_available_tokens_button.setText(_translate("ObjectSettingsWidget", "..."))
        self.comment_path_example_label.setText(_translate("ObjectSettingsWidget", "Comment path example"))
