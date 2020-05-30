from jinja2 import Environment, FileSystemLoader
import os
import yaml

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
basic = []
intermediate = []
advanced = []
campaigns = []
all = []

count = []

for entry in data:
    print(entry)
    tips.append(entry["tip"])
    if entry["audience"] == "campaigns":
        campaigns.append(entry["tip"])
    else:
        all.append(entry["tip"])

    if entry["level"] == "basic" and entry["audience"] != "campaigns":
        basic.append(entry["tip"])
    elif entry["level"] == "intermediate" and entry["audience"] != "campaigns":
        intermediate.append(entry["tip"])
    elif entry["level"] == "advanced" and entry["audience"] != "campaigns":
        advanced.append(entry["tip"])

filename = "index.html"
with open(filename, "w") as fh:
    fh.write(template.render(
        tips=tips, 
        data=data,
        basic=basic,
        intermediate=intermediate,
        advanced=advanced,
        campaigns=campaigns,
        ))
