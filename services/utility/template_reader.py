from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

from config import logger, ROOT_DIR

TEMPLATES_DIR = os.path.join(ROOT_DIR, "resources", 'templates')

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)
logger.info(TEMPLATES_DIR)

def render_template(template_name: str, context: dict) -> str:

    template = env.get_template(template_name)
    return template.render(context)
