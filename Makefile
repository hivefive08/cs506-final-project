# Install core dependencies for running the Flask app
install:
	pip install -r requirements.txt

# Run the Flask app
run:
	python app.py

# Clean up unnecessary files and folders
clean:
	rm -rf __pycache__

