"""Module used to build consistent UI for Colorium's tools using maya.cmds."""

import maya.cmds as cmds
import colorium.data_binding as data_binding


class CUI(object):
    """Base class for a Colorium UI."""

    @property
    def name(self):
        """The name of the UI."""

        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def controller(self):
        """The controller associated with the UI."""

        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value


    @property
    def main_window(self):
        """The name of the UI's main window."""

        return self._main_window

    @main_window.setter
    def main_window(self, value):
        self._main_window = value


    @property
    def main_frame(self):
        """The name of the UI's main frame."""

        return self._main_frame

    @main_frame.setter
    def main_frame(self, value):
        self._main_frame = value


    @property
    def main_layout(self):
        """The name of the UI's main layout."""

        return self._main_layout

    @main_layout.setter
    def main_layout(self, value):
        self._main_layout = value


    def __init__(self, name, controller):
        self._controls = []

        self._name = name
        self._controller = None
        self._main_window = ''
        self._main_frame = ''
        self._main_layout = ''

        if not self._controller or self._controller != controller:
            self._controller = controller
            self._controller.ui = self

        self.display_ui(self._controller.display_ui_callback)


    def display_ui(self, callback):
        """
        Displays the tool's UI.
        """

        self.build_main_window()
        self.build_main_layout()
        self.build_ui()

        for control in self._controls:
            control.build_ui()

        callback()


    def build_ui(self):
        """
        Builds the tool's UI.
        """

        pass


    def add_control(self, control):
        """Adds a control to the UI's controls."""

        if control not in self._controls:
            self._controls.append(control)


    def remove_control(self, control):
        """Removes a control from the UI's controls."""

        if control in self._controls:
            self._controls.remove(control)


    def get_control_by_name(self, name):
        """Returns a control from the UI's controls by it's name."""

        for control in self._controls:
            if control.name == name:
                return control


    def build_main_window(self):
        """Builds the main window."""

        self._main_window = self.build_window("win_main", self._name)


    def build_window(self, name="untitled", title="untitled"):
        """Helper function that builds a window using maya.cmds."""

        window_exists = cmds.window(name, q=True, ex=True)

        if window_exists:
            cmds.deleteUI(name, window=True)

        window = cmds.window(name, t=title, rtf=True, tlb=True)

        cmds.showWindow(window)

        return window


    def build_main_layout(self):
        """Builds the main layout."""

        self._main_frame = cmds.frameLayout("frm_main", p=self._main_window, lv=False, mh=5, mw=5)
        self._main_layout = cmds.columnLayout("lay_main", p=self._main_frame, adj=True)


class CController(object):
    """Base class for a Colorium UI Controller."""

    @property
    def ui(self):
        """The UI associated with the controller."""
        return self._ui

    @ui.setter
    def ui(self, value):
        self._ui = value


    def __init__(self):
        self._ui = None


    def display_ui_callback(self):
        """Called at the end of the method Display of the associated UI instance. Used for post-display operations."""

        pass


class CToggleable():
    """\"Interface\" used to define toggleable controls."""

    def toggle(self, value):
        """Method used to enable/disable the control."""

        pass


class CUIElement(object):
    """Base class for a Colorium UI Element."""

    @property
    def name(self):
        """The name of the CUIElement."""

        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def title(self):
        """The title of the CUIElement."""

        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    @property
    def parent(self):
        """The name of the CUIElement's parent."""

        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value


    def __init__(self, name, title, parent):
        self._name = name
        self._title = title
        self._parent = parent


class CLayout(CUIElement):
    """Base class for a Colorium UI Layout."""

    def __init__(self, name, title, parent, childrens=None):
        super(CLayout, self).__init__(name, title, parent)

        self._childrens = childrens if childrens else []


    def add_children(self, children):
        """Add a given children to the CLayout's childrens."""

        if children not in self._childrens:
            self._childrens.append(children)


    def remove_children(self, children):
        """Remove a given children from the CLayout's childrens."""

        if children in self._childrens:
            self._childrens.remove(children)


class CControl(CUIElement, data_binding.CBindable):
    """Base class for a Colorium UI Control."""

    def __init__(self, name, title, parent):
        super(CControl, self).__init__(name, title, parent)
        data_binding.CBindable.__init__(self)


    def build_ui(self):
        """Method used to build the control's UI."""

        pass


class CInlineLayout(CLayout):
    """Class representing an Inline Layout. It's childrens are placed side by side, aligned on the left or on the right."""

    def __init__(self, name, title, parent, childrens=None, align="left"):
        super(CInlineLayout, self).__init__(name, title, parent)

        self._childrens = childrens if childrens else []
        self._align = align


    def build_ui(self):
        """Method used to build the control's UI."""

        align_offset = 0
        align_adjustement_column = len(self._childrens) + 1
        if self._align == "right":
            align_offset = 1
            align_adjustement_column = 1

        column_attachments = []
        for children in range(1 + align_offset, len(self._childrens) + 1 + align_offset):
            if children == 1 + align_offset:
                column_attachments.append((children, "right", 2.5))
            elif children == len(self._childrens) + align_offset:
                column_attachments.append((children, "left", 2.5))
            else:
                column_attachments.append((children, "both", 2.5))

        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=len(self._childrens) + 1, cat=column_attachments, adj=align_adjustement_column)

        if self._align == "right":
            cmds.separator("sep_{}".format(self._name), vis=False)

        if self._childrens:
            for children in self._childrens:
                children.parent = layout
                children.build_ui()

        if self._align == "left":
            cmds.separator("sep_{}".format(self._name), vis=False)


class CTextInput(CControl, CToggleable):
    """Class that represents a Text Input. Used to write text."""

    @property
    def text(self):
        """The text written in the Text Input."""

        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

        cmds.textField("txt_{}".format(self._name), e=True, tx=value)

        self.notify_property_changed("text", value)
        print('\'text\' property of CTextInput set to \'{}\'').format(value)


    @property
    def enabled(self):
        """The state of the Text Input."""

        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

        cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
        cmds.control("txt_{}".format(self._name), e=True, en=value)

        self.notify_property_changed("enabled", value)
        print('\'enabled\' property of CTextInput set to \'{}\'').format(value)


    def __init__(self, name, title, parent, enabled=True, changed_command=None, toggle_command=None, toggleable=False, default_value=""):
        super(CTextInput, self).__init__(name, title, parent)

        self.__text = default_value
        self.__enabled = enabled
        self.__toggleable = toggleable
        self.__changed_command = changed_command if changed_command else lambda value: NotImplemented
        self.__toggle_command = toggle_command if toggle_command else lambda value: NotImplemented


    def build_ui(self):
        """Method used to build the control's UI."""

        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)

        if self.__toggleable:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self.__enabled, cc=self.toggle)
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l=self._title, al="right")
        cmds.textField("txt_{}".format(self._name), p=layout, tx=self.__text, en=self.__enabled, cc=self.text_changed)


    def text_changed(self, value):
        """Method called when the Text Input's text changed."""

        self.__changed_command(value)

        self.text = value


    def toggle(self, value):
        """Method called when the Text Input's state changed."""

        self.__toggle_command(value)

        self.enabled = value

        cmds.control("txt_{}".format(self._name), e=True, en=value)


class CIntInput(CControl, CToggleable):
    """Class that represents a Int Input. Used to write numbers."""

    @property
    def value(self):
        """The number written in the Int Input."""

        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

        cmds.intSliderGrp("int_{}".format(self._name), e=True, v=value)

        self.notify_property_changed("value", value)
        print('\'value\' property of CIntInput set to \'{}\'').format(value)


    @property
    def enabled(self):
        """The state of the Int Input."""

        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

        cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
        cmds.control("int_{}".format(self._name), e=True, en=value)

        self.notify_property_changed("enabled", value)
        print('\'enabled\' property of CIntInput set to \'{}\'').format(value)


    def __init__(self, name, title, parent, enabled=True, min_value=1, max_value=10, changed_command=None, toggle_command=None, toggleable=False, default_value=1):
        super(CIntInput, self).__init__(name, title, parent)

        self.__value = default_value
        self.__enabled = enabled
        self.__toggleable = toggleable
        self.__min = min_value
        self.__max = max_value
        self.__changed_command = changed_command if changed_command else lambda value: NotImplemented
        self.__toggle_command = toggle_command if toggle_command else lambda value: NotImplemented


    def build_ui(self):
        """Method used to build the control's UI."""

        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)

        if self.__toggleable:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self.__enabled, cc=self.toggle)
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l=self._title, al="right")
        cmds.intSliderGrp("int_{}".format(self._name), p=layout, v=self.__value, f=True, min=self.__min, max=self.__max, en=self.__enabled, cc=self.value_changed)


    def value_changed(self, value):
        """Method called when the Int Input's value changed."""

        self.__changed_command(value)

        self.value = value


    def toggle(self, value):
        """Method called when the Int Input's state changed."""

        self.__toggle_command(value)

        self.enabled = value

        cmds.control("int_{}".format(self._name), e=True, en=value)


class CComboInput(CControl, CToggleable):
    """Class that represents a Combo Input. Used to choose a value from a list of values."""

    @property
    def value(self):
        """The chosen value of the Combo Input."""

        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

        cmds.optionMenu("cmb_{}".format(self._name), e=True, v=value)

        self.notify_property_changed("value", value)
        print('\'value\' property of CComboInput set to \'{}\'').format(value)


    @property
    def enabled(self):
        """The state of the Combo Input."""

        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

        cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
        cmds.control("cmb_{}".format(self._name), e=True, en=value)

        self.notify_property_changed("enabled", value)
        print('\'enabled\' property of CComboInput set to \'{}\'').format(value)


    def __init__(self, name, title, parent, enabled=True, items=None, changed_command=None, toggle_command=None, toggleable=False, default_value=""):
        super(CComboInput, self).__init__(name, title, parent)

        self.__value = default_value
        self.__enabled = enabled
        self.__toggleable = toggleable
        self.__items = items if items else []
        self.__changed_command = changed_command if changed_command else lambda value: NotImplemented
        self.__toggle_command = toggle_command if toggle_command else lambda value: NotImplemented


    def build_ui(self):
        """Method used to build the control's UI."""

        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)

        if self.__toggleable:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self.__enabled, cc=self.toggle)
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l=self._title, al="right")
        cmds.optionMenu("cmb_{}".format(self._name), p=layout, en=self.__enabled, cc=self.value_changed)

        for item in self.__items:
            cmds.menuItem("itm_{}_{}".format(self._name, item), l=item)

        if self.__value in self.__items:
            cmds.optionMenu("cmb_{}".format(self._name), e=True, v=self.__value)


    def value_changed(self, value):
        """Method called when the Combo Input's value changed."""

        self.__changed_command(value)

        self.value = value


    def toggle(self, value):
        """Method called when the Combo Input's state changed."""

        self.__toggle_command(value)

        self.enabled = value

        cmds.control("cmb_{}".format(self._name), e=True, en=value)


class CFilePathInput(CControl, CToggleable):
    """Class that represents a File Path Input. Used to write a file path and open it in the explorer."""

    @property
    def text(self):
        """The file path written in the File Path Input."""

        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

        cmds.textField("txt_{}".format(self._name), e=True, tx=value)

        self.notify_property_changed("text", value)
        print('\'text\' property of CFilePathInput set to \'{}\'').format(value)


    @property
    def enabled(self):
        """The state of the File Path Input."""

        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

        cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
        cmds.control("txt_{}".format(self._name), e=True, en=value)

        self.notify_property_changed("enabled", value)
        print('\'enabled\' property of CFilePathInput set to \'{}\'').format(value)


    def __init__(self, name, title, parent, enabled=True, changed_command=None, open_command=None, toggle_command=None, toggleable=False, default_value=""):
        super(CFilePathInput, self).__init__(name, title, parent)

        self.__text = default_value
        self.__enabled = enabled
        self.__toggleable = toggleable
        self.__changed_command = changed_command if changed_command else lambda value: NotImplemented
        self.__open_command = open_command if open_command else lambda value: NotImplemented
        self.__toggle_command = toggle_command if toggle_command else lambda value: NotImplemented


    def build_ui(self):
        """Method used to build the control's UI."""

        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=4, cat=[(2, "right", 5), (4, "left", 5)], cw=[(1, 25), (2, 100), (4, 100)], adj=3)

        if self.__toggleable:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self.__enabled, cc=self.toggle)
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l=self._title, al="right")
        cmds.textField("txt_{}".format(self._name), p=layout, tx=self.__text, en=self.__enabled, tcc=self.text_changed)
        cmds.button("btn_open_{}".format(self._name), p=layout, l="Open", w=60, c=self.__open_command)


    def text_changed(self, value):
        """Method called when the File Path Input's value changed."""

        self.__changed_command(value)

        self.text = value


    def toggle(self, value):
        """Method called when the File Path Input's state changed."""

        self.__toggle_command(value)

        self.enabled = value

        cmds.control("txt_{}".format(self._name), e=True, en=value)


class CButtonControl(CControl):
    """Class that represents a Button Control. Used to execute a command."""

    def __init__(self, name, title, parent, command=None):
        super(CButtonControl, self).__init__(name, title, parent)

        self._command = command if command else lambda value: NotImplemented


    def build_ui(self):
        """Method used to build the control's UI."""

        cmds.button("btn_{}".format(self._name), l=self._title, p=self._parent, w=60, c=self._command)
