from colorium.CConfiguration import CConfiguration

import assetTypeDefinition
import colorium.CDataBinding as CDataBinding
import namingConvention


class CAsset(object, CDataBinding.CBindable):
    @property
    def hasType(self):
        return self._hasType
    
    @hasType.setter
    def hasType(self, value):
        self._hasType = value
        self.notify_configurations()
        self.notify_property_changed("hasType", value)
        print('\'hasType\' property of CAsset set to \'{}\'').format(value)


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.notify_configurations()
        self.notify_property_changed("type", value)
        print('\'type\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def hasName(self):
        return self._hasName
    
    @hasName.setter
    def hasName(self, value):
        self._hasName = value
        self.notify_configurations()
        self.notify_property_changed("hasName", value)
        print('\'hasName\' property of CAsset set to \'{}\'').format(value)


    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, value):
        self._name = value
        self.notify_configurations()
        self.notify_property_changed("name", value)
        print('\'name\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def hasVariant(self):
        return self._hasVariant
    
    @hasVariant.setter
    def hasVariant(self, value):
        self._hasVariant = value
        self.notify_configurations()
        self.notify_property_changed("hasVariant", value)
        print('\'hasVariant\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def variant(self):
        return self._variant
    
    @variant.setter
    def variant(self, value):
        self._variant = value
        self.notify_configurations()
        self.notify_property_changed("variant", value)
        print('\'variant\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def hasScene(self):
        return self._hasScene
    
    @hasScene.setter
    def hasScene(self, value):
        self._hasScene = value
        self.notify_configurations()
        self.notify_property_changed("hasScene", value)
        print('\'hasScene\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def scene(self):
        return self._scene
    
    @scene.setter
    def scene(self, value):
        self._scene = value
        self.notify_configurations()
        self.notify_property_changed("scene", value)
        print('\'scene\' property of CAsset set to \'{}\'').format(value)


    @property
    def hasShot(self):
        return self._hasShot
    
    @hasShot.setter
    def hasShot(self, value):
        self._hasShot = value
        self.notify_configurations()
        self.notify_property_changed("hasShot", value)
        print('\'hasShot\' property of CAsset set to \'{}\'').format(value)
    

    @property
    def shot(self):
        return self._shot
    
    @shot.setter
    def shot(self, value):
        self._shot = value
        self.notify_configurations()
        self.notify_property_changed("shot", value)
        print('\'shot\' property of CAsset set to \'{}\'').format(value)


    @property
    def hasVersion(self):
        return self._hasVersion
    
    @hasVersion.setter
    def hasVersion(self, value):
        self._hasVersion = value
        self.notify_configurations()
        self.notify_property_changed("hasVersion", value)
        print('\'hasVersion\' property of CAsset set to \'{}\'').format(value)


    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        self._version = value
        self.notify_configurations()
        self.notify_property_changed("version", value)
        print('\'version\' property of CAsset set to \'{}\'').format(value)

    
    @property
    def save_config(self):
        return self._save_config

    @save_config.setter
    def save_config(self, value):
        self._save_config = value
        self.notify_configurations()
        self.notify_property_changed("save_config", value)
        print('\'save_config\' property of CAsset set to \'{}\'').format(value)


    @property
    def publish_config(self):
        return self._publish_config

    @publish_config.setter
    def publish_config(self, value):
        self._publish_config = value
        self.notify_configurations()
        self.notify_property_changed("publish_config", value)
        print('\'publish_config\' property of CAsset set to \'{}\'').format(value)


    @property
    def export_config(self):
        return self._export_config

    @export_config.setter
    def export_config(self, value):
        self._export_config = value
        self.notify_configurations()
        self.notify_property_changed("export_config", value)
        print('\'export_config\' property of CAsset set to \'{}\'').format(value)


    def __init__(self, hasType=False, type="non", hasName=False, name="unamed", hasVariant=False, variant=1, hasScene=False, scene=10, hasShot=False, shot=10, hasVersion=False, version=1, save_config=None, publish_config=None, export_config=None):
        CDataBinding.CBindable.__init__(self)

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
            self._save_config = CConfiguration("save", self,\
                file_name_generator_function=namingConvention.generateFileNameForSavedAsset,\
                path_generator_function=namingConvention.generatePathForSavedAsset,\
                )

        if publish_config:
            self._publish_config = publish_config
        else:  
            self._publish_config = CConfiguration("publish", self,\
                file_name_generator_function=namingConvention.generateFileNameForPublishedAsset,\
                path_generator_function=namingConvention.generatePathForPublishedAsset,\
                )

        if export_config:
            self._export_config = export_config
        else:
            self._export_config = CConfiguration("export", self,\
                file_name_generator_function=namingConvention.generateFileNameForExportedAsset,\
                path_generator_function=namingConvention.generatePathForExportedAsset,\
                )


    def notify_configurations(self):
        self.save_config.update()
        self.publish_config.update()
        self.export_config.update()
