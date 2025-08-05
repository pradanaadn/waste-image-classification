import os
from pathlib import Path
import kagglehub
from loguru import logger

LIST_DATASETS = [
    "sumn2u/garbage-classification-v2",
    "mostafaabla/garbage-classification",
    "vencerlanz09/plastic-paper-garbage-bag-synthetic-images",
    "vencerlanz09/plastic-and-paper-cups-synthetic-image-dataset",
    "joebeachcapital/realwaste",
]

try:
    download_path = Path(__file__).parent.joinpath("datasets")
    os.environ["KAGGLEHUB_CACHE"] = str(download_path)
    for dataset in LIST_DATASETS:
        path = kagglehub.dataset_download(dataset)

    logger.info(f"Path to dataset files: {path}")
except Exception as e:
    logger.error(f"An error occurred while downloading the dataset: {str(e)}")
