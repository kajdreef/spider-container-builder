import json
from jinja2 import Template
import docker
from io import BytesIO
import logging
import sys
import argparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def create_dockerfile(config):
    result = BytesIO()
    # Load template
    with open('resources/docker-template.j2') as f:
        template = Template(f.read())

    dockerfile_content = template.render(**config)
    result.write(dockerfile_content.encode('utf-8'))

    return result

def parse_arguments():
    parser = argparse.ArgumentParser(description="Build docker containers containing spiderlab developed tools")
    parser.add_argument('--force',  action='store_true', help="Force rebuild the containers")
    
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Connect to docker deamon.
    try:
        client = docker.from_env()
        logger.info("Connected to Docker daemon.")
    except:
        logger.error("Docker doesn't seem to be installed.")
        return 1

    # Load json config
    with open('resources/container-config.json') as f:
        config_dict = json.load(f)

    # Create configs and build containers
    for docker_file_name, config in config_dict.items():
        logger.info("Create docker image for: %s", docker_file_name)
        dockerfile = create_dockerfile(config)
        client.images.build(fileobj=dockerfile, tag=docker_file_name, quiet=False, nocache=args.force)
