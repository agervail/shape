IMAGE_NAME:=showyou/shapesetector
CONTAINER_NAME:=ShapeDetection

build-image:
	docker build -t $(IMAGE_NAME) .

start-image:
	docker run -d -t -v $(CURDIR):/ShapeDetector --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)

run-bash:
	docker exec -it $(CONTAINER_NAME) /bin/bash

generate-png:
	docker exec -it $(CONTAINER_NAME) python read_dxf.py --convert-to-png --delete-svg

stop-image:
	docker stop $(CONTAINER_NAME)

remove-image:
	docker rm $(IMAGE_NAME)

