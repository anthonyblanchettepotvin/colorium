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
        self._controls = []

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

        for control in self._controls:
            control.build_ui()

        callback()

        
    def build_ui(self):
        """
        Builds the tool's UI.
        """

        NotImplemented


    def add_control(self, control):
        if control not in self._controls:
            self._controls.append(control)

    
    def remove_control(self, control):
        if control in self._controls:
            self._controls.remove(control)


    def get_control_by_name(self, name):
        for control in self._controls:
            if control._name == name:
                return control


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


class CToggleable():
    def toggle(self, value):
        """
        Enables/disables the control.
        """

        NotImplemented


class CBindable():
    def bind(self, bindable):
        """
        Binds a bindable object to another bindable object.
        """

        NotImplemented


    def unbind(self, bindable):
        """
        Unbinds a bindable object from another bindable object.
        """

        NotImplemented


    def update(self, topic, value):
        """
        Sends an update to all bindings of the bindable object.
        """

        NotImplemented


class CControl(object, CBindable):
    def __init__(self, name, parent):
        self._bindings = []

        self._name = name
        self._parent = parent


    def build_ui(self):
        """
        Builds the control's UI.
        """

        NotImplemented


    def bind(self, bindable):
        if bindable not in self._bindings:
            self._bindings.append(bindable)

        
    def unbind(self, bindable):
        if bindable in self._bindings:
            self._bindings.remove(bindable)


    def notify(self, topic, value):
        for bindable in self._bindings:
            bindable.update(topic, value)

    
    def update(self, topic, value):
        NotImplemented


class CTextInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, changed_command=None, toggle_command=None, toggle=False):
        super(CTextInput, self).__init__(name, parent)

        self._enabled = enabled
        self._changed_command = changed_command
        self._toggle_command = toggle_command
        self._toggle = toggle


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        
        if self._toggle:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.textField("txt_{}".format(self._name), p=layout, en=self._enabled, tcc=lambda value: self._changed_command(value))


    def toggle(self, value):
        if self._toggle_command:
            self._toggle_command(value)
        
        cmds.control("txt_{}".format(self._name), e=True, en=value)


    def update(self, topic, value):
        if topic == self._name:
            cmds.textField("txt_{}".format(self._name), e=True, tx=value)
        elif topic == "has{}".format(self._name.title()) and self._toggle:
            cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
            cmds.control("txt_{}".format(self._name), e=True, en=value)


class CIntInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, min=1, max=10, changed_command=None, toggle_command=None, toggle=False):
        super(CIntInput, self).__init__(name, parent)

        self._enabled = enabled
        self._min = min
        self._max = max
        self._changed_command = changed_command
        self._toggle_command = toggle_command
        self._toggle = toggle


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        
        if self._toggle:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.intSliderGrp("int_{}".format(self._name), p=layout, f=True, min=self._min, max=self._max, en=self._enabled, cc=lambda value: self._changed_command(value))


    def toggle(self, value):
        if self._toggle_command:
            self._toggle_command(value)

        cmds.control("int_{}".format(self._name), e=True, en=value)


    def update(self, topic, value):
        if topic == self._name:
            cmds.intSliderGrp("int_{}".format(self._name), e=True, v=value)
        elif topic == "has{}".format(self._name.title()) and self._toggle:
            cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
            cmds.control("int_{}".format(self._name), e=True, en=value)


class CComboInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, items=[], changed_command=None, toggle_command=None, toggle=False):
        super(CComboInput, self).__init__(name, parent)

        self._enabled = enabled
        self._items = items
        self._changed_command = changed_command
        self._toggle_command = toggle_command
        self._toggle = toggle


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=3, cat=[(2, "right", 5)], cw=[(1, 25), (2, 100)], adj=3)
        
        if self._toggle:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l="Asset {}:".format(self._name), al="right")
        cmds.optionMenu("cmb_{}".format(self._name), p=layout, en=self._enabled, cc=lambda value: self._changed_command(value))

        for item in self._items:
            cmds.menuItem("itm_{}_{}".format(self._name, item), l=item)


    def toggle(self, value):
        if self._toggle_command:
            self._toggle_command(value)
        
        cmds.control("cmb_{}".format(self._name), e=True, en=value)

    
    def update(self, topic, value):
        if topic == self._name:
            cmds.optionMenu("cmb_{}".format(self._name), e=True, v=value)
        elif topic == "has{}".format(self._name.title()) and self._toggle:
            cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
            cmds.control("cmb_{}".format(self._name), e=True, en=value)


class CFilePathInput(CControl, CToggleable):
    def __init__(self, name, parent, enabled=True, changed_command=None, toggle_command=None, toggle=False):
        super(CFilePathInput, self).__init__(name, parent)

        self._enabled = enabled
        self._changed_command = changed_command
        self._toggle_command = toggle_command
        self._toggle = toggle


    def build_ui(self):
        layout = cmds.rowLayout("lay_{}".format(self._name), p=self._parent, nc=4, cat=[(2, "right", 5), (4, "left", 5)], cw=[(1, 25), (2, 100), (4, 100)], adj=3)
        
        if self._toggle:
            cmds.checkBox("chk_{}".format(self._name), p=layout, l="", v=self._enabled, cc=lambda value: self.toggle(value))
        else:
            cmds.separator("sep_{}".format(self._name), vis=False)

        cmds.text("lbl_{}".format(self._name), p=layout, l="{} Path:".format(self._name.title()), al="right")
        cmds.textField("txt_{}".format(self._name), p=layout, en=self._enabled, tcc=lambda value: self._changed_command(value))
        cmds.button("btn_open_{}".format(self._name), p=layout, l="Open")


    def toggle(self, value):
        if self._toggle_command:
            self._toggle_command(value)
        
        cmds.control("txt_{}".format(self._name), e=True, en=value)


    def update(self, topic, value):
        if topic == self._name:
            cmds.textField("txt_{}".format(self._name), e=True, tx=value)
        elif topic == "has{}".format(self._name.title()) and self._toggle:
            cmds.checkBox("chk_{}".format(self._name), e=True, v=value)
            cmds.control("txt_{}".format(self._name), e=True, en=value)
