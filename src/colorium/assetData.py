from patterns.observerPattern import Subject, Observer
import assetTypeDefinition

class AssetData(Subject, Observer):
    _observers = []

    _type = assetTypeDefinition.noneType
    _name = ""
    _hasVariant = False
    _variant = 1
    _hasScene = False
    _scene = 10
    _hasShot = False
    _shot = 10
    _version = 1
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
        self.notify("type", value)
    
    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, value):
        self._name = value
        self.notify("name", value)
    
    @property
    def hasVariant(self):
        return self._hasVariant
    
    @hasVariant.setter
    def hasVariant(self, value):
        self._hasVariant = value
        self.notify("hasVariant", value)
    
    @property
    def variant(self):
        return self._variant
    
    @variant.setter
    def variant(self, value):
        self._variant = value
        self.notify("variant", value)
    
    @property
    def hasScene(self):
        return self._hasScene
    
    @hasScene.setter
    def hasScene(self, value):
        self._hasScene = value
        self.notify("hasScene", value)
    
    @property
    def scene(self):
        return self._scene
    
    @scene.setter
    def scene(self, value):
        self._scene = value
        self.notify("scene", value)
    
    @property
    def hasShot(self):
        return self._hasShot
    
    @hasShot.setter
    def hasShot(self, value):
        self._hasShot = value
        self.notify("hasShot", value)
    
    @property
    def shot(self):
        return self._shot
    
    @shot.setter
    def shot(self, value):
        self._shot = value
        self.notify("shot", value)

    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        self._version = value
        self.notify("version", value)
        
    def __init__(self, type=None, name="", hasVariant=False, variant=1, hasScene=False, scene=10, hasShot=False, shot=10, version=1):
        if type != None:
            self._type = type

        self._name = name
        self._hasVariant = hasVariant
        self._variant = variant
        self._hasScene = hasScene
        self._scene = scene
        self._hasShot = hasShot
        self._shot = shot
        self._version = version

    def attach(self, observer):
        self._observers.append(observer)

    def attachAndNotify(self, observer):
        self.attach(observer)
        self.notify()

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.update(args)

    def clearObservers(self):
        self._observers = []

    def update(self, *args):
        prop = args[0]
        value = args[1]

        if prop == "name":
            self.name = value
        elif prop == "type":
            self.type = value
        elif prop == "hasVariant":
            self.hasVariant = value
        elif prop == "variant":
            self.variant = value
        elif prop == "hasScene":
            self.hasScene = value
        elif prop == "scene":
            self.scene = value
        elif prop == "hasShot":
            self.hasShot = value
        elif prop == "shot":
            self.shot = value
        elif prop == "version":
            self.version = value
