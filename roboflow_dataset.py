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
    ("coco","demo-wdd86", "od-3vc4m", 1),
    ("coco","construction-8c2ry", "pipe-fittings", 1),
    ("folder","sumeyye-mo9wj", "paper-7qwal", 1),
    ("folder","rijah-yrbls", "paper-d2z5n", 1),
    ("folder","trash-classification-mjez0", "paper-1", 2),
    ("folder","color-qltok", "pet-bottle-9xet7", 1),
    ("folder","computer-vision-ewm5r", "botol-pjepi", 4),
    ("coco","university-d2l2p", "tetrapak-xczol", 2),
    ("coco","project-space-12", "egg-tray-count", 1),
    ("folder","manuelmulattieri97", "bottlecap-side", 3),
    ("coco","work3-dqzz5", "bottle-cap-y6pzg", 1),
    ("folder","kabies-sickkk", "svm-plastic-and-metal", 2),
    ("coco","tgmt-wgnd8", "metal-ipkdz", 1),
    ("coco","talovtask", "plastic-bag-tlche", 1),
    ("coco","new-workspace-slpmv", "bag-qe348", 4),
    ("coco","testee-rv5vr", "metal-zn5s0", 1),
    ("coco","minhthong", "glass-model", 2),
    ("coco","project-qynru", "glass-fc9h7", 1),
    ("coco","hana-ygz4l", "tri-des-dechets-hdpe", 1),
    ("folder","nararit", "classification-pet-hdpe", 3),
    
    
    
    
    
    
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
