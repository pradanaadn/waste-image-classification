from roboflow import Roboflow

LIST_DATASET = [
    "beverage-containers-3atxb"
]

rf = Roboflow(api_key="LRRjhLvhz6FI3dVLj7CK")
project = rf.workspace("roboflow-universe-projects").project(
    "beverage-containers-3atxb"
)
version = project.version(8)
dataset = version.download("coco", location="./datasets/roboflow/beverage-containers")
