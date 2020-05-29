# output index.html

from jinja2 import Environment, FileSystemLoader
import os
import yaml

with open("advice.yaml", 'r') as stream:
    try:
        data = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root)
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('template.html')

for item in data:
    print(item)
    for k,v in enumerate(item):
        print(v)

filename = "index.html"
with open(filename, 'w') as fh:
    fh.write(template.render(
        h1 = "Hello Jinja2",
        data = data,
        show_one = True,
        show_two = False,
        names    = ["Foo", "Bar", "Qux"],
    ))