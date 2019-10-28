import maya.cmds as cmds
from functools import partial
from patterns.observerPattern import Subject, Observer
from colorium.assetData import AssetData
from colorium.configuration import Configuration, SaveConfiguration, PublishConfiguration, ExportConfiguration, OpenConfiguration, CreateConfiguration
import colorium.save as save
import colorium.publish as publish
import colorium.export as export
import colorium.open as open
import colorium.create as create
import colorium.assetTypeDefinition as assetTypeDefinition


class ColoriumAssetManagementToolUI:
    WINDOW_NAME = "coloriumAssetManagementTool"
    WINDOW_TITLE = "Colorium Asset Management Tool"

    _controller = None

    def __init__(self):
        self._controller = ColoriumAssetManagementToolController(self)

        self.createUI(self._controller.attachToData)

    def createUI(self, callback = None):
        window = self.createWindow()
        main = self.createMainLayout()

        self.createAssetDataView(main)
        self.createSaveOptionsView(main)
        self.createPublishOptionsView(main)
        self.createExportOptionsView(main)
        self.createAssetFileNameView(main)
        self.createAssetPathView(main)
        self.createButtonSection(main)

        cmds.showWindow(window)

        if callback != None:
            callback()

    def createWindow(self):
        if cmds.window(self.WINDOW_NAME, q=True, ex=True):
            cmds.deleteUI(self.WINDOW_NAME, window=True)

        return cmds.window(self.WINDOW_NAME, t=self.WINDOW_TITLE)

    MAIN_LAYOUT_NAME = "mainLayout"
    def createMainLayout(self):
        return cmds.columnLayout(self.MAIN_LAYOUT_NAME, adj=True)


    # Create Asset Data View
    def createAssetDataView(self, parent):
        layout = self.createAssetDataViewLayout(parent)

        self.createAssetDataViewFields(layout)

    ASSET_DATA_VIEW_LAYOUT_NAME = "assetDataViewLayout"
    ASSET_DATA_VIEW_LAYOUT_COLUMN_COUNT = 4
    ASSET_DATA_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 20), (2, 60), (3, 200)]
    def createAssetDataViewLayout(self, parent):
        return cmds.rowColumnLayout(self.ASSET_DATA_VIEW_LAYOUT_NAME, p=parent, nc=self.ASSET_DATA_VIEW_LAYOUT_COLUMN_COUNT, cw=self.ASSET_DATA_VIEW_LAYOUT_COLUMN_WIDTHS, adj=4)

    def createAssetDataViewFields(self, parent):
        self.createAssetTypeField(parent)
        self.createAssetNameField(parent)
        self.createAssetVariantField(parent)
        self.createAssetSceneField(parent)
        self.createAssetShotField(parent)
        self.createAssetVersionField(parent)

    ASSET_TYPE_LABEL_NAME = "assetTypeLabel"
    ASSET_TYPE_LABEL_TEXT = "Type"
    ASSET_TYPE_MENU_NAME = "assetTypeMenu"
    ASSET_TYPE_MENU_ITEMS = assetTypeDefinition.names
    def createAssetTypeField(self, parent):
        self.createOptionMenuField(self.ASSET_TYPE_LABEL_NAME, self.ASSET_TYPE_LABEL_TEXT, self.ASSET_TYPE_MENU_NAME, self._controller.assetData.type, self.ASSET_TYPE_MENU_ITEMS, partial(self._controller.inputChangedCommand, "type"))

    ASSET_NAME_LABEL_NAME = "assetNameLabel"
    ASSET_NAME_LABEL_TEXT = "Name"
    ASSET_NAME_FIELD_NAME = "assetNameField"
    def createAssetNameField(self, parent):
        self.createTextField(self.ASSET_NAME_LABEL_NAME, self.ASSET_NAME_LABEL_TEXT, self.ASSET_NAME_FIELD_NAME, self._controller.assetData.name, partial(self._controller.inputChangedCommand, "name"))

    ASSET_VARIANT_LABEL_NAME = "assetVariantLabel"
    ASSET_VARIANT_LABEL_TEXT = "Variant"
    ASSET_VARIANT_FIELD_NAME = "assetVariantField"
    def createAssetVariantField(self, parent):
        self.createIntField(self.ASSET_VARIANT_LABEL_NAME, self.ASSET_VARIANT_LABEL_TEXT, self.ASSET_VARIANT_FIELD_NAME, self._controller.assetData.variant, True, self._controller.assetData.hasVariant, 1, 99, partial(self._controller.inputChangedCommand, "variant"), partial(self._controller.inputChangedCommand, "hasVariant"))

    ASSET_SCENE_LABEL_NAME = "assetSceneLabel"
    ASSET_SCENE_LABEL_TEXT = "Scene"
    ASSET_SCENE_FIELD_NAME = "assetSceneField"
    def createAssetSceneField(self, parent):
        self.createIntField(self.ASSET_SCENE_LABEL_NAME, self.ASSET_SCENE_LABEL_TEXT, self.ASSET_SCENE_FIELD_NAME, self._controller.assetData.scene, True, self._controller.assetData.hasScene, 1, 999, partial(self._controller.inputChangedCommand, "scene"), partial(self._controller.inputChangedCommand, "hasScene"))

    ASSET_SHOT_LABEL_NAME = "assetShotLabel"
    ASSET_SHOT_LABEL_TEXT = "Shot"
    ASSET_SHOT_FIELD_NAME = "assetShotField"
    def createAssetShotField(self, parent):
        self.createIntField(self.ASSET_SHOT_LABEL_NAME, self.ASSET_SHOT_LABEL_TEXT, self.ASSET_SHOT_FIELD_NAME, self._controller.assetData.shot, True, self._controller.assetData.hasShot, 1, 999, partial(self._controller.inputChangedCommand, "shot"), partial(self._controller.inputChangedCommand, "hasShot"))

    ASSET_VERSION_LABEL_NAME = "assetVersionLabel"
    ASSET_VERSION_LABEL_TEXT = "Version"
    ASSET_VERSION_FIELD_NAME = "assetVersionField"
    def createAssetVersionField(self, parent):
        self.createIntField(self.ASSET_VERSION_LABEL_NAME, self.ASSET_VERSION_LABEL_TEXT, self.ASSET_VERSION_FIELD_NAME, self._controller.assetData.version, min=1, max=99, valueChangedCommand=partial(self._controller.inputChangedCommand, "version"))


    # Create Save Options View
    def createSaveOptionsView(self, parent):
        layout = self.createSaveOptionsViewLayout(parent)

        self.createSaveOptionsViewFields(layout)

    SAVE_OPTIONS_VIEW_FRAME_NAME = "saveOptionsViewFrame"
    SAVE_OPTIONS_NAME_VIEW_FRAME_TEXT = "Save Options"
    SAVE_OPTIONS_NAME_VIEW_LAYOUT_NAME = "saveOptionsViewLayout"
    SAVE_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT = 4
    SAVE_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 20), (2, 60), (3, 200)]
    def createSaveOptionsViewLayout(self, parent):
        frame = cmds.frameLayout(self.SAVE_OPTIONS_VIEW_FRAME_NAME, p=parent, l=self.SAVE_OPTIONS_NAME_VIEW_FRAME_TEXT)
        return cmds.rowColumnLayout(self.SAVE_OPTIONS_NAME_VIEW_LAYOUT_NAME, p=frame, nc=self.SAVE_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT, cw=self.SAVE_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS, adj=4)

    def createSaveOptionsViewFields(self, parent):
        self.createSaveTypeField(parent)

    SAVE_TYPE_LABEL_NAME = "saveTypeLabel"
    SAVE_TYPE_LABEL_TEXT = "Type"
    SAVE_TYPE_MENU_NAME = "saveTypeMenu"
    SAVE_TYPE_MENU_ITEMS = save.getNames()
    def createSaveTypeField(self, parent):
        self.createOptionMenuField(self.SAVE_TYPE_LABEL_NAME, self.SAVE_TYPE_LABEL_TEXT, self.SAVE_TYPE_MENU_NAME, self._controller.assetData.type, self.SAVE_TYPE_MENU_ITEMS, self._controller.saveTypeChangedCommand)


    # Create Publish Options View
    def createPublishOptionsView(self, parent):
        layout = self.createPublishOptionsViewLayout(parent)

        self.createPublishOptionsViewFields(layout)

    PUBLISH_OPTIONS_VIEW_FRAME_NAME = "publishOptionsViewFrame"
    PUBLISH_OPTIONS_NAME_VIEW_FRAME_TEXT = "Publish Options"
    PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_NAME = "publishOptionsViewLayout"
    PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT = 4
    PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 20), (2, 60), (3, 200)]
    def createPublishOptionsViewLayout(self, parent):
        frame = cmds.frameLayout(self.PUBLISH_OPTIONS_VIEW_FRAME_NAME, p=parent, l=self.PUBLISH_OPTIONS_NAME_VIEW_FRAME_TEXT)
        return cmds.rowColumnLayout(self.PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_NAME, p=frame, nc=self.PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT, cw=self.PUBLISH_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS, adj=4)

    def createPublishOptionsViewFields(self, parent):
        self.createPublishTypeField(parent)

    PUBLISH_TYPE_LABEL_NAME = "publishTypeLabel"
    PUBLISH_TYPE_LABEL_TEXT = "Type"
    PUBLISH_TYPE_MENU_NAME = "publishTypeMenu"
    PUBLISH_TYPE_MENU_ITEMS = publish.getNames()
    def createPublishTypeField(self, parent):
        self.createOptionMenuField(self.PUBLISH_TYPE_LABEL_NAME, self.PUBLISH_TYPE_LABEL_TEXT, self.PUBLISH_TYPE_MENU_NAME, self._controller.assetData.type, self.PUBLISH_TYPE_MENU_ITEMS, self._controller.publishTypeChangedCommand)


    # Create Export Options View
    def createExportOptionsView(self, parent):
        layout = self.createExportOptionsViewLayout(parent)

        self.createExportOptionsViewFields(layout)

    EXPORT_OPTIONS_VIEW_FRAME_NAME = "exportOptionsViewFrame"
    EXPORT_OPTIONS_NAME_VIEW_FRAME_TEXT = "Export Options"
    EXPORT_OPTIONS_NAME_VIEW_LAYOUT_NAME = "exportOptionsViewLayout"
    EXPORT_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT = 4
    EXPORT_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 20), (2, 60), (3, 200)]
    def createExportOptionsViewLayout(self, parent):
        frame = cmds.frameLayout(self.EXPORT_OPTIONS_VIEW_FRAME_NAME, p=parent, l=self.EXPORT_OPTIONS_NAME_VIEW_FRAME_TEXT)
        return cmds.rowColumnLayout(self.EXPORT_OPTIONS_NAME_VIEW_LAYOUT_NAME, p=frame, nc=self.EXPORT_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_COUNT, cw=self.EXPORT_OPTIONS_NAME_VIEW_LAYOUT_COLUMN_WIDTHS, adj=4)

    def createExportOptionsViewFields(self, parent):
        self.createExportTypeField(parent)

    EXPORT_TYPE_LABEL_NAME = "exportTypeLabel"
    EXPORT_TYPE_LABEL_TEXT = "Type"
    EXPORT_TYPE_MENU_NAME = "exportTypeMenu"
    EXPORT_TYPE_MENU_ITEMS = export.getNames()
    def createExportTypeField(self, parent):
        self.createOptionMenuField(self.EXPORT_TYPE_LABEL_NAME, self.EXPORT_TYPE_LABEL_TEXT, self.EXPORT_TYPE_MENU_NAME, self._controller.assetData.type, self.EXPORT_TYPE_MENU_ITEMS, self._controller.exportTypeChangedCommand)


    # Create Asset File Name View
    def createAssetFileNameView(self, parent):
        layout = self.createAssetFileNameViewLayout(parent)

        self.createAssetFileNameViewFields(layout)

    ASSET_FILE_NAME_VIEW_FRAME_NAME = "assetFileNameViewFrame"
    ASSET_FILE_NAME_VIEW_FRAME_TEXT = "File Name Preview"
    ASSET_FILE_NAME_VIEW_LAYOUT_NAME = "assetFileNameViewLayout"
    ASSET_FILE_NAME_VIEW_LAYOUT_COLUMN_COUNT = 3
    ASSET_FILE_NAME_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 120), (3, 60)]
    def createAssetFileNameViewLayout(self, parent):
        frame = cmds.frameLayout(self.ASSET_FILE_NAME_VIEW_FRAME_NAME, p=parent, l=self.ASSET_FILE_NAME_VIEW_FRAME_TEXT)
        return cmds.rowColumnLayout(self.ASSET_FILE_NAME_VIEW_LAYOUT_NAME, p=frame, nc=self.ASSET_FILE_NAME_VIEW_LAYOUT_COLUMN_COUNT, cw=self.ASSET_FILE_NAME_VIEW_LAYOUT_COLUMN_WIDTHS, adj=2)

    def createAssetFileNameViewFields(self, parent):
        self.createSaveFileNameField(parent)
        self.createPublishFileNameField(parent)
        self.createExportFileNameField(parent)

    SAVE_FILE_NAME_LABEL_NAME = "saveFileNameLabel"
    SAVE_FILE_NAME_LABEL_TEXT = "Save File Name"
    SAVE_FILE_NAME_FIELD_NAME = "saveFileNameField"
    def createSaveFileNameField(self, parent):
        self.createFileNamePreviewField(self.SAVE_FILE_NAME_LABEL_NAME, self.SAVE_FILE_NAME_LABEL_TEXT, self.SAVE_FILE_NAME_FIELD_NAME, self._controller._saveConfig.fileName, self._controller._saveConfig, "fileName")

    PUBLISH_FILE_NAME_LABEL_NAME = "publishFileNameLabel"
    PUBLISH_FILE_NAME_LABEL_TEXT = "Publish File Name"
    PUBLISH_FILE_NAME_FIELD_NAME = "publishFileNameField"
    def createPublishFileNameField(self, parent):
        self.createFileNamePreviewField(self.PUBLISH_FILE_NAME_LABEL_NAME, self.PUBLISH_FILE_NAME_LABEL_TEXT, self.PUBLISH_FILE_NAME_FIELD_NAME, self._controller._publishConfig.fileName, self._controller._publishConfig, "fileName")

    EXPORT_FILE_NAME_LABEL_NAME = "exportFileNameLabel"
    EXPORT_FILE_NAME_LABEL_TEXT = "Export File Name"
    EXPORT_FILE_NAME_FIELD_NAME = "exportFileNameField"
    def createExportFileNameField(self, parent):
        self.createFileNamePreviewField(self.EXPORT_FILE_NAME_LABEL_NAME, self.EXPORT_FILE_NAME_LABEL_TEXT, self.EXPORT_FILE_NAME_FIELD_NAME, self._controller._exportConfig.fileName, self._controller._exportConfig, "fileName")


    # Create Asset Path View
    def createAssetPathView(self, parent):
        layout = self.createAssetPathViewLayout(parent)

        self.createAssetPathViewFields(layout)

    ASSET_PATH_VIEW_FRAME_NAME = "assetPathViewFrame"
    ASSET_PATH_VIEW_FRAME_TEXT = "Path Preview"
    ASSET_PATH_VIEW_LAYOUT_NAME = "assetPathViewLayout"
    ASSET_PATH_VIEW_LAYOUT_COLUMN_COUNT = 4
    ASSET_PATH_VIEW_LAYOUT_COLUMN_WIDTHS = [(1, 120), (3, 60), (4, 60)]
    def createAssetPathViewLayout(self, parent):
        frame = cmds.frameLayout(self.ASSET_PATH_VIEW_FRAME_NAME, p=parent, l=self.ASSET_PATH_VIEW_FRAME_TEXT)
        return cmds.rowColumnLayout(self.ASSET_PATH_VIEW_LAYOUT_NAME, p=frame, nc=self.ASSET_PATH_VIEW_LAYOUT_COLUMN_COUNT, cw=self.ASSET_PATH_VIEW_LAYOUT_COLUMN_WIDTHS, adj=2)

    def createAssetPathViewFields(self, parent):
        self.createSavePathField(parent)
        self.createPublishPathField(parent)
        self.createExportPathField(parent)

    SAVE_PATH_LABEL_NAME = "savePathLabel"
    SAVE_PATH_LABEL_TEXT = "Save Path"
    SAVE_PATH_FIELD_NAME = "savePathField"
    def createSavePathField(self, parent):
        self.createPathPreviewField(self.SAVE_PATH_LABEL_NAME, self.SAVE_PATH_LABEL_TEXT, self.SAVE_PATH_FIELD_NAME, self._controller._saveConfig.path, self._controller._saveConfig, "path")

    PUBLISH_PATH_LABEL_NAME = "publishPathLabel"
    PUBLISH_PATH_LABEL_TEXT = "Publish Path"
    PUBLISH_PATH_FIELD_NAME = "publishPathField"
    def createPublishPathField(self, parent):
        self.createPathPreviewField(self.PUBLISH_PATH_LABEL_NAME, self.PUBLISH_PATH_LABEL_TEXT, self.PUBLISH_PATH_FIELD_NAME, self._controller._publishConfig.path, self._controller._publishConfig, "path")

    EXPORT_PATH_LABEL_NAME = "exportPathLabel"
    EXPORT_PATH_LABEL_TEXT = "Export Path"
    EXPORT_PATH_FIELD_NAME = "exportPathField"
    def createExportPathField(self, parent):
        self.createPathPreviewField(self.EXPORT_PATH_LABEL_NAME, self.EXPORT_PATH_LABEL_TEXT, self.EXPORT_PATH_FIELD_NAME, self._controller._exportConfig.path, self._controller._exportConfig, "path")


    # Create Button Section
    def createButtonSection(self, parent):
        layout = self.createButtonSectionLayout(parent)

        self.createButtonSectionFields(layout)

    BUTTON_SECTION_FRAME_NAME = "buttonSectionFrame"
    BUTTON_SECTION_FRAME_TEXT = "Button Section"
    BUTTON_SECTION_LAYOUT_NAME = "buttonSectionLayout"
    BUTTON_SECTION_LAYOUT_COLUMN_COUNT = 5
    def createButtonSectionLayout(self, parent):
        frame = cmds.frameLayout(self.BUTTON_SECTION_FRAME_NAME, p=parent, l=self.BUTTON_SECTION_FRAME_TEXT)
        return cmds.rowLayout(self.BUTTON_SECTION_LAYOUT_NAME, p=frame, nc=self.BUTTON_SECTION_LAYOUT_COLUMN_COUNT, adj=True)

    def createButtonSectionFields(self, parent):
        cmds.separator(vis=False)

        self.createCancelButton(parent)
        self.createOpenButton(parent)
        self.createCreateButton(parent)
        self.createCommitButton(parent)

    def createCancelButton(self, parent):
        cmds.button("cancelButton", l="Cancel", w=75, c=self._controller.cancelCommand)

    def createOpenButton(self, parent):
        cmds.button("openButton", l="Open", w=75, c=self._controller.openCommand)

    def createCreateButton(self, parent):
        cmds.button("createButton", l="Create", w=75, c=self._controller.createCommand)

    def createCommitButton(self, parent):
        cmds.button("commitButton", l="Commit", w=75, c=self._controller.commitCommand)

    def createFileNamePreviewField(self, labelName="", labelText="", fieldName="", fieldValue="", config=None, configProperty=""):
        cmds.text(labelName, l=labelText, al="left")
        cmds.textField(fieldName, tx=fieldValue, en=False, tcc=partial(self._controller.previewTextChanged, fieldName, config, configProperty))
        cmds.button(fieldName + "EditButton", l="Edit", c=partial(self._controller.toggleFieldEdit, fieldName, config, configProperty))

    def createPathPreviewField(self, labelName="", labelText="", fieldName="", fieldValue="", config=None, configProperty=""):
        self.createFileNamePreviewField(labelName, labelText, fieldName, fieldValue, config, configProperty)
        cmds.button(fieldName + "OpenButton", l="Open", c=partial(self._controller.openPathInExplorer, config))

    def createOptionMenuField(self, labelName="", labelText="", fieldName="", fieldValue="", items=[], changedCommand=""):
        cmds.separator(vis=False)
        cmds.text(labelName, l=labelText, al="left")
        cmds.optionMenu(fieldName)

        if changedCommand != "":
            cmds.optionMenu(fieldName, e=True, cc=changedCommand)

        for item in items:
            cmds.menuItem(l=item)

        cmds.separator(vis=False)

    def createTextField(self, labelName="", labelText="", fieldName="", fieldValue="", textChangedCommand=""):
        cmds.separator(vis=False)
        cmds.text(labelName, l=labelText, al="left")
        cmds.textField(fieldName, tx=fieldValue)

        if textChangedCommand != "":
            cmds.textField(fieldName, e=True, tcc=textChangedCommand)

        cmds.separator(vis=False)

    def createIntField(self, labelName="", labelText="", fieldName="", fieldValue=0, toggleField=False, toggleValue=False, min=0, max=0, valueChangedCommand="", toggleChangedCommand=""):
        if toggleField:
            cmds.checkBox(fieldName + "Toggle", l="", v=toggleValue)

            if toggleChangedCommand != "":
                cmds.checkBox(fieldName + "Toggle", e=True, cc=toggleChangedCommand)
        else:
            cmds.separator(vis=False)

        cmds.text(labelName, l=labelText, al="left")
        cmds.intSliderGrp(fieldName, field=True, cw=[(1, 35)], min=min, max=max, v=fieldValue)

        if valueChangedCommand != "":
            cmds.intSliderGrp(fieldName, e=True, cc=valueChangedCommand)

        cmds.separator(vis=False)


class ColoriumAssetManagementToolController(Subject, Observer):
    _observers = []

    _ui = None
    _assetData = None
    _saveConfig = None
    _publishConfig = None
    _exportConfig = None
    _openConfig = None
    _createConfig = None

    @property
    def assetData(self):
        return self._assetData

    def __init__(self, UI):
        self._ui = UI
        self._assetData = AssetData()
        self._saveConfig = SaveConfiguration(self._assetData)
        self._publishConfig = PublishConfiguration(self._assetData)
        self._exportConfig = ExportConfiguration(self._assetData)
        self._openConfig = OpenConfiguration(self._assetData)
        self._createConfig = CreateConfiguration(self._assetData)

    def attachToData(self):
        self.attach(self._assetData)
        self._saveConfig.attachAndNotify(self)
        self._publishConfig.attachAndNotify(self)
        self._exportConfig.attachAndNotify(self)
        self._openConfig.attachAndNotify(self)
        self._createConfig.attachAndNotify(self)

    def attach(self, observer):
        self._observers.append(observer)

    def attachAndNotify(self, observer):
        self.attach(observer)
        self.notify()

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        prop = args[0]
        value = args[1]

        if prop == "type":
            for assetType in assetTypeDefinition.assetTypes:
                if assetType.name == value:
                    value = assetType

        for observer in self._observers:
            observer.update(prop, value)

    def clearObservers(self):
        self._observers = []

    def update(self, *args):
        target = args[0]

        if target == "saveConfig":
            cmds.textField(self._ui.SAVE_FILE_NAME_FIELD_NAME, e=True, tx=self._saveConfig.fileName)
            cmds.textField(self._ui.SAVE_PATH_FIELD_NAME, e=True, tx=self._saveConfig.path)
        elif target == "publishConfig":
            cmds.textField(self._ui.PUBLISH_FILE_NAME_FIELD_NAME, e=True, tx=self._publishConfig.fileName)
            cmds.textField(self._ui.PUBLISH_PATH_FIELD_NAME, e=True, tx=self._publishConfig.path)
        elif target == "exportConfig":
            cmds.textField(self._ui.EXPORT_FILE_NAME_FIELD_NAME, e=True, tx=self._exportConfig.fileName)
            cmds.textField(self._ui.EXPORT_PATH_FIELD_NAME, e=True, tx=self._exportConfig.path)
        elif target == "openConfig":
            pass

    def previewTextChanged(self, field, config, property, *args):
        text = cmds.textField(field, q=True, tx=True)

        if property == "fileName":
            config.fileName = text
        elif property == "path":
            config.path = text

    def toggleFieldEdit(self, field, config, property, *args):
        enabled = cmds.control(field, q=True, en=True)

        if enabled:
            enabled = False
        else:
            enabled = True

        cmds.control(field, e=True, en=enabled)

        if property == "fileName":
            config.fileNameOverridden = enabled
        elif property == "path":
            config.pathOverridden = enabled

        config.update()

    def openPathInExplorer(self, config, *args):
        config.command = open.getCommandByName("Explorer")

        config.executeCommand()

    def inputChangedCommand(self, prop, *args):
        self.notify(prop, args[0])

    def saveTypeChangedCommand(self, *args):
        type = args[0]

        self._saveConfig.command = save.getCommandByName(type)

    def publishTypeChangedCommand(self, *args):
        type = args[0]

        self._publishConfig.command = publish.getCommandByName(type)

    def exportTypeChangedCommand(self, *args):
        type = args[0]

        self._exportConfig.command = export.getCommandByName(type)

    def cancelCommand(self, *args):
        cmds.deleteUI(self._ui.WINDOW_NAME)
        
    def createCommand(self, *args):
        self._createConfig.command = create.getCommandByName("MA")

        createConfirmed = cmds.confirmDialog(
            title="Create asset in " + self._createConfig.command.name,
            message="The asset is going to be created in " + self._createConfig.command.name + " to " + self._createConfig.path + " with the name " + self._createConfig.fileName + ". Do you confirm the operation ?",
            button=["Yes", "No"],
            defaultButton="Yes",
            cancelButton="No",
            dismissString="No"
        )

        if createConfirmed == "Yes":
            self._createConfig.executeCommand()

    def openCommand(self, config, *args):
        self._openConfig.command = open.getCommandByName("Generic")

        openConfirmed = cmds.confirmDialog(
            title="Open asset",
            message="The asset named " + self._openConfig.fileName + " in " + self._openConfig.path + " is going to be opened. Do you confirm the operation ?",
            button=["Yes", "No"],
            defaultButton="Yes",
            cancelButton="No",
            dismissString="No"
        )

        if openConfirmed == "Yes":
            self._openConfig.executeCommand()

    def commitCommand(self, *args):
        saveType = cmds.optionMenu(self._ui.SAVE_TYPE_MENU_NAME, q=True, v=True)
        saveEnable = False if saveType == "None" else True
        publishType = cmds.optionMenu(self._ui.PUBLISH_TYPE_MENU_NAME, q=True, v=True)
        publishEnable = False if publishType == "None" else True
        exportType = cmds.optionMenu(self._ui.EXPORT_TYPE_MENU_NAME, q=True, v=True)
        exportEnable = False if exportType == "None" else True

        if not saveEnable and not publishEnable and not exportEnable:
            cmds.confirmDialog(
                title="Cannot commit asset",
                message="The asset cannot be committed. Please, select a save, publish or export type and try again.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return

        if saveEnable:
            self.save()

        if publishEnable:
            self.publish()

        if exportEnable:
            self.export()

    def save(self):
        saveConfirmed = cmds.confirmDialog(
            title="Save asset in " + self._saveConfig.command.name,
            message="The asset is going to be saved in " + self._saveConfig.command.name + " to " + self._saveConfig.path + " with the name " + self._saveConfig.fileName + ". Do you confirm the operation ?",
            button=["Yes", "No"],
            defaultButton="Yes",
            cancelButton="No",
            dismissString="No"
        )

        if saveConfirmed == "Yes":
            self._saveConfig.executeCommand()

    def publish(self):
        publishConfirmed = cmds.confirmDialog(
            title="Publish asset in " + self._publishConfig.command.name,
            message="The asset is going to be published in " + self._publishConfig.command.name + " to " + self._publishConfig.path + " with the name " + self._publishConfig.fileName + ". Do you confirm the operation ?",
            button=["Yes", "No"],
            defaultButton="Yes",
            cancelButton="No",
            dismissString="No"
        )

        if publishConfirmed == "Yes":
            self._publishConfig.executeCommand()

    def export(self):
        exportConfirmed = cmds.confirmDialog(
            title="Export asset in " + self._exportConfig.command.name,
            message="The asset is going to be exported in " + self._exportConfig.command.name + " to " + self._exportConfig.path + " with the name " + self._exportConfig.fileName + ". Do you confirm the operation ?",
            button=["Yes", "No"],
            defaultButton="Yes",
            cancelButton="No",
            dismissString="No"
        )

        if exportConfirmed == "Yes":
            self._exportConfig.executeCommand()
