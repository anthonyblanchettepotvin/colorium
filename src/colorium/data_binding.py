"""Module that contains a variety of functions and classes used to bind classes' properties together."""


class CBinding(object):
    """Description of a binding between two bindable objects : the source object (children of this class) and the destination object."""

    @property
    def obj(self):
        """The instance of the destination object that has the binded property."""

        return self.__obj

    @obj.setter
    def obj(self, value):
        self.__obj = value


    @property
    def obj_prop(self):
        """The destination object's binded property's name."""

        return self.__obj_prop

    @obj_prop.setter
    def obj_prop(self, value):
        self.__obj_prop = value


    @property
    def prop(self):
        """The property's name of the source object itself."""

        return self.__prop

    @prop.setter
    def prop(self, value):
        self.__prop = value


    def __init__(self, obj, obj_prop, prop):
        self.__obj = obj
        self.__obj_prop = obj_prop
        self.__prop = prop


    def __eq__(self, other):
        if self.__obj is other.obj and self.__obj_prop == other.obj_prop and self.__prop == other.prop:
            return True

        return False


    def __ne__(self, other):
        if self.__eq__(other):
            return False

        return True


    def update_prop(self, value):
        """Update the destination object's property value with the new source object's property value."""

        obj_type = type(self.__obj)

        if self.__obj_prop not in obj_type.__dict__:
            print '{!r} is not an attribute of class {}'.format(self.__obj_prop, obj_type.__name__)
        else:
            prop = obj_type.__dict__[self.__obj_prop]

            if not isinstance(prop, property):
                print '{!r} is not a property of class {}'.format(self.__obj_prop, obj_type.__name__)

            self.__obj.notified = True

            prop.__set__(self.__obj, value)

            self.__obj.notified = False


class CBindable():
    """\"Interface\" used to define a bindable object. A bindable object's properties can be bound to another bindable object's properties.
    The notify_property_changed function can be used in the setter fucntion of a bindable object's property to notify any bindable object's property
    bound to the notifier."""

    @property
    def notified(self):
        """Indicates if the object is being notify."""

        return self.__notified

    @notified.setter
    def notified(self, value):
        self.__notified = value


    def __init__(self):
        self.__bindings = []
        self.__notified = False


    def add_binding(self, new_binding):
        """Add a binding the object's binding list."""

        if not self.__bindings:
            self.__bindings.append(new_binding)
        else:
            found = False

            for binding in self.__bindings:
                if binding == new_binding:
                    found = True

            if not found:
                self.__bindings.append(new_binding)


    def remove_binding(self, old_binding):
        """Add a binding the object's binding list."""

        if self.__bindings:
            for binding in self.__bindings:
                if binding == old_binding:
                    self.__bindings.remove(binding)


    def notify_property_changed(self, prop, value):
        """Notifies the bindings in the object's binding list that match the specified property and sends them the new value."""

        if not self.__notified:
            for binding in self.__bindings:
                if binding.prop == prop:
                    binding.update_prop(value)


def bind(obj_a, obj_a_property, obj_b, obj_b_property, two_way=True):
    """Binds a object's property to another object's property."""

    if is_valid_property(obj_a, obj_a_property) and is_valid_property(obj_b, obj_b_property):
        binding_a = CBinding(obj_a, obj_a_property, obj_b_property)

        obj_b.add_binding(binding_a)

        if two_way:
            binding_b = CBinding(obj_b, obj_b_property, obj_a_property)

            obj_a.add_binding(binding_b)


def unbind(obj_a, obj_a_property, obj_b, obj_b_property, two_way=True):
    """Unbinds a object's property from another object's property."""

    if is_valid_property(obj_a, obj_a_property) and is_valid_property(obj_b, obj_b_property):
        binding_a = CBinding(obj_a, obj_a_property, obj_b_property)

        obj_b.remove_binding(binding_a)

        if two_way:
            binding_b = CBinding(obj_b, obj_b_property, obj_a_property)

            obj_a.remove_binding(binding_b)


def is_valid_property(obj, prop):
    """Checks if a property on a object is valid/exists."""

    obj_type = type(obj)

    if prop not in obj_type.__dict__:
        print '{!r} is not an attribute of class {}'.format(prop, obj_type.__name__)

        return False
    else:
        prop = obj_type.__dict__[prop]

        if not isinstance(prop, property):
            print '{!r} is not a property of class {}'.format(prop, obj_type.__name__)

            return False

    return True
