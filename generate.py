from jinja2 import Environment, FileSystemLoader
import os
import yaml
import black

with open("advice.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root)
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("template.html")

tips = []

for entry in data:
    print(entry)
    print(entry["audience"])
    tips.append(entry["tip"])
    for k in entry.keys():
        print(k)


filename = "index.html"
with open(filename, "w") as fh:
    fh.write(template.render(tips=tips, data=data,))
