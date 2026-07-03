# HR Chatbot

This repository contains a simple HR document search prototype that uses vector search to answer questions from HR policies.

It demonstrates how to:
- create text embeddings with OpenAI,
- store vectors in a local Qdrant collection,
- index company policy text,
- and run similarity search on user queries.

## How it works

1. `database/hr.db` stores the HR employee data used for SQL-style lookups and entity matching.
2. `app/database_setup.py` creates the SQLite database and the `employees` table if they do not already exist.
3. `documents/leave_policy_detailed.txt` contains the HR policy text that is indexed for semantic search.
4. `app/index_documents.py` reads the policy, splits it into chunks, and converts each chunk into a high-dimensional vector using OpenAI embeddings.
5. The vectors and their text payloads are stored in a local Qdrant collection named `hr_docs` under `qdrant_data/`.
6. `app/text_normalizer.py` and `app/query_preprocessor.py` clean and normalize the user input before it is routed to search or SQL logic.
7. `app/chat.py`, `app/main.py`, and `app/chatbot.py` create embeddings or SQL-aware prompts for a query and use retrieval, hybrid search, or database lookup to find the most relevant policy or employee information.
8. Matching document chunks, SQL results, or hybrid results are returned with relevance scores or context so you can inspect the supporting evidence.

## How the modules work together

This project has a document-search pipeline and a database-driven pipeline that can work together:

- `chunker.py`: breaks a long document into small pieces called "chunks" (default 1000 characters). Smaller pieces give better results when creating embeddings.
- `embeddings.py`: calls OpenAI to convert a text chunk into a numeric vector (an embedding) that represents the meaning of the text.
- `index_documents.py`: the orchestrator for the document flow. It reads the document(s), calls the chunker to split text, calls the embeddings helper for each chunk, and uploads each vector + text payload to Qdrant.
- `qdrant_service.py`: creates or resets the `hr_docs` collection in Qdrant with the correct vector size and distance metric. Run this once before indexing.
- `database_setup.py`: creates the SQLite database at `database/hr.db` and the `employees` table used for structured HR data lookups.
- `sql_search.py`: runs SQL queries against the SQLite database and returns structured results.
- `query_preprocessor.py` and `text_normalizer.py`: prepare and normalize user questions before they are sent to SQL or retrieval logic.

End-to-end flow (simple):

1. Run `python3 app/database_setup.py` to create the SQLite database and `employees` table.
2. Run `python3 app/qdrant_service.py` to create the Qdrant collection for document embeddings.
3. Run `python3 app/index_documents.py` to read documents, chunk them, create embeddings, and store vectors in Qdrant.
4. Run `python3 app/chat.py` (or `python3 app/main.py` or `python3 app/chatbot.py`) to normalize the question, run SQL lookup or document retrieval, and combine the results in a hybrid flow when needed.

Each step shows simple console output so beginners can see what happened (example: "Indexed Successfully" after indexing). If you want, I can add a visual inspector to list stored points from Qdrant.

## Project structure

- `app/` - This folder contains all the Python scripts that run the chatbot.
  - `chat.py` - A simple script you can run to ask questions. It finds the answer from the HR policy.
  - `main.py` - Another way to ask questions about the HR policy. Same as chat.py but organized differently.
  - `embeddings.py` - Converts words and sentences into numbers that the computer can compare. Uses OpenAI.
  - `entity_extractor.py` - Extracts structured entities from a natural-language question so downstream logic can understand user intent more precisely.
  - `text_normalizer.py` - Cleans and standardizes user text so downstream search and prompt logic receives consistent input.
  - `query_preprocessor.py` - Prepares and corrects user questions before they are passed to SQL or retrieval logic.
  - `index_documents.py` - Reads the policy file, breaks it into small pieces, and saves it in Qdrant so it can be searched.
  - `qdrant_service.py` - Prepares the database (Qdrant) to store the HR policy information.
  - `chunker.py` - A helper tool that breaks big text into smaller pieces.
  - `extract_pdf.py` - A tool to read documents from the `documents/` folder. It now supports:
    - `.txt`
    - `.pdf`
    - `.docx` and `.doc`
    - `.xlsx` and `.xls`
    The helper extracts text from each file so it can be indexed and searched.
  - `database_setup.py` - Creates the local SQLite database and the `employees` table used by the chatbot and SQL search features.
  - `sql_search.py` - Provides SQL search helper functions to query the database and return structured results.
  - `text_to_sql.py` - Converts natural language questions into SQL queries or SQL-aware prompts for the chatbot.
  - `prompt_builder.py` - Builds system and user prompts for the chatbot, including document and SQL prompt templates.
  - `chatbot.py` - The conversational interface that accepts user questions and routes them through the SQL / vector search pipeline.
  - `search.py` - Placeholder for shared search functions and reusable query logic.
- `documents/` - This folder holds the HR policy files.
  - `leave_policy_detailed.txt` - Comprehensive HR policy text about leaves, remote work, and other policies. This is the file we search through.
- `qdrant_data/` - This folder stores the vector database. It saves all the information about the policy in a searchable format.
 
## About new app files

- `database_setup.py` - Creates the local SQLite database at `database/hr.db` and defines the `employees` table schema.
- `sql_search.py` - Runs SQL queries against the configured database and returns matching results.
- `text_to_sql.py` - Converts user text questions into SQL statements or SQL-aware search prompts.
- `prompt_builder.py` - Builds system and user prompts for the chatbot, including document and SQL prompt templates.
- `chatbot.py` - A higher-level chat interface that blends natural language understanding with SQL and vector search to answer HR questions.

## About `database_setup.py`

`database_setup.py` creates the SQL database and table used by the chatbot.

- Creates the `database/` directory if needed.
- Creates `database/hr.db`.
- Creates `employees` table with columns:
  - `id` INTEGER PRIMARY KEY
  - `name` TEXT
  - `department` TEXT
  - `salary` INTEGER
  - `leave_balance` INTEGER

How to run:

```bash
python3 app/database_setup.py
```

This ensures the SQL backend exists before you run `sql_search.py`, `text_to_sql.py`, or `chatbot.py`.

## About `chunker.py`

`chunker.py` is a small helper that breaks long documents into short pieces called "chunks." Each chunk is a short slice of text (default 1000 characters). We create chunks because the embedding model and the search database work better with smaller pieces of text.

How to run the chunker (shows what it does):

```bash
python3 app/chunker.py
```

This will read `documents/leave_policy_detailed.txt` (if present) and print how many chunks were created and a preview of the first chunk.

## About `entity_extractor.py`

`entity_extractor.py` provides a small helper for turning a user question into a structured entity payload. It sends the question to an OpenAI chat model and asks for a JSON response that can be used by the rest of the chatbot pipeline.

Typical use:

```python
from app.entity_extractor import extract_entities

entities = extract_entities("Who is the HR contact for leave requests?")
print(entities)
```

This is useful when the chatbot needs to identify things like people, departments, policy topics, or other relevant entities from a question before answering it.

## About `text_normalizer.py`

`text_normalizer.py` cleans and standardizes text before it is used in search or prompt-building workflows. It helps reduce noise in user input by handling common formatting issues such as extra whitespace, repeated punctuation, or inconsistent casing.

Typical use:

```python
from app.text_normalizer import normalize_text

clean_text = normalize_text("  Please  explain leave policy   ")
print(clean_text)
```

This module is useful when the chatbot needs a more consistent version of a user query before further processing.

## About `query_preprocessor.py`

`query_preprocessor.py` prepares user questions before they are passed to the SQL or retrieval layers. It can correct likely misspellings in employee names or departments and find the closest matching values from the database.

Typical use:

```python
from app.query_preprocessor import correct_question

corrected = correct_question("show me employees from enginering")
print(corrected)
```

This module is especially helpful when the chatbot needs to normalize ambiguous user input before generating SQL or searching documents.

## Requirements

- Python 3.10 or newer
- OpenAI API key
- Python packages:
  - `qdrant-client`
  - `openai`
  - `python-dotenv`
  - `python-docx` (for Word `.docx` / `.doc` files)
  - `openpyxl` (for Excel `.xlsx` / `.xls` files)
- A local Python virtual environment (recommended)

## Create the project

If you are starting from scratch, follow these steps:

1. Create a project folder and enter it:

```bash
mkdir hr_chatbot
cd hr_chatbot
```

2. Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Create the required directories and files:

```bash
mkdir app documents qdrant_data
touch README.md .env
```

4. Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Install dependencies

1. Activate the virtual environment if not already active:

```bash
source .venv/bin/activate
```

2. Install the required Python packages:

```bash
python3 -m pip install qdrant-client openai python-dotenv python-docx openpyxl
```

3. Verify the `qdrant_data/` directory exists:

```bash
mkdir -p qdrant_data
```

4. Optionally save dependencies:

```bash
python3 -m pip freeze > requirements.txt
```

## Setup

1. Make sure `.env` contains your OpenAI key:

```env
OPENAI_API_KEY=your_api_key_here
```

2. Ensure the `qdrant_data/` directory exists:

```bash
mkdir -p qdrant_data
```

## Usage

1. Create or recreate the Qdrant collection:

```bash
python3 app/qdrant_service.py
```

or:

```bash
python3 app/main.py
```

## Detailed Setup Steps

### 1. Set up Qdrant collection

This step prepares the database to store your HR documents.

- Open a terminal in the project folder
- Activate your virtual environment: `source .venv/bin/activate`
- Run the setup command: `python3 app/qdrant_service.py`
- You should see: "Collection created"

### 2. Index the detailed policy document

This step reads the HR policy and saves it in a searchable format.

- Make sure you are in the project folder
- Make sure your virtual environment is active
- Run the index command: `python3 app/index_documents.py`
- You should see: "Indexed Successfully"

### 3. Query the indexed documents

This step lets you ask questions about the HR policy.

- Make sure you are in the project folder
- Make sure your virtual environment is active
- Run the query command: `python3 app/chat.py`
- Change the question in `chat.py` line 22 to ask different questions
- The script will show you the matching policy text and a score

## Example query output

When you run `python app/chat.py`, the script:
- converts the query text into an embedding,
- searches `hr_docs` for the closest vectors,
- prints the matching text chunks and similarity scores.

This helps you build a QA-style search experience over HR documents.

## Notes

- The embedding model in `app/embeddings.py` is `text-embedding-3-small`.
- `index_documents.py` currently indexes `documents/leave_policy_detailed.txt`. You can add more .txt files to `documents/` and the script will index them all.
- `qdrant_service.py` initializes the collection using Qdrant's local storage at `qdrant_data/`.

## Quick reference notes

# 1. documents/

You have:

```
documents
  ├── Leave-Policy.pdf
  ├── Remote Working Policy.pdf
  ├── leave_policy_detailed.txt
```

Purpose:

```
Source Documents
These are NOT embeddings.
These are NOT vectors.
These are raw files.
```

---

# 2. extract_pdf.py

Purpose:

```
PDF
↓
Plain Text
```

Example:

Input:

```
Leave-Policy.pdf
```

Output:

```
Employees receive 20 leave days annually.
Unused leave up to 5 days can be carried forward.
```

---

# 3. chunker.py

Purpose:

```
Large Text↓Small Chunks
```

Example:

```
Chunk 1 Employees receive 20 leave days annually.
Chunk 2 Unused leave up to 5 days can be carried forward.
Chunk 3 Remote work allowed 2 days weekly.
```

---

# 4. embeddings.py

Purpose:

Convert each chunk:

```
Unused leave up to 5 dayscan be carried forward.
```

into:

```
[0.12,-0.44,0.91,...1536 dimensions]
```

This vector represents meaning.

---

# 5. qdrant_service.py

Purpose:

Create:

```
Collectionhr_docs
```

Equivalent to:

```
CREATE TABLE hr_docs
```

except it stores vectors.

---

# 6. index_documents.py

This is your most important indexing script.

It performs:

```
For each document
Read
  ↓
Chunk
  ↓
Embedding
  ↓
Store in Qdrant
```

---

Suppose:

```
Leave-Policy.pdf
```

contains:

```
Unused leave up to 5 days can be carried forward.
```

Qdrant stores:

```json
{
  "id": 7,
  "vector": [0.21, -0.55, ...],
  "payload": {
    "text": "Unused leave up to 5 days can be carried forward.",
    "file": "Leave-Policy.pdf"
  }
}
```

This is called:

```
Vector Index
```

---

# 7. qdrant_data/

You already have:

```
qdrant_data
storage.sqlite
collection/hr_docs
meta.json
```

This means:

```
Your vectors are physically stored here.
```

Equivalent to:

```
SQLite database file
but optimized for vectors.
```

---

# 8. inspect_qdrant.py

Purpose:

Look inside the database.

Equivalent SQL:

```
SELECT * FROM hr_docs
```

Qdrant:

```
client.scroll()
```

Output:

```
ID: 7
File:Leave-Policy.pdf
Text:Unused leave up to 5 days can be carried forward.
```

---

# 9. search.py

Purpose:

Semantic Search

User:

```
Can I carry forward leave?
```

↓

Embedding:

```
[0.11,-0.44....]
```

↓

Qdrant:

```
query_points()
```

↓

Result:

```
Unused leave up to 5 days can be carried forward.
```

---

# 10. chat.py

Final RAG

Flow:

```
Question↓Embedding↓Qdrant Search↓Relevant Chunks↓Prompt Builder↓GPT↓Answer
```

## Inspecting Qdrant contents

A small helper script is provided to list the points stored in the `hr_docs` collection for quick debugging and verification.

- File: `app/inspect_qdrant.py`
- What it does: connects to the local Qdrant storage at `qdrant_data/`, scrolls stored points and prints each point's id, source file, and a short preview of the stored text payload.

How to run:

```bash
# activate venv if needed
source .venv/bin/activate

# run the inspector
python3 app/inspect_qdrant.py
```

Expected output: a list of stored points similar to:

```
- id: 0_0 | file: leave_policy_detailed.txt | text preview: 'Employees are eligible for...'
- id: 0_1 | file: leave_policy_detailed.txt | text preview: 'Requests should be submitted...'
```

If you see "No points found" or an error about missing `qdrant_client`, follow the install and setup steps above (create collection and index documents first).

## Next steps

- Add more HR documents to `documents/`.
- Update `index_documents.py` to process all files in the `documents/` folder.
- Implement query handling and answer generation in `app/search.py`.
- Build a web or API interface to make the chatbot easier to use.
