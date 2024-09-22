.PHONY: notebook
notebook:
	uv run jupyter notebook --port 8080 --no-browser

IPYNBS = $(shell ls chapter*/*.ipynb)

.PHONY: test
test:
	uv run jupyter nbconvert --inplace --execute $(IPYNBS)

.PHONY: clean
clean:
	uv run jupyter nbconvert --inplace --clear-output $(IPYNBS)
