## datasets_searchpath_plugins

SearchPath plugins are automatically discovered and enabled after installation. They provide configuration files (*.yaml) for datasets corresponding to specific tasks.

### Key Features

- **Automatic Configuration Discovery**: Users can easily discover and create configurations tailored to their needs.

- **Hydra Integration**: Automatically extends Hydra with the keyword **"base"**, allowing for the addition of extra configurations within existing configuration groups.

- **Configuration Priority**: Hydra prepends its configurations, ensuring they take precedence over any configurations they are intended to replace.

- **Flexible Overrides**: Configurations can be replaced flexibly to suit various requirements.

This setup simplifies the management of datasets and enhances the flexibility of configuration management.