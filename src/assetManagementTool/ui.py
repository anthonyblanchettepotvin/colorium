import colorium.CUI as CUI
import maya.cmds as cmds
from colorium.assetData import AssetData
import colorium.assetTypeDefinition as assetTypeDefinition


class AssetManagementToolUI(CUI.CUI):
    def build_ui(self):
        self.build_asset_information_section()
        self.build_save_options_section()


    def build_asset_information_section(self):
        """
        Builds the asset information section.
        """

        def build_combo_input(name, parent, enabled, items, changed_command, toggle_command):
            """
            Helper function that builds a base combo input for the asset information section.
            """

            lay_input = cmds.rowLayout("lay_{}".format(name), p=parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
            cmds.checkBox("chk_{}".format(name), p=lay_input, l="", v=enabled, cc=lambda value: _toggle(value))
            cmds.text("lbl_{}".format(name), p=lay_input, l="Asset {}:".format(name), al="right")
            cmds.optionMenu("cmb_{}".format(name), p=lay_input, en=enabled, cc=lambda value: changed_command(value))

            for item in items:
                cmds.menuItem("itm_{}_{}".format(name, item), l=item)

            def _toggle(value):
                toggle_command(value)
                cmds.control("cmb_{}".format(name), e=True, en=value)


        def build_text_input(name, parent, enabled, changed_command, toggle_command):
            """
            Helper function that builds a base text input for the asset information section.
            """

            lay_input = cmds.rowLayout("lay_{}".format(name), p=parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
            cmds.checkBox("chk_{}".format(name), p=lay_input, l="", v=enabled, cc=lambda value: _toggle(value))
            cmds.text("lbl_{}".format(name), p=lay_input, l="Asset {}:".format(name), al="right")
            cmds.textField("txt_{}".format(name), p=lay_input, en=enabled, tcc=lambda value: changed_command(value))

            def _toggle(value):
                toggle_command(value)
                cmds.control("txt_{}".format(name), e=True, en=value)


        def build_int_input(name, parent, enabled, min, max, changed_command, toggle_command):
            """
            Helper function that builds a base int input for the asset information section.
            """

            lay_input = cmds.rowLayout("lay_{}".format(name), p=parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
            cmds.checkBox("chk_{}".format(name), p=lay_input, l="", v=enabled, cc=lambda value: _toggle(value))
            cmds.text("lbl_{}".format(name), p=lay_input, l="Asset {}:".format(name), al="right")
            cmds.intSliderGrp("int_{}".format(name), p=lay_input, f=True, min=min, max=max, en=enabled, cc=lambda value: changed_command(value))

            def _toggle(value):
                toggle_command(value)
                cmds.control("int_{}".format(name), e=True, en=value)


        frm_asset_information = cmds.frameLayout("frm_asset_information", l="Asset Information", p=self.main_layout, mh=5, mw=5)

        build_combo_input("type", frm_asset_information, True, assetTypeDefinition.names(), self.controller.set_asset_type, self.controller.set_asset_hasType)
        build_text_input("name", frm_asset_information, True, self.controller.set_asset_name, self.controller.set_asset_hasName)
        build_int_input("variant", frm_asset_information, self.controller.asset.hasVariant, 1, 99, self.controller.set_asset_variant, self.controller.set_asset_hasVariant)
        build_int_input("scene", frm_asset_information, self.controller.asset.hasScene, 0, 995, self.controller.set_asset_scene, self.controller.set_asset_hasScene)
        build_int_input("shot", frm_asset_information, self.controller.asset.hasShot, 0, 995, self.controller.set_asset_shot, self.controller.set_asset_hasShot)
        build_int_input("version", frm_asset_information, True, 1, 99, self.controller.set_asset_version, self.controller.set_asset_hasVersion)


    def build_save_options_section(self):
        """
        Builds the save options section.
        """

        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5)


class AssetManagementToolController(CUI.CController):
    @property
    def asset(self):
        return self._asset


    @asset.setter
    def asset(self, value):
        self._asset = value


    def __init__(self):
        super(AssetManagementToolController, self).__init__()
        
        self._asset = AssetData()


    def display_ui_callback(self):
        print "UI displayed !"


    def set_asset_type(self, value):
        self.asset.type = value
        print self.asset.type


    def set_asset_hasType(self, value):
        # self.asset.hasType = value
        # print self.asset.hasType
        pass


    def set_asset_name(self, value):
        self.asset.name = value
        print self.asset.name


    def set_asset_hasName(self, value):
        # self.asset.hasName = value
        # print self.asset.hasName
        pass


    def set_asset_variant(self, value):
        self.asset.variant = value
        print self.asset.variant


    def set_asset_hasVariant(self, value):
        self.asset.hasVariant = value
        print self.asset.hasVariant


    def set_asset_scene(self, value):
        self.asset.scene = value
        print self.asset.scene


    def set_asset_hasScene(self, value):
        self.asset.hasScene = value
        print self.asset.hasScene


    def set_asset_shot(self, value):
        self.asset.shot = value
        print self.asset.shot


    def set_asset_hasShot(self, value):
        self.asset.hasShot = value
        print self.asset.hasShot


    def set_asset_version(self, value):
        self.asset.version = value
        print self.asset.version


    def set_asset_hasVersion(self, value):
        # self.asset.hasVersion = value
        # print self.asset.hasVersion
        pass
