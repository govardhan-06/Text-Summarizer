# Text Summarizer

## Overview

This project implements a text summarization application using the Hugging Face Transformers library and FastAPI backend. The model used for summarization is `google/pegasus-newsroom`, fine-tuned on the `samsum dataset`.

## Features

- Summarize any given dialogue using the `google/pegasus-newsroom` model.
- RESTful API for text summarization.
- Easy to use and integrate into other applications.

## Installation

### Prerequisites

- Python 3.9+
- pip

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/govardhan-06/Text-Summarizer.git
   cd Text-Summarizer
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:
   ```bash
   python app.py
   ```

## API Endpoints

### GET /train

- **Description**: Train the model.

### POST /summarize

- **Description**: Summarize the provided text.
- **Request Body**:
  - `text` (string): The text to be summarized.
- **Response**:
  - `summary` (string): The summarized text.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
