#!/bin/sh

container=$1

images=($(docker images | tail -n +2 | grep -o '^\S*' ))

# Check if the container you want to start is in the list of containers
if [[ " ${images[@]} " =~ " ${container} " ]]; then
	echo "Start: ${container}"
	docker run -i -t "$container" /bin/bash
else
	echo "[Error] container is not available"
fi
