from roboflow import Roboflow
from loguru import logger

LIST_DATASET = [
    ("coco", "a-3zezt", "styrofoam-wfuot", 1),
    ("coco", "ijuden", "kelapa-megatron-kupas", 1),
    ("coco", "dataixalab", "metal-f7t6c", 1),
    ("folder", "trash-classification-mjez0", "plastic-hdpe", 1),
    ("coco", "project-swd48", "plastic-cups-v7jar", 1),
    ("coco", "cups-iupj5", "cups-ctpw3", 1),
    ("folder", "recyclable-sorting-algorithm", "plastic-sorting-algorithm", 1),
    ("folder", "piyush-yadav-gh70a", "pvc-pipe-detection", 1),
    ("folder", "tiago-rosa", "un-pvc", 1),
]
try:
    rf = Roboflow(api_key="LRRjhLvhz6FI3dVLj7CK")
    for output_format, workspace, dataset, version_number in LIST_DATASET:
        logger.info(f"Downloading dataset: {dataset}")
        project = rf.workspace(workspace).project(dataset)
        version = project.version(version_number)
        dataset = version.download(
            output_format, location=f"./datasets/roboflow/{dataset}"
        )
except Exception as e:
    logger.error(f"An error occurred while downloading the dataset: {e}")
