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
