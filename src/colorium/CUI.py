from abc import ABCMeta, abstractproperty, abstractmethod
import maya.cmds as cmds

class CUI(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value

    @property
    def main_window(self):
        return self._main_window

    @main_window.setter
    def main_window(self, value):
        self._main_window = value

    @property
    def main_layout(self):
        return self._main_layout

    @main_layout.setter
    def main_layout(self, value):
        self._main_layout = value

    def __init__(self, name, controller):
        self._name = name
        self._controller = None
        self._main_window = ""
        self._main_layout = ""

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

        callback()

        
    def build_ui(self):
        """
        Builds the tool's UI.
        """

        NotImplemented


    def build_main_window(self):
        """
        Builds the main window.
        """

        self._main_window = self.build_window("win_main", self._name)


    def build_window(self, name="untitled", title="untitled"):
        """
        Helper function that builds a window using maya.cmds.
        """

        window_exists = cmds.window(name, q=True, ex=True)

        if window_exists:
            cmds.deleteUI(name, window=True)

        window = cmds.window(name, t=title, rtf=True)

        cmds.showWindow(window)

        return window


    def build_main_layout(self):
        """
        Builds the main layout.
        """

        self._main_layout = cmds.columnLayout("lay_main", adj=True)


class CController(object):
    @property
    def ui(self):
        return self._ui

    @ui.setter
    def ui(self, value):
        self._ui = value

    def __init__(self):
        self._ui = None

    def display_ui_callback(self):
        """
        Called at the end of the method Display of the associated UI instance. Used for post-display operations.
        """
        
        NotImplemented


class CToggleable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def toggle(self, value):
        """
        Enables/disables the control.
        """

        NotImplemented


class CUpdateable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_value(self, value):
        """
        Updates the control's value.
        """

        NotImplemented


class CControl(object):
    def __init__(self, name, parent):
        self._name = name
        self._parent = parent

    def build_ui(self):
        """
        Builds the control's UI.
        """

        NotImplemented


class CTextInput(CControl, CToggleable, CUpdateable):
    def __init__(self, name, parent, enabled=True, changed_command=None, toggle_command=None, build=False):
        super(CTextInput, self).__init__(name, parent)

        self._enabled = enabled
        self._changed_command = changed_command
        self._toggle_command = toggle_command

        if build:
            self.build_ui()


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.textField("txt_{}".format(self._name), p=layout, en=self._enabled, tcc=lambda value: self._changed_command(value))


    def toggle(self, value):
        self._toggle_command(value)
        cmds.control("txt_{}".format(self._name), e=True, en=value)

    
    def update_value(self, value):
        cmds.textField("txt_{}".format(self._name), e=True, tx=value)


class CIntInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, min=1, max=10, changed_command=None, toggle_command=None, build=False):
        super(CIntInput, self).__init__(name, parent)

        self._enabled = enabled
        self._min = min
        self._max = max
        self._changed_command = changed_command
        self._toggle_command = toggle_command

        if build:
            self.build_ui()


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.intSliderGrp("int_{}".format(self._name), p=layout, f=True, min=self._min, max=self._max, en=self._enabled, cc=lambda value: self._changed_command(value))


    def toggle(self, value):
        self._toggle_command(value)
        cmds.control("int_{}".format(self._name), e=True, en=value)


class CComboInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, items=[], changed_command=None, toggle_command=None, build=False):
        super(CComboInput, self).__init__(name, parent)

        self._enabled = enabled
        self._items = items
        self._changed_command = changed_command
        self._toggle_command = toggle_command

        if build:
            self.build_ui()


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.optionMenu("cmb_{}".format(self._name), p=layout, en=self._enabled, cc=lambda value: self._changed_command(value))

        for item in self._items:
            cmds.menuItem("itm_{}_{}".format(self._name, item), l=item)


    def toggle(self, value):
        self._toggle_command(value)
        cmds.control("cmb_{}".format(self._name), e=True, en=value)
