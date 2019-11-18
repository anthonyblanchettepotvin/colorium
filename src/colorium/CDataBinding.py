

class CBinding():

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, value):
        self.__obj = value


    @property
    def obj_prop(self):
        return self.__obj_prop

    @obj_prop.setter
    def obj_prop(self, value):
        self.__obj_prop = value


    @property
    def prop(self):
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
        else:
            return False


    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True


    def update_prop(self, value):
        obj_type = type(self.__obj)

        if self.__obj_prop not in obj_type.__dict__:
            print('{!r} is not an attribute of class {}'.format(self.__obj_prop, obj_type.__name__))
        else:
            prop = obj_type.__dict__[self.__obj_prop]

            if not isinstance(prop, property):
                print('{!r} is not a property of class {}'.format(self.__obj_prop, obj_type.__name__))

            self.__obj.notified = True

            prop.__set__(self.__obj, value)

            self.__obj.notified = False


class CBindable():

    @property
    def notified(self):
        return self.__notified

    @notified.setter
    def notified(self, value):
        self.__notified = value


    def __init__(self):
        self.__bindings = []
        self.__notified = False


    def add_binding(self, bind):
        if not self.__bindings:
            self.__bindings.append(bind)
        else:
            found = False

            for binding in self.__bindings:
                if binding == bind:
                    found = True

            if not found:     
                self.__bindings.append(bind)


    def remove_binding(self, bind):
        if self.__bindings:
            for binding in self.__bindings:
                if binding == bind:
                    self.__bindings.remove(binding)
    

    def notify_property_changed(self, prop, value):
        if not self.__notified:
            for binding in self.__bindings:
                if binding.prop == prop:
                    binding.update_prop(value)


def bind(obj_a, obj_a_property, obj_b, obj_b_property, two_way=True):
    if is_valid_property(obj_a, obj_a_property) and is_valid_property(obj_b, obj_b_property):
        binding_a = CBinding(obj_a, obj_a_property, obj_b_property)

        obj_b.add_binding(binding_a)

        if two_way:
            binding_b = CBinding(obj_b, obj_b_property, obj_a_property)

            obj_a.add_binding(binding_b)


def unbind(obj_a, obj_a_property, obj_b, obj_b_property, two_way=True):
    if is_valid_property(obj_a, obj_a_property) and is_valid_property(obj_b, obj_b_property):
        binding_a = CBinding(obj_a, obj_a_property, obj_b_property)

        obj_b.remove_binding(binding_a)

        if two_way:
            binding_b = CBinding(obj_b, obj_b_property, obj_a_property)

            obj_a.remove_binding(binding_b)


def is_valid_property(obj, prop):
    obj_type = type(obj)

    if prop not in obj_type.__dict__:
            print('{!r} is not an attribute of class {}'.format(prop, obj_type.__name__))

            return False
    else:
        prop = obj_type.__dict__[prop]

        if not isinstance(prop, property):
            print('{!r} is not a property of class {}'.format(prop, obj_type.__name__))

            return False

    return True
