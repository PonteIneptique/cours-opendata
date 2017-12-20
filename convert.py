from csv import DictReader
from csv import DictWriter

nodes = {}
edges = []

with open("enc.tsv.csv") as src_file:
    lines = DictReader(src_file, delimiter="\t")

    for line in lines:
        if line["id"] not in nodes:
            nodes[line["id"]] = line["label"]
        if line["in"] not in nodes:
            nodes[line["in"]] = line["label_in"]
        edges.append(
            {"source": line["id"], "target": line["in"], "label": line["label_relation"]}
        )

with open("chapitre-3/nodes.csv", "w") as nodes_file:
    writer = DictWriter(nodes_file, ["id", "label"])
    writer.writeheader()
    for nid, label in nodes.items():
        writer.writerow({"id": nid, "label": label})

with open("chapitre-3/edges.csv", "w") as nodes_file:
    writer = DictWriter(nodes_file, ["source", "target", "label"])
    writer.writeheader()
    for node in edges:
        writer.writerow(node)
