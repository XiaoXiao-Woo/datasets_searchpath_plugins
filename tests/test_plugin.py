# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from hydra.core.global_hydra import GlobalHydra
from hydra.core.plugins import Plugins
from hydra import initialize
from hydra.plugins.search_path_plugin import SearchPathPlugin
from hydra_plugins.searchpath_plugin.searchpath_plugin import CustomizedSearchPathPlugin


def test_discovery() -> None:
    # Tests that this plugin can be discovered via the plugins subsystem when looking at all Plugins
    assert CustomizedSearchPathPlugin.__name__ in [
        x.__name__ for x in Plugins.instance().discover(SearchPathPlugin)
    ]


def test_config_installed() -> None:
    with initialize(version_base=None):
        hydra = GlobalHydra.instance()
        config_loader = hydra.config_loader()
        for name in config_loader.get_group_options("base"):
            print(hydra.hydra._print_search_path(name, ""))


test_discovery()
test_config_installed()
