from colorium.CUI import CBindable
from colorium.CConfiguration import SaveConfiguration, PublishConfiguration, ExportConfiguration
import assetTypeDefinition

class CAsset(object, CBindable):
    @property
    def hasType(self):
        return self._hasType
    
    @hasType.setter
    def hasType(self, value):
        self._hasType = value
        self.notify("hasType", value)


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.notify("type", value)
    

    @property
    def hasName(self):
        return self._hasName
    
    @hasName.setter
    def hasName(self, value):
        self._hasName = value
        self.notify("hasName", value)


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
    def hasVersion(self):
        return self._hasVersion
    
    @hasVersion.setter
    def hasVersion(self, value):
        self._hasVersion = value
        self.notify("hasVersion", value)


    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        self._version = value
        self.notify("version", value)

    
    @property
    def save_config(self):
        return self._save_config

    @save_config.setter
    def save_config(self, value):
        self._save_config = value
        self.notify("save_config", value)


    @property
    def publish_config(self):
        return self._publish_config

    @publish_config.setter
    def publish_config(self, value):
        self._publish_config = value
        self.notify("publish_config", value)


    @property
    def export_config(self):
        return self._export_config

    @export_config.setter
    def export_config(self, value):
        self._export_config = value
        self.notify("export_config", value)


    def __init__(self, hasType=False, type="non", hasName=False, name="unamed", hasVariant=False, variant=1, hasScene=False, scene=10, hasShot=False, shot=10, hasVersion=False, version=1, save_config=None, publish_config=None, export_config=None):
        self._bindings = []
        
        self._hasType = hasType
        self._type = type
        self._hasName = hasName
        self._name = name
        self._hasVariant = hasVariant
        self._variant = variant
        self._hasScene = hasScene
        self._scene = scene
        self._hasShot = hasShot
        self._shot = shot
        self._hasVersion = hasVersion
        self._version = version

        if save_config:
            self._save_config = save_config
        else:
            self._save_config = SaveConfiguration("save", self)

        if publish_config:
            self._publish_config = publish_config
        else:  
            self._publish_config = PublishConfiguration("publish", self)

        if export_config:
            self._export_config = export_config
        else:
            self._export_config = ExportConfiguration("export", self)


    def bind(self, bindable):
        if bindable not in self._bindings:
            self._bindings.append(bindable)

        
    def unbind(self, bindable):
        if bindable in self._bindings:
            self._bindings.remove(bindable)


    def notify(self, topic, value):
        self._save_config.update(topic, value)
        self._publish_config.update(topic, value)
        self._export_config.update(topic, value)

        for bindable in self._bindings:
            bindable.update(topic, value)


    def update(self, topic, value):
        NotImplemented
