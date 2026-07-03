# Table of Contents

- Introduction
- Features
- Architecture
- Workflow
- Folder Structure
- Installation
- Environment Setup
- SQLite
- Qdrant
- Document Indexing
- Search Pipeline
- Example Questions
- Python Modules
- Troubleshooting
- Future Improvements

                Frontend
                    │
                    ▼
             Command Line
                    │
                    ▼
             Python Application
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   SQLite Database         Qdrant Vector DB
        │                       │
        └───────────┬───────────┘
                    ▼
               OpenAI API
                    ▼
              Final Response

User
 │
 │ Ask Question
 ▼
Chatbot
 │
 │ Intent Classification
 ▼
Entity Extractor
 │
 ▼
Normalizer
 │
 ▼
Search
 │
 ├──────────────┐
 ▼              ▼
SQLite       Qdrant
 │              │
 └──────┬───────┘
        ▼
Answer Generator
        ▼
       User


chat.py
   │
   ▼
chatbot.py
   │
   ├────────► entity_extractor.py
   │
   ├────────► text_normalizer.py
   │
   ├────────► text_to_sql.py
   │
   ├────────► sql_search.py
   │
   ├────────► search.py
   │
   └────────► answer_generator.py



# 🤖 HR AI Chatbot

Welcome to the **HR AI Chatbot** project!

This project demonstrates how to build an intelligent Human Resources (HR) assistant using **Artificial Intelligence (AI)**, **Natural Language Processing (NLP)**, **Vector Search**, and **SQL Database Search**.

Unlike a traditional chatbot that searches only keywords, this chatbot understands the **meaning** of a user's question. It can retrieve answers from company HR policy documents, query employee information stored in a database, or combine both sources to provide a complete response.

For example, the chatbot can answer questions such as:

- Who works in the HR department?
- What is John's leave balance?
- What is the company's leave policy?
- Does the leave policy allow carry forward?
- What is Alice's salary?
- What is John's leave balance and what does the leave policy say?

The project combines multiple AI techniques into a single application:

- **Natural Language Understanding** to understand user questions.
- **Entity Extraction** to identify employee names and departments.
- **Text Normalization** to correct spelling mistakes.
- **Text-to-SQL** to generate SQL queries automatically.
- **SQLite Database** for structured employee information.
- **OpenAI Embeddings** for semantic document understanding.
- **Qdrant Vector Database** for intelligent document search.
- **Hybrid Search** to combine database results and document search into one answer.

---

# 🎯 Project Goal

The main objective of this project is to demonstrate how an AI-powered HR assistant can answer both structured and unstructured questions.

The chatbot can retrieve information from two different data sources:

## 1. Structured Data

Structured data refers to information stored inside a relational database.

Examples:

- Employee Name
- Department
- Salary
- Leave Balance

Example question:

> Who works in IT?

The chatbot searches the SQLite database and returns the employee information.

---

## 2. Unstructured Data

Unstructured data refers to company documents such as:

- Leave Policy
- Remote Work Policy
- HR Guidelines
- Company Handbook
- PDF Documents
- Word Documents

Example question:

> Can employees carry forward leave?

The chatbot searches the HR policy documents stored inside the Vector Database.

---

## 3. Hybrid Search

Some questions require information from both the database and company documents.

Example:

> What is John's leave balance and what does the leave policy say?

The chatbot performs two searches simultaneously:

- Searches SQLite to find John's leave balance.
- Searches Qdrant to find the relevant leave policy.

Finally, it combines both results into a single natural language response.

---

# 🧠 What Makes This Project Different?

Most beginner chatbot projects use only one data source.

For example:

```
User
   │
   ▼
ChatGPT
```

or

```
User
   │
   ▼
SQLite Database
```

or

```
User
   │
   ▼
PDF Search
```

This project combines all of these technologies into one intelligent pipeline.

```
                    User Question
                          │
                          ▼
                Intent Classification
                          │
        ┌─────────────────┴─────────────────┐
        │                                   │
        ▼                                   ▼
   SQL Database Search               Vector Search
        │                                   │
        ▼                                   ▼
 Employee Information             HR Policy Documents
        └─────────────────┬─────────────────┘
                          ▼
                   AI Response Generator
                          │
                          ▼
                    Final Answer
```

---

# 💡 Example Questions

The chatbot understands questions written in natural language.

### Database Questions

```
Who works in HR?

Who works in IT?

What is John's salary?

What is Alice's leave balance?

Who is John?
```

---

### Document Questions

```
What is the leave policy?

Can employees work remotely?

How many casual leaves are allowed?

Explain maternity leave.
```

---

### Hybrid Questions

```
What is John's leave balance and explain the leave policy.

Who works in HR and what are the leave rules?

Show Alice's salary and remote working policy.
```

---

# 🎓 Who Should Use This Project?

This project is designed for developers who want to learn modern AI application development.

It is especially useful for:

- Python Beginners
- AI Engineers
- Machine Learning Engineers
- NLP Engineers
- Backend Developers
- Android Developers interested in AI
- Students learning Retrieval-Augmented Generation (RAG)
- Developers building enterprise chatbots

---

# 📚 What You Will Learn

After completing this project, you will understand:

- How Large Language Models (LLMs) work.
- How OpenAI Embeddings are generated.
- How Vector Databases store document embeddings.
- How semantic search differs from keyword search.
- How SQL can be generated automatically from natural language.
- How entity extraction improves chatbot accuracy.
- How text normalization handles spelling mistakes.
- How structured and unstructured data can be combined.
- How Retrieval-Augmented Generation (RAG) works.
- How to build production-style AI assistants.

---

# 🚀 End Result

By the end of this project, you will have built a complete AI-powered HR assistant capable of:

✅ Understanding natural language.

✅ Searching employee records from SQLite.

✅ Searching HR policies using Vector Search.

✅ Correcting spelling mistakes automatically.

✅ Extracting employee names and departments.

✅ Generating SQL automatically using AI.

✅ Combining multiple data sources into one intelligent answer.

This project demonstrates many of the core techniques used in modern enterprise AI applications.

# ✨ Features

The HR AI Chatbot is designed to answer Human Resource (HR) related questions using both structured employee data and unstructured HR policy documents.

Instead of relying on simple keyword matching, it uses Artificial Intelligence to understand the user's intent and retrieve the most relevant information.

Below are the major features of the project.

---

# 1. 💬 Natural Language Understanding (NLU)

Users can ask questions in normal English without learning SQL or specific commands.

For example:

```
Who works in HR?

What is John's salary?

How many casual leaves are allowed?

Can I carry forward my leave?
```

The chatbot understands the meaning of the question and automatically determines what information the user is requesting.

---

# 2. 🎯 Intent Classification

Before answering a question, the chatbot first identifies **what type of question** the user is asking.

Currently, the chatbot supports multiple intents.

```
                    User Question
                          │
                          ▼
               Intent Classification
                          │
      ┌───────────┬────────────┬──────────────┐
      │           │            │              │
      ▼           ▼            ▼              ▼
  Database     Document      Hybrid      General Chat
```

### Database Intent

Questions that require employee information stored inside SQLite.

Example:

```
Who works in IT?

What is Alice's salary?

Show John's leave balance.
```

---

### Document Intent

Questions that require information from HR policy documents.

Example:

```
Explain the leave policy.

What is the remote work policy?

How many sick leaves are allowed?
```

---

### Hybrid Intent

Questions that require information from both the database and HR documents.

Example:

```
What is John's leave balance and explain the leave policy.

Who works in HR and what are the leave rules?
```

The chatbot automatically combines both results into one answer.

---

# 3. 🔍 Entity Extraction

The chatbot extracts important information from the user's question.

These important pieces of information are called **Entities**.

Example:

Question:

```
What is Jon's leave balance?
```

The chatbot extracts:

```json
{
    "employee_name": "Jon",
    "department": null
}
```

Another example:

Question:

```
Who works in HR?
```

Extracted entities:

```json
{
    "employee_name": null,
    "department": "HR"
}
```

Entity extraction helps the chatbot understand exactly what the user is referring to before generating SQL or searching documents.

---

# 4. ✏️ Text Normalization

People often make spelling mistakes while typing.

The chatbot automatically corrects common mistakes before processing the question.

Example:

| User Input | Corrected |
|------------|-----------|
| jon | John |
| alce | Alice |
| hr | HR |
| it | IT |
| sallary | salary |
| leav | leave |

This significantly improves search accuracy.

---

# 5. 🤖 AI Powered SQL Generation

One of the most interesting features of this project is **Natural Language to SQL**.

Instead of writing SQL manually, users ask questions in English.

Example:

User asks:

```
Who works in IT?
```

The AI automatically generates:

```sql
SELECT *
FROM employees
WHERE LOWER(department)=LOWER('IT');
```

Another example:

```
What is John's salary?
```

Generated SQL:

```sql
SELECT salary
FROM employees
WHERE LOWER(name)=LOWER('John');
```

This allows non-technical users to query databases without knowing SQL.

---

# 6. 🗄 SQLite Database Search

Employee information is stored inside a local SQLite database.

Example employee data:

| Name | Department | Salary | Leave Balance |
|------|------------|---------|----------------|
| John | IT | 50000 | 20 |
| Alice | HR | 45000 | 15 |

Whenever a user asks about employee information, the chatbot searches this database.

---

# 7. 📄 Document Search

The chatbot can search HR documents such as:

- Leave Policy
- Remote Work Policy
- Employee Handbook
- Company Guidelines

Supported document formats include:

- TXT
- PDF
- DOCX
- XLSX

Instead of searching for exact words, the chatbot searches based on the **meaning** of the text.

This technique is called **Semantic Search**.

---

# 8. 🧠 OpenAI Embeddings

Computers cannot understand plain text directly.

The embedding model converts every document into a mathematical representation called a **Vector**.

Example:

```
Employees receive 20 annual leaves.
```

becomes

```
[0.14, -0.32, 0.76, ...]
```

Documents with similar meaning produce similar vectors.

This allows the chatbot to answer questions even when the wording is different.

Example:

Document:

```
Employees receive 20 annual leaves.
```

User asks:

```
How many vacation days do employees get?
```

Although the words are different, the chatbot understands they have the same meaning.

---

# 9. 🚀 Vector Search using Qdrant

All document embeddings are stored inside a Vector Database called **Qdrant**.

Instead of searching text directly, Qdrant searches vectors.

The process looks like this:

```
Question
     │
     ▼
Embedding
     │
     ▼
Qdrant Vector Search
     │
     ▼
Most Similar Documents
```

This makes searching much faster and more accurate.

---

# 10. 🔀 Hybrid Search

Sometimes the answer requires both the database and HR documents.

Example:

```
What is John's leave balance and explain the leave policy.
```

The chatbot performs two searches simultaneously.

```
                  User Question
                        │
                        ▼
               Intent Classification
                        │
         ┌──────────────┴──────────────┐
         │                             │
         ▼                             ▼
 SQLite Database                 Vector Search
         │                             │
         ▼                             ▼
Employee Data                 HR Policy Document
         └──────────────┬──────────────┘
                        ▼
               AI Response Generator
                        │
                        ▼
                  Final Answer
```

This provides much richer responses than using only one data source.

---

# 11. 📚 Retrieval-Augmented Generation (RAG)

The chatbot follows the RAG architecture.

RAG stands for **Retrieval-Augmented Generation**.

Instead of asking the AI to answer from memory, the chatbot first retrieves relevant information and then generates the answer.

The process is:

```
User Question
       │
       ▼
Retrieve Relevant Data
       │
       ▼
Provide Context to AI
       │
       ▼
Generate Accurate Answer
```

This approach reduces hallucinations and improves answer accuracy.

---

# 12. 📈 Scalable Architecture

The project is designed in a modular way.

Each Python file has a specific responsibility.

```
User Question
      │
      ▼
Intent Classification
      │
      ▼
Entity Extraction
      │
      ▼
Text Normalization
      │
      ▼
SQL Generation / Vector Search
      │
      ▼
Response Generation
```

Because each module performs only one task, the project is easy to understand, maintain, and extend.

---

# 🌟 Summary

This project demonstrates many modern AI techniques used in production applications:

- ✅ Natural Language Understanding
- ✅ Intent Classification
- ✅ Entity Extraction
- ✅ Text Normalization
- ✅ Automatic SQL Generation
- ✅ SQLite Database Search
- ✅ OpenAI Embeddings
- ✅ Vector Search using Qdrant
- ✅ Semantic Search
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Hybrid Search
- ✅ AI Response Generation

Together, these features enable the HR AI Chatbot to answer both structured and unstructured HR questions accurately and efficiently.

# 🛠 Technologies Used

This project combines several modern technologies to build an intelligent AI-powered HR chatbot.

Each technology has a specific responsibility. Together, they create a complete end-to-end AI application capable of understanding natural language, searching databases, retrieving documents, and generating intelligent responses.

---

# Technology Stack Overview

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| OpenAI GPT | Natural language understanding and SQL generation |
| OpenAI Embeddings | Convert text into vector representations |
| SQLite | Store structured employee information |
| Qdrant | Store document embeddings for semantic search |
| RapidFuzz | Correct spelling mistakes and fuzzy matching |
| python-dotenv | Load environment variables securely |
| python-docx | Read Microsoft Word documents |
| PyPDF2 | Extract text from PDF files |
| openpyxl | Read Microsoft Excel files |
| JSON | Structured communication between modules |

---

# 1. 🐍 Python

Python is the primary programming language used throughout this project.

It is widely used in Artificial Intelligence, Machine Learning, Natural Language Processing, Data Science, and Backend Development because of its simplicity and rich ecosystem of libraries.

Python acts as the glue that connects every component of this chatbot.

It is responsible for:

- Reading documents
- Calling OpenAI APIs
- Generating embeddings
- Querying SQLite
- Communicating with Qdrant
- Processing user questions
- Generating chatbot responses

---

Example:

```python
question = input("Ask a question: ")
answer = chatbot(question)
print(answer)
```

---

# Why Python?

✅ Easy to learn

✅ Huge AI ecosystem

✅ Excellent community support

✅ Fast development

✅ Cross-platform

---

# 2. 🤖 OpenAI GPT

OpenAI GPT is the Large Language Model (LLM) used by this project.

Instead of writing complicated rules manually, GPT understands human language and performs intelligent tasks.

In this project GPT is responsible for:

- Intent Classification
- Entity Extraction
- SQL Generation
- Response Generation
- Hybrid Answer Generation

---

Example

User asks:

```
Who works in IT?
```

GPT understands that:

```
Intent

↓

Database Question

↓

Department = IT
```

Then GPT generates SQL automatically.

---

Another example:

```
Explain the leave policy.
```

GPT understands:

```
Intent

↓

Document Search
```

No SQL is required.

---

# Why GPT?

GPT understands natural language much better than traditional rule-based chatbots.

It can understand:

- Grammar
- Context
- Intent
- Misspellings
- Human language

instead of relying on exact keywords.

---

# 3. 🧠 OpenAI Embeddings

Large Language Models understand text.

Vector Databases understand numbers.

Therefore we need a way to convert text into numbers.

This process is called **Embedding Generation**.

Example:

```
Employee receives 20 annual leaves.
```

becomes

```
[0.12,
-0.55,
0.89,
...
1536 numbers]
```

These numbers represent the meaning of the sentence.

Two sentences with similar meanings will produce similar vectors.

Example:

```
Employees receive 20 annual leaves.
```

and

```
Employees get 20 vacation days.
```

will generate vectors that are very close to each other.

---

Why is this important?

Traditional keyword search would fail because:

```
annual leave

≠

vacation days
```

Semantic search succeeds because their meanings are similar.

---

# 4. 🗄 SQLite

SQLite is a lightweight relational database.

Unlike MySQL or PostgreSQL, SQLite stores everything inside a single file.

Example:

```
database/

    hr.db
```

This makes the project extremely easy to distribute.

No database server is required.

---

Employee Table

```
employees
```

contains

```
id

name

department

salary

leave_balance
```

Example

| ID | Name | Department | Salary | Leave Balance |
|----|------|------------|---------|---------------|
|1|John|IT|50000|20|
|2|Alice|HR|45000|15|

---

Whenever the user asks:

```
What is John's salary?
```

SQLite returns

```
50000
```

---

# Why SQLite?

✅ Simple

✅ No installation

✅ Fast

✅ Single database file

✅ Perfect for beginner projects

---

# 5. 🚀 Qdrant

Qdrant is a Vector Database.

Unlike SQLite, it does not store tables of rows.

Instead it stores:

```
Vector

+

Metadata

+

Original Text
```

Example

```
ID : 17

Vector :

[0.21,
0.55,
...
1536 values]

Payload

Leave Policy

Original Text
```

Qdrant allows us to search documents based on meaning instead of keywords.

---

Traditional Database

```
Name

Salary

Department
```

Vector Database

```
Meaning

Similarity

Embeddings
```

---

# Why Qdrant?

Because it is specifically designed for AI applications.

Benefits

✅ Fast vector search

✅ High performance

✅ Local storage

✅ Easy integration

✅ Open Source

---

# 6. 🔍 RapidFuzz

Users often make typing mistakes.

Example

```
jon
```

instead of

```
John
```

RapidFuzz compares strings and finds the closest match.

Example

```
jon

↓

John
```

Another example

```
hr

↓

HR
```

or

```
enginering

↓

Engineering
```

RapidFuzz significantly improves chatbot accuracy.

---

Why RapidFuzz?

It is:

- Very fast
- Lightweight
- Accurate
- Easy to integrate

---

# 7. 📄 PyPDF2

Many HR policies are distributed as PDF documents.

PyPDF2 extracts text from PDF files.

Example

```
Leave Policy.pdf

↓

Extract Text

↓

String
```

Once extracted, the text is sent to the chunking and embedding pipeline.

---

# 8. 📘 python-docx

Some HR policies are stored as Microsoft Word documents.

python-docx reads those documents.

Example

```
Policy.docx

↓

Extract Text

↓

Index
```

---

# 9. 📊 openpyxl

Sometimes HR data exists inside Excel spreadsheets.

openpyxl allows the chatbot to read:

```
.xlsx

.xls
```

files.

This makes it possible to index HR information stored in spreadsheets.

---

# 10. 🔐 python-dotenv

The project uses an OpenAI API Key.

Instead of writing the key directly inside Python code, it is stored inside

```
.env
```

Example

```
OPENAI_API_KEY=your_api_key_here
```

python-dotenv automatically loads these values when the application starts.

This keeps sensitive information secure.

---

# How Everything Works Together

The following diagram shows how all technologies interact.

```
                   User Question
                         │
                         ▼
                     Python
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
 RapidFuzz         OpenAI GPT        OpenAI Embeddings
      │                  │                  │
      │                  │                  ▼
      │                  │             Vector Search
      │                  │                  │
      ▼                  ▼                  ▼
 Entity Extraction   SQL Generation      Qdrant
      │                  │                  │
      ▼                  ▼                  ▼
                SQLite Database      HR Documents
                      │                  │
                      └──────────┬───────┘
                                 ▼
                         AI Response
                                 │
                                 ▼
                           Final Answer
```

---

# Summary

This project combines modern AI technologies into one intelligent system.

| Technology | Responsibility |
|------------|----------------|
| Python | Main application logic |
| OpenAI GPT | Understands user questions |
| OpenAI Embeddings | Converts text into vectors |
| SQLite | Stores employee records |
| Qdrant | Stores document embeddings |
| RapidFuzz | Corrects spelling mistakes |
| PyPDF2 | Reads PDF documents |
| python-docx | Reads Word documents |
| openpyxl | Reads Excel documents |
| python-dotenv | Loads environment variables |

Each technology performs a specific task, and together they create a powerful AI-powered HR chatbot capable of answering both structured and unstructured HR questions.

# 🏗️ Project Architecture

Before exploring the source code, it is important to understand how all the components of this project work together.

This HR AI Chatbot is **not just a chatbot**. It combines several Artificial Intelligence techniques with traditional database technologies to answer user questions intelligently.

The project follows a modular architecture, where each module is responsible for a single task. This makes the code easier to understand, maintain, and extend.

---

# High-Level Architecture

The following diagram illustrates the complete architecture of the application.

```
                               +--------------------+
                               |      User          |
                               +---------+----------+
                                         |
                                         |
                                 Ask a Question
                                         |
                                         ▼
                         +-------------------------------+
                         |      Intent Classification     |
                         +-------------------------------+
                                         |
                +------------------------+------------------------+
                |                         |                        |
                |                         |                        |
                ▼                         ▼                        ▼
        Database Intent          Document Intent          Hybrid Intent
                |                         |                        |
                |                         |                        |
                ▼                         ▼                        ▼
         SQLite Search             Vector Search          Both Searches
                |                         |                        |
                |                         |                        |
                ▼                         ▼                        ▼
         Employee Data           HR Policy Documents      Combine Results
                \                         |                     /
                 \                        |                    /
                  \_______________________|___________________/
                                          |
                                          ▼
                               AI Response Generator
                                          |
                                          ▼
                                  Final Answer
```

---

# Why Do We Need This Architecture?

A normal chatbot usually works in one of the following ways:

```
User
   │
   ▼
ChatGPT
```

or

```
User
   │
   ▼
Database
```

or

```
User
   │
   ▼
PDF Search
```

These approaches have limitations.

For example:

### ChatGPT Only

Pros

- Understands language very well.

Cons

- Does not know your company's HR policies.
- Does not know employee information.
- May hallucinate answers.

---

### Database Only

Pros

- Provides accurate employee information.

Cons

- Cannot answer questions from documents.
- Cannot explain HR policies.

---

### Document Search Only

Pros

- Can answer HR policy questions.

Cons

- Cannot retrieve employee salary or leave balance.

---

Our chatbot combines all three approaches.

This allows it to answer almost every HR-related question.

---

# Overall Request Processing Pipeline

Every user question follows the same processing pipeline.

```
                User Question
                      │
                      ▼
          Text Normalization
                      │
                      ▼
           Intent Classification
                      │
                      ▼
             Entity Extraction
                      │
                      ▼
          Entity Normalization
                      │
                      ▼
      +---------------+---------------+
      |                               |
      ▼                               ▼
 Database Search               Document Search
      |                               |
      ▼                               ▼
 Employee Data               Relevant Documents
      +---------------+---------------+
                      │
                      ▼
           AI Response Generator
                      │
                      ▼
                Final Response
```

Every step in this pipeline performs one specific task.

---

# Step-by-Step Architecture

Let's understand each step in detail.

---

## Step 1 – User Asks a Question

Everything starts with a natural language question.

Example:

```
Who works in HR?
```

or

```
What is John's leave balance?
```

or

```
Explain the leave policy.
```

The user does not need to know SQL.

The user does not need to know database tables.

The user simply asks questions naturally.

---

## Step 2 – Text Normalization

Users frequently make typing mistakes.

Examples:

```
jon

↓

John
```

```
leav

↓

leave
```

```
hr

↓

HR
```

The chatbot automatically cleans the question before processing it.

This greatly improves accuracy.

---

## Step 3 – Intent Classification

Now the chatbot decides what kind of question it has received.

Possible intents are:

```
DATABASE
```

```
DOCUMENT
```

```
HYBRID
```

Example:

```
Who works in HR?

↓

DATABASE
```

---

```
Explain leave policy.

↓

DOCUMENT
```

---

```
What is John's leave balance and explain leave policy?

↓

HYBRID
```

The intent determines which search pipeline should be executed.

---

## Step 4 – Entity Extraction

After determining the intent, the chatbot extracts important information.

Example:

Question

```
What is Jon's leave balance?
```

Extracted entities

```json
{
    "employee_name":"Jon",
    "department":null
}
```

Another example

```
Who works in HR?
```

becomes

```json
{
    "employee_name":null,
    "department":"HR"
}
```

These extracted entities are later validated using RapidFuzz.

---

## Step 5 – Entity Normalization

The extracted entities may contain spelling mistakes.

Example

```
Jon

↓

John
```

```
in

↓

IT
```

```
enginering

↓

Engineering
```

Instead of correcting the whole sentence, only the extracted entities are corrected.

This avoids accidental replacements.

---

# Database Pipeline

Questions related to employee information are processed using SQLite.

Example:

```
What is Alice's salary?
```

Pipeline

```
Question
    │
    ▼
Entity Extraction
    │
    ▼
Generate SQL
    │
    ▼
SQLite Database
    │
    ▼
Employee Record
    │
    ▼
AI Response
```

Generated SQL

```sql
SELECT salary
FROM employees
WHERE LOWER(name)=LOWER('Alice');
```

---

# Vector Search Pipeline

Policy questions follow a completely different route.

Example

```
Can employees carry forward leave?
```

Pipeline

```
Question
      │
      ▼
Embedding
      │
      ▼
Vector Search
      │
      ▼
Relevant Chunks
      │
      ▼
GPT
      │
      ▼
Answer
```

Instead of searching keywords, the chatbot searches document meaning.

---

# Hybrid Search Pipeline

Some questions require both pipelines.

Example

```
What is John's leave balance and explain leave policy.
```

Pipeline

```
                  User Question
                        │
                        ▼
                 Intent = HYBRID
                        │
        +---------------+---------------+
        |                               |
        ▼                               ▼
SQLite Search                  Vector Search
        |                               |
        ▼                               ▼
Employee Data                 Policy Context
        +---------------+---------------+
                        │
                        ▼
               GPT Response Generator
                        │
                        ▼
                  Final Response
```

The chatbot merges both results into one answer.

---

# Internal Component Architecture

Each Python module has one responsibility.

```
                   app/
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 chat.py       chatbot.py      main.py
      │
      ▼
query_preprocessor.py
      │
      ▼
entity_extractor.py
      │
      ▼
text_to_sql.py
      │
      ▼
sql_search.py
      │
      ▼
SQLite Database
```

For document search

```
chat.py
    │
    ▼
embeddings.py
    │
    ▼
Qdrant
    │
    ▼
Retrieved Chunks
    │
    ▼
Prompt Builder
    │
    ▼
GPT
```

---

# Why Modular Architecture?

Every module performs one job.

Instead of writing everything inside one Python file, responsibilities are separated.

Benefits

✅ Easier to understand

✅ Easier debugging

✅ Better code reuse

✅ Easier testing

✅ Easier maintenance

✅ Easier to add new features

For example, if you want to support **PostgreSQL** instead of SQLite, only the database layer needs to change.

If you want to support another vector database instead of Qdrant, only the vector search layer changes.

The remaining application stays exactly the same.

---

# Architecture Summary

The HR AI Chatbot combines multiple technologies into one intelligent system.

```
User
 │
 ▼
Natural Language Question
 │
 ▼
Text Normalization
 │
 ▼
Intent Classification
 │
 ▼
Entity Extraction
 │
 ▼
Entity Normalization
 │
 ▼
─────────────────────────────────────
│                                   │
│ Database Search                   │
│ SQLite                            │
│                                   │
├───────────────────────────────────┤
│                                   │
│ Document Search                   │
│ OpenAI Embeddings                 │
│ Qdrant Vector Database            │
│                                   │
─────────────────────────────────────
 │
 ▼
Combine Results
 │
 ▼
OpenAI GPT
 │
 ▼
Final Answer
```

This architecture follows modern AI application design principles and demonstrates how structured databases and semantic document search can work together to build an intelligent enterprise chatbot.

# 🔄 Project Workflow

Understanding the project workflow is one of the most important parts of this project.

Many beginners can run a project by following commands, but they often don't understand **what is happening behind the scenes**.

This section explains the complete lifecycle of the HR AI Chatbot—from creating the project to receiving an AI-generated answer.

---

# Complete Workflow

The following diagram shows the complete workflow of the project.

```
                    Create Project
                           │
                           ▼
              Create Virtual Environment
                           │
                           ▼
                 Install Dependencies
                           │
                           ▼
                 Configure Environment
                       (.env file)
                           │
                           ▼
               Create SQLite Database
                           │
                           ▼
              Create Qdrant Collection
                           │
                           ▼
                 Read HR Documents
                           │
                           ▼
                 Extract Document Text
                           │
                           ▼
                 Split into Chunks
                           │
                           ▼
               Generate Embeddings
                           │
                           ▼
             Store Vectors in Qdrant
                           │
                           ▼
                  Start the Chatbot
                           │
                           ▼
                  User Asks Question
                           │
                           ▼
               Intent Classification
                           │
                           ▼
                 Entity Extraction
                           │
                           ▼
              Database / Vector Search
                           │
                           ▼
                AI Generates Answer
                           │
                           ▼
                  Display Final Answer
```

Every step in this workflow has a specific purpose.

Let's understand each one.

---

# Step 1 – Create the Project

The first step is creating the project folder.

Example

```bash
mkdir hr_chatbot
cd hr_chatbot
```

At this stage, nothing has been installed.

Your folder is simply an empty workspace where all project files will be stored.

Example structure:

```
hr_chatbot/
```

Think of this as building the foundation of a house before constructing the rooms.

---

# Step 2 – Create a Virtual Environment

A Virtual Environment creates an isolated Python environment for your project.

Without it, every Python package would be installed globally on your computer.

This can create version conflicts between projects.

Create it using:

```bash
python3 -m venv .venv
```

Activate it:

Mac/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

After activation, your terminal should look similar to:

```
(.venv)
```

This indicates that Python packages will now be installed only for this project.

---

# Step 3 – Install Required Packages

Now install all required Python libraries.

```bash
pip install -r requirements.txt
```

or

```bash
pip install openai qdrant-client python-dotenv rapidfuzz python-docx PyPDF2 openpyxl
```

These libraries provide different capabilities.

| Package | Purpose |
|----------|---------|
| openai | Communicates with OpenAI models |
| qdrant-client | Stores and searches vectors |
| rapidfuzz | Corrects spelling mistakes |
| python-dotenv | Reads API keys from `.env` |
| python-docx | Reads Word documents |
| PyPDF2 | Reads PDF files |
| openpyxl | Reads Excel files |

---

# Step 4 – Configure the Environment

The project needs an OpenAI API Key.

Instead of writing it inside Python code, it is stored inside a `.env` file.

Example:

```
OPENAI_API_KEY=your_api_key_here
```

Your application loads it automatically when it starts.

Advantages:

- Keeps secrets secure
- Prevents accidental sharing
- Easy to change later

---

# Step 5 – Create the SQLite Database

The chatbot answers employee-related questions using SQLite.

Run:

```bash
python3 app/database_setup.py
```

This script creates:

```
database/
    hr.db
```

Inside this database, an `employees` table is created.

```
employees
```

Example:

| ID | Name | Department | Salary | Leave Balance |
|----|------|------------|---------|---------------|
|1|John|IT|50000|20|
|2|Alice|HR|45000|15|

Now the chatbot has structured employee information.

---

# Step 6 – Create the Qdrant Collection

Before storing document embeddings, Qdrant needs a collection.

Think of a collection as a table in a relational database.

Run:

```bash
python3 app/qdrant_service.py
```

Internally it creates something similar to:

```
Collection

↓

hr_docs
```

The collection will later store vectors generated from HR documents.

---

# Step 7 – Read HR Documents

Now the chatbot reads company HR documents.

Supported formats include:

```
TXT

PDF

DOCX

DOC

XLSX

XLS
```

Example

```
Leave-Policy.pdf

Remote-Working.pdf

Employee-Handbook.docx
```

These are still normal files.

The AI cannot search them efficiently yet.

---

# Step 8 – Extract Text

The documents are converted into plain text.

Example

```
Leave-Policy.pdf

↓

Employees receive 20 annual leave days...
```

This process is handled by:

```
extract_pdf.py
```

Now every document has become plain text.

---

# Step 9 – Chunk the Documents

Large Language Models cannot efficiently process huge documents.

Therefore each document is divided into smaller pieces.

Example

Original Document

```
100 Pages
```

↓

```
Chunk 1

Chunk 2

Chunk 3

...

Chunk N
```

Example chunk:

```
Employees receive 20 paid leave days every year.
```

Smaller chunks improve search accuracy.

---

# Step 10 – Generate Embeddings

Each chunk is converted into a mathematical vector.

Example

```
Employees receive 20 paid leave days.
```

↓

```
[0.12,
-0.45,
0.81,
...
1536 numbers]
```

These vectors represent the meaning of the text.

Documents discussing similar topics produce similar vectors.

---

# Step 11 – Store Embeddings in Qdrant

Each vector is stored together with its original text.

Example

```
{
    id:12,

    vector:[0.11,-0.55,...],

    payload:{
        file:"Leave-Policy.pdf",

        text:"Employees receive 20 paid leave days."
    }
}
```

Now the documents become searchable.

---

# Step 12 – Start the Chatbot

Everything is now ready.

Run:

```bash
python3 app/chatbot.py
```

or

```bash
python3 app/chat.py
```

The chatbot waits for user questions.

Example

```
Ask a question:
```

---

# Step 13 – User Asks a Question

Example

```
Who works in HR?
```

or

```
What is John's leave balance?
```

or

```
Explain the leave policy.
```

---

# Step 14 – Intent Classification

The chatbot first determines what the user wants.

Possible intents:

```
DATABASE

DOCUMENT

HYBRID
```

Example

```
Who works in HR?

↓

DATABASE
```

---

```
Explain leave policy

↓

DOCUMENT
```

---

```
John leave balance and leave policy

↓

HYBRID
```

---

# Step 15 – Entity Extraction

The chatbot identifies important information.

Example

```
Who works in HR?
```

↓

```json
{
    "employee_name":null,

    "department":"HR"
}
```

---

```
John leave balance
```

↓

```json
{
    "employee_name":"John",

    "department":null
}
```

---

# Step 16 – Search

Depending on the intent:

Database

↓

SQLite

or

Document

↓

Qdrant

or

Both

↓

Hybrid Search

---

# Step 17 – AI Generates the Answer

The retrieved information is sent to GPT.

GPT combines:

- User Question
- Database Results
- Document Context

into a natural language answer.

Example

```
John currently has a leave balance of 20 days.

According to the company leave policy, employees receive 20 paid annual leave days, with up to 5 unused days eligible for carry forward.
```

---

# Complete End-to-End Workflow

```
                    User
                      │
                      ▼
              Ask Question
                      │
                      ▼
          Intent Classification
                      │
                      ▼
            Entity Extraction
                      │
                      ▼
         Text Normalization
                      │
                      ▼
      +---------------+---------------+
      |                               |
      ▼                               ▼
SQLite Database                 Qdrant Search
      |                               |
      ▼                               ▼
Employee Data                Relevant Chunks
      +---------------+---------------+
                      │
                      ▼
                 OpenAI GPT
                      │
                      ▼
                Final Response
```

---

# Workflow Summary

The HR AI Chatbot follows a structured pipeline where each module performs a specific task.

1. Create the project.
2. Create a virtual environment.
3. Install all required dependencies.
4. Configure the OpenAI API key.
5. Create the SQLite database.
6. Create the Qdrant collection.
7. Read HR documents.
8. Extract text from documents.
9. Split text into smaller chunks.
10. Generate embeddings.
11. Store vectors in Qdrant.
12. Start the chatbot.
13. Accept a user question.
14. Classify the user's intent.
15. Extract and normalize entities.
16. Search the SQLite database, Qdrant, or both.
17. Use GPT to generate a natural language response.
18. Display the final answer to the user.

By understanding this workflow, you will be able to understand how every file in the project contributes to building an intelligent HR AI assistant.

# 📁 Project Structure

A well-organized project structure makes the application easier to understand, maintain, and extend.

This project follows a modular architecture where each Python file is responsible for a single task.

```
HR_CHATBOT/
│
├── .cache/                     # Python cache (auto-generated)
├── .venv/                      # Python virtual environment
│
├── app/                        # Main application source code
│   ├── answer_generator.py
│   ├── chat.py
│   ├── chatbot.py
│   ├── chunker.py
│   ├── database_setup.py
│   ├── embeddings.py
│   ├── entity_extractor.py
│   ├── extract_pdf.py
│   ├── hybrid_search.py
│   ├── index_documents.py
│   ├── insert_data.py
│   ├── inspect_qdrant.py
│   ├── main.py
│   ├── prompt_builder.py
│   ├── qdrant_service.py
│   ├── query_preprocessor.py
│   ├── search.py
│   ├── sql_chat.py
│   ├── sql_search.py
│   ├── text_normalizer.py
│   └── text_to_sql.py
│
├── database/
│   └── hr.db                   # SQLite database
│
├── documents/                  # HR policy documents
│
├── qdrant_data/                # Local Qdrant vector storage
│
├── .env                        # Environment variables
├── requirements.txt
├── README.md
└── NEW_README.md
```

---

# 📂 Root Directory

The root directory contains everything required to build and run the project.

```
HR_CHATBOT/
```

Think of this as the main workspace where source code, database, documents, and configuration files are stored.

---

# 📁 app/

```
app/
```

This is the heart of the project.

Almost all application logic is implemented inside this folder.

Every Python file has a specific responsibility.

Instead of writing thousands of lines inside one file, the project is divided into small reusable modules.

Benefits include:

- Easier maintenance
- Better readability
- Easier debugging
- Easier testing
- Easier feature additions

---

# 📁 database/

```
database/
```

This folder stores the SQLite database.

Example

```
database/

    hr.db
```

The database contains structured employee information such as:

- Employee Name
- Department
- Salary
- Leave Balance

Whenever the chatbot receives a database-related question, it queries this database.

Example:

```
Who works in HR?
```

↓

SQLite Database

↓

Employee Record

---

# 📁 documents/

```
documents/
```

This folder stores all company HR documents.

Examples

```
Leave Policy.pdf

Remote Working Policy.docx

Employee Handbook.pdf

Holiday Calendar.xlsx
```

These files are indexed into the Vector Database.

The chatbot never searches these files directly.

Instead it searches their vector representations stored inside Qdrant.

---

# 📁 qdrant_data/

```
qdrant_data/
```

This folder contains the local Qdrant Vector Database.

When document embeddings are generated, they are stored here.

Think of it as the database for semantic search.

Unlike SQLite, it stores vectors instead of tables.

---

# 📄 .env

```
.env
```

Stores sensitive configuration values.

Example

```
OPENAI_API_KEY=your_api_key_here
```

Advantages

- Keeps API keys secure
- Prevents accidental commits
- Easy configuration

Never commit this file to GitHub.

---

# 📄 requirements.txt

Lists every Python package required to run the project.

Example

```
openai

qdrant-client

rapidfuzz

python-docx

PyPDF2

openpyxl
```

Install everything using

```bash
pip install -r requirements.txt
```

---

# 📁 .venv/

Python Virtual Environment.

Contains all installed Python packages for this project only.

This folder should not be committed to GitHub.

---

# 📁 .cache/

Automatically generated by Python.

Used to improve execution performance.

Can be safely ignored.

---

# 🧩 Source Code Modules

The following sections explain every Python file in detail.

Each file has a single responsibility, making the application modular and easy to understand.

# 📄 chatbot.py

## Purpose

This file contains the main chatbot workflow.

It coordinates all modules required to answer a question.

Think of this file as the project's **brain**.

It does not perform every task itself.

Instead, it delegates work to specialized modules.

---

## Responsibilities

- Receive the user's question
- Normalize the text
- Classify intent
- Extract entities
- Execute SQL search or vector search
- Generate the final response

---

## Workflow

```
User Question
      │
      ▼
Text Normalization
      │
      ▼
Intent Classification
      │
      ▼
Entity Extraction
      │
      ▼
Database Search
or
Vector Search
      │
      ▼
Answer Generator
      │
      ▼
Return Response
```

# 📄 prompt_builder.py

## Purpose

Large Language Models (LLMs) generate responses based on prompts.

Instead of writing prompts throughout the project, all prompts are centralized inside `prompt_builder.py`.

This makes the project easier to maintain.

If you want to change how the AI behaves, you only need to modify this file.

---

## Why is it Needed?

Without this file:

```
chat.py

↓

Huge Prompt
```

```
text_to_sql.py

↓

Another Huge Prompt
```

```
entity_extractor.py

↓

Another Prompt
```

The same prompt logic would be duplicated throughout the project.

Instead, all prompts are stored in one place.

---

## Responsibilities

Depending on your implementation, this file stores prompts for:

- Intent Classification
- Entity Extraction
- SQL Generation
- Answer Generation
- Hybrid Search
- Document Search
- Database Search

---

## Example

```
User Question

↓

Prompt Builder

↓

System Prompt

↓

GPT

↓

Response
```

---

## Benefits

- Centralized prompt management
- Easier prompt tuning
- Less duplicated code
- Cleaner architecture
- Easier maintenance

Whenever you want to improve the AI's behaviour, this is usually the first file you modify.

# 📄 query_preprocessor.py

## Purpose

`query_preprocessor.py` is responsible for preparing the user's question before it is processed by the chatbot.

Users often type incomplete sentences, inconsistent capitalization, or unnecessary punctuation. This module cleans the input so that the remaining components of the system receive a consistent and predictable question.

Think of this file as the **first processing stage** after the user enters a question.

---

## Why is it Needed?

Humans write questions in many different ways.

Example:

```
Who Work In HR
```

```
who work in hr???
```

```
WHO WORK IN HR
```

```
who work in Hr
```

Although these questions mean exactly the same thing, computers see them as different strings.

The Query Preprocessor standardizes the input before further processing.

---

## Responsibilities

Depending on your implementation, this module may perform tasks such as:

- Removing unnecessary spaces
- Removing extra punctuation
- Converting inconsistent formatting
- Preparing the question for normalization
- Passing the cleaned text to the next stage

---

## Workflow

```
User Question
       │
       ▼
Query Preprocessor
       │
       ▼
Clean Question
       │
       ▼
Text Normalizer
```

---

## Example

User input

```
Who   Work    In HR???
```

After preprocessing

```
Who Work In HR
```

The cleaned question is now ready for normalization and entity extraction.

---

## Benefits

- Produces consistent user input
- Reduces unnecessary processing
- Improves downstream accuracy
- Makes later modules simpler

# 📄 text_normalizer.py

## Purpose

The Text Normalizer corrects spelling mistakes and standardizes important words before generating SQL or searching documents.

Users rarely type perfect questions.

For example:

```
jon
```

instead of

```
John
```

or

```
leav
```

instead of

```
leave
```

The Text Normalizer automatically fixes these mistakes.

---

## Why is it Needed?

Suppose the database contains

```
John
```

The user asks

```
What is jon leave?
```

Without normalization

```
jon

≠

John
```

The database search fails.

After normalization

```
jon

↓

John
```

The search succeeds.

---

## Responsibilities

The Text Normalizer performs several important tasks.

### 1. Correct Employee Names

Example

```
jon

↓

John
```

```
alce

↓

Alice
```

The corrected names are later used during SQL generation.

---

### 2. Correct Department Names

Example

```
hr

↓

HR
```

```
it

↓

IT
```

```
enginering

↓

Engineering
```

---

### 3. Correct HR Keywords

The chatbot also corrects common HR-related spelling mistakes.

Example

```
leav

↓

leave
```

```
sallary

↓

salary
```

```
balnce

↓

balance
```

---

## How Does It Work?

The module first extracts entities.

Then it compares them against values stored inside the database.

Example

```
jon

↓

RapidFuzz

↓

John
```

Only the extracted entity is replaced.

The remaining sentence remains unchanged.

---

## Workflow

```
Question
      │
      ▼
Extract Entities
      │
      ▼
RapidFuzz Matching
      │
      ▼
Replace Entity
      │
      ▼
Normalized Question
```

---

## Example

Original Question

```
what is jon leav?
```

↓

Entity Extraction

```
employee_name = jon
```

↓

RapidFuzz

```
John
```

↓

Keyword Normalization

```
leave
```

↓

Final Question

```
What is John leave?
```

---

## Benefits

- Corrects typing mistakes
- Improves SQL generation
- Improves vector search
- Avoids database search failures
- Makes the chatbot more user-friendly

# 📄 entity_extractor.py

## Purpose

The Entity Extractor identifies important pieces of information from the user's question.

These pieces of information are called **entities**.

Instead of processing the entire sentence, the chatbot first identifies the most important values.

Examples include:

- Employee Name
- Department
- Salary
- Leave
- Date (future enhancement)

---

## What is an Entity?

An entity is a meaningful value inside a sentence.

Question

```
What is John's salary?
```

Entities

```json
{
    "employee_name":"John",
    "department":null
}
```

---

Question

```
Who works in HR?
```

Entities

```json
{
    "employee_name":null,
    "department":"HR"
}
```

---

Question

```
Who works in IT?
```

Entities

```json
{
    "employee_name":null,
    "department":"IT"
}
```

---

## Why Extract Entities?

Imagine searching every word using RapidFuzz.

Question

```
Who works in HR?
```

Words

```
Who

works

in

HR
```

RapidFuzz might incorrectly match

```
works

↓

John
```

or

```
in

↓

IT
```

This creates incorrect results.

Instead, GPT first determines which words actually represent entities.

Only those entities are normalized.

This significantly improves accuracy.

---

## Responsibilities

The Entity Extractor is responsible for:

- Identifying employee names
- Identifying department names
- Returning structured JSON
- Preserving the original user text
- Passing entities to the Text Normalizer

---

## Example

User Question

```
what is jon leave?
```

↓

Entity Extractor

```json
{
    "employee_name":"jon",
    "department":null
}
```

↓

Text Normalizer

```
John
```

↓

Updated Question

```
What is John leave?
```

---

## Why Use GPT Instead of Regular Expressions?

Traditional methods require writing many manual rules.

Example

```
John salary

salary of John

John's salary

salary John

show salary for John
```

Each sentence has a different structure.

GPT understands all of these naturally without requiring complex pattern matching.

---

## Workflow

```
User Question
        │
        ▼
OpenAI GPT
        │
        ▼
Extract JSON
        │
        ▼
Normalize Entities
        │
        ▼
Generate SQL
```

---

## Output

The Entity Extractor always returns structured JSON.

Example

```json
{
    "employee_name":"John",
    "department":"IT"
}
```

or

```json
{
    "employee_name":null,
    "department":"HR"
}
```

or

```json
{
    "employee_name":"Alice",
    "department":null
}
```

Using structured JSON makes the rest of the application much easier to implement and maintain.

---

## Benefits

- Understands natural language
- Reduces false fuzzy matches
- Improves normalization
- Produces structured data
- Simplifies SQL generation
- Makes the chatbot more accurate

# ❓ Why Not Generate SQL Directly?

A common question is:

> If GPT can generate SQL directly from the user's question, why do we need Query Preprocessor, Text Normalizer, and Entity Extractor?

The answer is **accuracy**.

Large Language Models are very good at understanding language, but they can still generate incorrect SQL when the input contains spelling mistakes, ambiguous words, or invalid entities.

---

## Without Preprocessing

Imagine the user asks:

```
what is jon leav?
```

The chatbot directly sends this question to GPT.

```
User Question
      │
      ▼
GPT
      │
      ▼
Generate SQL
```

GPT may misunderstand:

- `jon`
- `leav`

and generate incorrect SQL such as:

```sql
SELECT *
FROM employees
WHERE LOWER(name) LIKE LOWER('%jon%');
```

Since the database contains **John**, not **Jon**, no records are found.

---

## With Preprocessing

Instead, the chatbot first cleans the question.

```
User Question
      │
      ▼
Query Preprocessor
      │
      ▼
Entity Extractor
      │
      ▼
Text Normalizer
      │
      ▼
     GPT
      │
      ▼
Generate SQL
```

The processing becomes:

```
Original

↓

what is jon leav?

↓

Entity Extraction

↓

employee_name = jon

↓

Text Normalization

↓

John

↓

Keyword Correction

↓

leave

↓

Final Question

↓

What is John leave?
```

Now GPT generates:

```sql
SELECT leave_balance
FROM employees
WHERE LOWER(name)=LOWER('John');
```

The SQL is now correct.

---

## Benefits of Preprocessing

Without preprocessing:

❌ Typos cause database search failures.

❌ Wrong SQL may be generated.

❌ More hallucinations.

❌ Poor user experience.

---

With preprocessing:

✅ Correct employee names.

✅ Correct department names.

✅ Correct HR keywords.

✅ Better SQL generation.

✅ Better document retrieval.

✅ Better final answers.

---

## Complete Preprocessing Pipeline

```
                     User Question
                           │
                           ▼
                Query Preprocessor
                           │
                           ▼
                 Entity Extraction
                           │
                           ▼
                 Text Normalization
                           │
                           ▼
                    Clean Question
                           │
                           ▼
                    SQL Generation
                           │
                           ▼
                     SQLite Search
```

The cleaner the input, the more accurate the generated SQL.

# 📄 text_to_sql.py

## Purpose

`text_to_sql.py` converts a user's natural language question into a valid SQLite SQL query using a Large Language Model (LLM).

Instead of requiring users to write SQL manually, they simply ask questions in English.

The AI analyzes the question and automatically generates the appropriate SQL statement.

---

## Why Do We Need Text-to-SQL?

Most users do not know SQL.

For example, a Human Resources employee may ask:

```
Who works in HR?
```

Instead of writing:

```sql
SELECT *
FROM employees
WHERE LOWER(department)=LOWER('HR');
```

The chatbot generates this query automatically.

This makes database access much easier for non-technical users.

---

## Responsibilities

The `text_to_sql.py` module is responsible for:

- Receiving the normalized user question.
- Building the SQL generation prompt.
- Providing the database schema to GPT.
- Calling the OpenAI API.
- Generating a SQLite SELECT statement.
- Returning the SQL query to the caller.

---

## Complete Workflow

```
User Question
      │
      ▼
Normalized Question
      │
      ▼
Prompt Builder
      │
      ▼
Database Schema
      │
      ▼
OpenAI GPT
      │
      ▼
Generated SQL
      │
      ▼
SQLite Database
```

---

## Step 1 – Receive the User Question

Example

```
Who works in IT?
```

This question has already passed through:

- Query Preprocessor
- Entity Extractor
- Text Normalizer

Therefore the question is clean.

---

## Step 2 – Read Database Schema

GPT cannot generate SQL unless it knows the database structure.

The chatbot first loads the schema.

Example

```
employees

id

name

department

salary

leave_balance
```

This schema is included in the system prompt.

---

## Step 3 – Build the Prompt

Instead of asking GPT:

```
Generate SQL
```

the chatbot provides detailed instructions.

Example:

```
You are an expert SQLite query generator.

Generate ONLY SELECT statements.

Return ONLY SQL.

Use the following schema...

employees(
id,
name,
department,
salary,
leave_balance
)
```

Providing clear instructions significantly improves SQL quality.

---

## Step 4 – Generate SQL

GPT analyzes the question.

Example

```
Who works in HR?
```

↓

Generated SQL

```sql
SELECT *
FROM employees
WHERE LOWER(department)=LOWER('HR');
```

Another example

```
What is John's salary?
```

↓

```sql
SELECT salary
FROM employees
WHERE LOWER(name)=LOWER('John');
```

---

## Step 5 – Validate the SQL

Even after GPT generates SQL, the chatbot performs validation.

Example checks:

- Only SELECT statements are allowed.
- No INSERT.
- No UPDATE.
- No DELETE.
- No DROP.
- No ALTER.
- No CREATE.

This protects the database from accidental modification.

---

## Step 6 – Execute the SQL

The generated SQL is sent to SQLite.

```
Generated SQL
      │
      ▼
SQLite
      │
      ▼
Rows
```

Example

```
[(1,'John','IT',50000,20)]
```

The chatbot then converts these rows into a natural language response.

---

## Example 1

Question

```
Who works in HR?
```

Generated SQL

```sql
SELECT *
FROM employees
WHERE LOWER(department)=LOWER('HR');
```

Database Result

```
Alice
```

Final Answer

```
Alice works in the HR department.
```

---

## Example 2

Question

```
What is John's leave balance?
```

Generated SQL

```sql
SELECT leave_balance
FROM employees
WHERE LOWER(name)=LOWER('John');
```

Database Result

```
20
```

Final Answer

```
John has a leave balance of 20 days.
```

---

## Prompt Engineering

One of the most important parts of this module is the prompt.

The prompt instructs GPT to:

- Return only SQL.
- Avoid explanations.
- Use SQLite syntax.
- Generate only SELECT statements.
- Respect the provided database schema.
- Use case-insensitive comparisons.
- Prefer exact matches where appropriate.

A well-designed prompt results in much more accurate SQL generation.

---

## Benefits

- Users do not need SQL knowledge.
- Supports natural language queries.
- Generates SQL dynamically.
- Uses the latest database schema.
- Improves usability for non-technical users.

# 🔍 Search Pipeline Overview

After the user's question has been:

- Preprocessed
- Normalized
- Entities Extracted
- Converted into SQL (if required)

the chatbot must retrieve the requested information.

There are three possible search paths.

```
                    User Question
                          │
                          ▼
               Intent Classification
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   DATABASE          DOCUMENT          HYBRID
        │                 │                 │
        ▼                 ▼                 ▼
 sql_search.py      search.py      hybrid_search.py
        │                 │                 │
        ▼                 ▼                 ▼
     SQLite           Qdrant          Both Searches
        │                 │                 │
        └─────────────────┴─────────────────┘
                          │
                          ▼
                 answer_generator.py
                          │
                          ▼
                     Final Response
```

Each module has one responsibility.

This modular design makes the project easy to understand and maintain.

---

# 📄 sql_search.py

## Purpose

`sql_search.py` is responsible for searching the SQLite database.

Whenever the chatbot needs employee information such as:

- Employee Name
- Department
- Salary
- Leave Balance

this module executes the generated SQL query and returns the matching records.

Unlike `text_to_sql.py`, this module **does not generate SQL**.

It only executes SQL safely.

---

# Why Do We Need It?

Think of the chatbot like this:

```
User

↓

English Question

↓

GPT

↓

SQL

↓

SQLite

↓

Rows
```

`text_to_sql.py`

↓

Creates SQL

`sql_search.py`

↓

Runs SQL

Keeping these responsibilities separate makes the project easier to maintain.

---

# Responsibilities

- Connect to SQLite
- Execute SQL queries
- Fetch matching rows
- Return results
- Handle SQL errors safely

---

# Workflow

```
Generated SQL
      │
      ▼
SQLite Connection
      │
      ▼
Execute Query
      │
      ▼
Fetch Rows
      │
      ▼
Return Results
```

---

# Example

Generated SQL

```sql
SELECT *
FROM employees
WHERE LOWER(department)=LOWER('HR');
```

SQLite returns

```
[(2,'Alice','HR',45000,15)]
```

These rows are then passed to the Answer Generator.

---

# Why Separate SQL Generation and SQL Execution?

Many beginners ask:

Why not execute SQL immediately after GPT generates it?

Because these are two different responsibilities.

```
text_to_sql.py

↓

Generate SQL
```

```
sql_search.py

↓

Execute SQL
```

Separating responsibilities follows the **Single Responsibility Principle (SRP)**.

This makes debugging much easier.

---

# Benefits

- Cleaner architecture
- Easier testing
- Better error handling
- Reusable database layer

# 📄 search.py

## Purpose

`search.py` is responsible for searching company documents stored inside the Vector Database (Qdrant).

Unlike SQLite, this module searches based on **meaning**, not keywords.

This process is called **Semantic Search**.

---

# Why Do We Need Vector Search?

Suppose the HR policy contains

```
Employees receive 20 annual leave days.
```

The user asks

```
How many vacation days do employees get?
```

Keyword search fails because

```
annual leave

≠

vacation
```

Vector Search succeeds because both sentences have similar meanings.

---

# Responsibilities

- Convert the user's question into an embedding.
- Search Qdrant.
- Retrieve the most relevant document chunks.
- Return document context.

---

# Workflow

```
Question
     │
     ▼
Embedding
     │
     ▼
Qdrant Search
     │
     ▼
Relevant Chunks
     │
     ▼
Return Context
```

---

# Example

Question

```
Explain leave policy.
```

Embedding

↓

```
[0.12,
-0.44,
...
1536 values]
```

↓

Qdrant

↓

```
Chunk 12

Leave Policy
```

↓

Returned to GPT

---

# Why Use Semantic Search?

Traditional Search

```
leave
```

matches

```
leave
```

only.

Semantic Search understands

```
leave

vacation

paid leave

annual leave
```

have similar meanings.

This dramatically improves retrieval quality.

---

# Output

Instead of returning rows like SQLite,

this module returns

```
Relevant Document Chunks
```

Example

```
Employees receive 20 annual leave days.

Unused leave may be carried forward.
```

These chunks become context for GPT.

# 📄 hybrid_search.py

## Purpose

`hybrid_search.py` combines structured database search and semantic document search.

Some user questions require information from both sources.

This module coordinates both searches and merges the results.

---

# Why Do We Need Hybrid Search?

Example question

```
What is John's leave balance and explain the leave policy?
```

The question asks two different things.

```
John's leave balance

↓

SQLite
```

```
Leave Policy

↓

Qdrant
```

Both answers are required.

---

# Workflow

```
User Question
        │
        ▼
Intent = HYBRID
        │
        ├──────────────┐
        │              │
        ▼              ▼
SQLite Search     Vector Search
        │              │
        ▼              ▼
 Employee Data   Policy Context
        │              │
        └──────┬───────┘
               ▼
      Answer Generator
               ▼
        Final Response
```

---

# Example

Question

```
What is John's leave balance and explain leave policy?
```

SQLite

↓

```
John

Leave Balance

20
```

Qdrant

↓

```
Employees receive 20 paid annual leave days.

Unused leave can be carried forward.
```

Both results are combined.

Final response

```
John currently has 20 leave days.

According to the leave policy, employees receive 20 paid annual leave days and unused leave may be carried forward.
```

---

# Responsibilities

- Execute database search
- Execute vector search
- Combine both results
- Return a unified response

---

# Why Not Perform One Search?

Some information exists only in SQLite.

Some information exists only inside documents.

Hybrid Search combines both sources into one intelligent answer.

This approach is commonly used in enterprise AI systems.

---

# Benefits

- Richer answers
- Better user experience
- Combines structured and unstructured data
- Supports complex HR questions

# 🔄 Search Execution Flow

The following diagram illustrates how the search modules interact.

```
                     User Question
                           │
                           ▼
                Intent Classification
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
 DATABASE             DOCUMENT              HYBRID
      │                    │                    │
      ▼                    ▼                    ▼
sql_search.py        search.py         hybrid_search.py
      │                    │                    │
      ▼                    ▼                    ▼
SQLite Database     Qdrant Database     Both Databases
      │                    │                    │
      └────────────────────┴────────────────────┘
                           │
                           ▼
                 answer_generator.py
                           │
                           ▼
                    Final AI Response
```

Notice that each module performs only one specific task.

- `sql_search.py` retrieves structured employee data.
- `search.py` retrieves relevant HR document content.
- `hybrid_search.py` coordinates both searches when needed.

This separation follows the **Single Responsibility Principle (SRP)**, making the codebase modular, testable, and easy to extend.

# 📚 Document Indexing Pipeline

Before the chatbot can answer questions from HR documents, it must first understand those documents.

Computers cannot directly understand PDF, DOCX, or TXT files.

Instead, each document goes through a series of processing steps before it becomes searchable.

This process is called **Document Indexing**.

---

# Why is Document Indexing Needed?

Suppose your HR department provides this document:

```
Leave-Policy.pdf
```

A human can easily open it and read:

```
Employees receive 20 paid annual leave days.
```

However, an AI model cannot efficiently search an entire PDF every time a user asks a question.

Instead, the document is processed once and stored in a format optimized for semantic search.

---

# Complete Document Indexing Workflow

```
             HR Documents
                    │
                    ▼
            extract_pdf.py
                    │
                    ▼
               Plain Text
                    │
                    ▼
               chunker.py
                    │
                    ▼
            Small Text Chunks
                    │
                    ▼
             embeddings.py
                    │
                    ▼
             Vector Embeddings
                    │
                    ▼
          qdrant_service.py
                    │
                    ▼
         Store in Qdrant Database
                    │
                    ▼
         Ready for Semantic Search
```

This indexing process usually runs **once**, or whenever documents change.

---

# Why Split Documents?

Imagine a PDF with 100 pages.

Searching the entire document every time would be:

- Slow
- Expensive
- Less accurate

Instead we split it.

```
Leave Policy.pdf

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4

...
```

Now the chatbot searches only the most relevant chunks.

This improves both speed and accuracy.

---

# 📄 extract_pdf.py

## Purpose

This module extracts readable text from supported document formats.

AI models cannot search PDF files directly.

They first need plain text.

---

# Responsibilities

Depending on your implementation, this module reads:

- PDF
- DOCX
- TXT
- XLSX

and converts everything into plain text.

---

# Workflow

```
PDF

↓

Extract Text

↓

Plain Text
```

---

# Example

Input

```
Leave Policy.pdf
```

Output

```
Employees receive 20 annual leave days.

Unused leave can be carried forward.
```

---

# Why Not Store PDFs Directly?

PDFs contain

- formatting
- images
- page layouts
- fonts

The chatbot only needs the actual text.

Removing formatting makes later processing much easier.

---

# Benefits

- Supports multiple document formats
- Converts everything into plain text
- Provides input for chunking

# 📄 chunker.py

## Purpose

Large Language Models have context size limitations.

Very large documents must be divided into smaller pieces.

This process is called **Chunking**.

---

# Why Chunk Documents?

Suppose a handbook contains

```
250 pages
```

Searching all 250 pages for every question is inefficient.

Instead

```
250 Pages

↓

Chunk 1

Chunk 2

Chunk 3

...

Chunk N
```

Only the most relevant chunks are retrieved.

---

# Example

Original Text

```
Employees receive twenty days of annual leave.

Unused leave may be carried forward.

Managers must approve leave requests.
```

↓

Chunk 1

```
Employees receive twenty days of annual leave.
```

Chunk 2

```
Unused leave may be carried forward.
```

Chunk 3

```
Managers must approve leave requests.
```

---

# Chunk Size

A chunk usually contains

- 300–800 words

or

- 500–1000 tokens

depending on your implementation.

Choosing the right chunk size improves retrieval quality.

---

# Workflow

```
Document

↓

Plain Text

↓

Chunking

↓

Text Chunks
```

---

# Benefits

- Faster search
- Better retrieval
- Lower OpenAI cost
- Better GPT context

# 📄 embeddings.py

## Purpose

Computers cannot understand plain text.

They understand numbers.

This module converts every text chunk into a numerical vector called an **Embedding**.

---

# What is an Embedding?

An embedding is a list of floating-point numbers representing the semantic meaning of a sentence.

Example

```
Employees receive annual leave.
```

↓

```
[0.12,
-0.55,
0.98,
...
1536 numbers]
```

These numbers capture the meaning of the sentence.

---

# Why Use Embeddings?

Suppose two sentences are different.

Sentence A

```
Annual Leave
```

Sentence B

```
Vacation Days
```

Although the words differ,

their embeddings are very close together.

This allows semantic search.

---

# Workflow

```
Text Chunk

↓

OpenAI Embedding Model

↓

Vector

↓

Store in Qdrant
```

---

# Example

Chunk

```
Employees receive 20 annual leave days.
```

↓

Embedding

```
[0.11,
0.42,
...
1536 values]
```

---

# Benefits

- Enables semantic search
- Understands meaning
- Finds similar documents
- Supports Retrieval-Augmented Generation (RAG)

# 📄 qdrant_service.py

## Purpose

This module manages the connection between the chatbot and the Qdrant Vector Database.

Instead of repeatedly writing Qdrant connection code, everything is centralized here.

---

# Responsibilities

- Connect to Qdrant
- Create collections
- Insert vectors
- Search vectors
- Delete vectors (if needed)

---

# Workflow

```
Application

↓

Qdrant Service

↓

Qdrant Database
```

---

# Why Use a Service Layer?

Without this file

```
chat.py

↓

Qdrant Connection
```

```
search.py

↓

Qdrant Connection
```

```
index_documents.py

↓

Qdrant Connection
```

The same code would be duplicated many times.

Instead

```
All Files

↓

qdrant_service.py

↓

Qdrant
```

Only one module manages the connection.

---

# Benefits

- Cleaner code
- Centralized configuration
- Easier maintenance
- Reusable connection logic

# 📄 index_documents.py

## Purpose

This module builds the Vector Database.

It combines every document processing step into one pipeline.

---

# Responsibilities

- Read documents
- Extract text
- Split into chunks
- Generate embeddings
- Store vectors in Qdrant

---

# Workflow

```
Documents

↓

Extract Text

↓

Chunk Text

↓

Generate Embeddings

↓

Store in Qdrant
```

---

# Example

```
Leave Policy.pdf

↓

Extract Text

↓

15 Chunks

↓

15 Embeddings

↓

15 Vectors Stored
```

After indexing, the chatbot can answer questions from these documents almost instantly.

---

# Why Index Only Once?

Embedding generation is expensive.

Documents usually change infrequently.

Therefore the indexing process is typically executed:

- once during setup
- whenever documents are added
- whenever documents are updated

The chatbot simply searches the existing vectors during normal operation.

# 📄 inspect_qdrant.py

## Purpose

This module helps developers inspect the contents of the Qdrant Vector Database.

It is mainly used for debugging and development.

---

# Responsibilities

- Display collections
- Display stored vectors
- Display payloads
- Verify document indexing
- Check vector counts

---

# Example

```
Collection

↓

hr_documents

↓

Total Points

↓

245

↓

Payload

↓

Leave Policy.pdf
```

---

# Why is it Useful?

Suppose the chatbot cannot answer questions from a document.

Using this tool, you can verify:

- Was the document indexed?
- Were embeddings generated?
- Was the payload stored?
- Is the collection correct?

This significantly simplifies debugging.

---

# Benefits

- Easier debugging
- Verify indexing
- Inspect stored vectors
- Monitor collections

# 📊 Complete Document Processing Pipeline

The following diagram illustrates the complete lifecycle of an HR document.

```
            Leave Policy.pdf
                    │
                    ▼
          extract_pdf.py
                    │
                    ▼
             Plain Text
                    │
                    ▼
             chunker.py
                    │
                    ▼
             Text Chunks
                    │
                    ▼
            embeddings.py
                    │
                    ▼
         OpenAI Embeddings
                    │
                    ▼
         qdrant_service.py
                    │
                    ▼
        Qdrant Vector Database
                    │
                    ▼
             search.py
                    │
                    ▼
          Relevant Chunks
                    │
                    ▼
       answer_generator.py
                    │
                    ▼
             Final Response
```

Every module performs one well-defined responsibility, making the system modular, maintainable, and easy to extend.

For example, if you later replace OpenAI Embeddings with another embedding model or switch from Qdrant to a different vector database, only the corresponding modules need to change. The overall application workflow remains the same.

# Future plann
Planned Features

✓ Multi-language Support

✓ Voice Assistant

✓ Web UI

✓ Authentication

✓ Employee CRUD

✓ LangGraph Agent

✓ MCP Server

✓ Reranking

✓ Hybrid Search Optimization

✓ Conversation Memory