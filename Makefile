# Install core dependencies for running the Flask app
install:
	pip install -r requirements.txt

# Run the Flask app
run:
	python app.py

# Run Jupyter Notebook
notebook:
	jupyter notebook

# Clean up unnecessary files and folders
clean:
	rm -rf __pycache__
	rm -rf .ipynb_checkpoints
