import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifiers import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

#function to read yaml file
@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return a ConfigBox type.

    Args:
    path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty.
        e: empty  file

    Returns:
        ConfigBox: ConfigBox type

    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """Create list of directories.

    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool, optional): if True, print the directories created. Defaults to True.

    Returns:
        list: list of directories created

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")

@ensure_annotations