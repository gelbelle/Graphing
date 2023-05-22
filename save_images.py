import json

import junix

if __name__ == "__main__":

    with open("pies2.ipynb", "r") as f:
        notebook_dict = json.load(f)

    with open("pies.json", "w") as f:
        json.dump(notebook_dict, f)

    junix.export_images(
        filepath="pies2.ipynb",
        output_dir="charts/pies",
        prefix="nb",
    )
