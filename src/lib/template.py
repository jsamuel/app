import jinja2
import os


TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../templates')

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
    autoescape=True)


def render(template_file, vars=None):
    if vars is None:
        vars = {}
    template = JINJA_ENV.get_template(template_file)
    return template.render(**vars)
