# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# type: ignore
from setuptools import find_namespace_packages, setup, find_packages


setup(
    name="hydra-udl-searchpath-plugin",
    version="1.0.0",
    author="Xiao Wu",
    author_email="wxwsx1997@gmail.com",
    description="loading datasets conf using Hydra SearchPath plugin",
    url="https://github.com/facebookresearch/hydra/",
    packages=find_namespace_packages(include=["hydra_plugins.*"])
    + find_packages(include=["customized.*"]),
    classifiers=[
        # Feel free to use another license.
        "License :: OSI Approved :: MIT License",
        # Hydra uses Python version and Operating system to determine
        # In which environments to test this plugin
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # consider pinning to a specific major version of Hydra to avoid unexpected problems
        # if a new major version of Hydra introduces breaking changes for plugins.
        # e.g: "hydra-core==1.0.*",
        "hydra-core",
    ],
    # If this plugin is providing configuration files, be sure to include them in the package.
    # See MANIFEST.in.
    # For configurations to be discoverable at runtime, they should also be added to the search path.
    include_package_data=True,
)
