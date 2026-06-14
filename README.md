# 📚 AI Notes & Quiz Generator

## Overview

This project uses **LangChain**, **Hugging Face**, and **RunnableParallel** to generate:

- Short study notes
- Quiz questions
- A merged learning document

The application processes a given text and simultaneously generates notes and quiz questions using parallel LLM chains.

---

## Features

- Generate concise notes from any text
- Generate quiz questions automatically
- Parallel execution using LangChain's `RunnableParallel`
- Merge outputs into a single study document
- Powered by Qwen 2.5 7B Instruct

---

## Tech Stack

- Python
- LangChain
- Hugging Face Inference API
- Qwen2.5-7B-Instruct
- Python Dotenv

---

## Project Workflow

```text
Input Text
    │
    ▼
RunnableParallel
 ├── Notes Generator
 └── Quiz Generator
    │
    ▼
Merge Chain
    │
    ▼
Final Study Material
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Notes-and-Quiz-Generator.git
cd AI-Notes-and-Quiz-Generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_api_token_here
```

---

## Usage

Run the script:

```bash
python app.py
```

---

## Example Input

```text
A random forest is a machine learning ensemble method that combines multiple decision trees to improve predictive accuracy and reduce overfitting.
```

---

## Example Output

### Notes

- Random Forest is an ensemble learning algorithm.
- It combines multiple decision trees.
- It improves prediction accuracy.
- It reduces overfitting.

### Quiz Questions

1. What is a Random Forest?
2. Why does Random Forest use multiple decision trees?
3. How does Random Forest help reduce overfitting?

---

## Project Structure

```text
├── app.py
├── README.md
├── requirements.txt
├── .env
└── venv/
```

---

## LangChain Concepts Used

- PromptTemplate
- RunnableParallel
- Output Parsers
- Chain Composition
- Hugging Face Integration

---

## Future Improvements

- Streamlit Web App
- PDF Export
- Flashcard Generation
- MCQ Generation
- Multi-language Support

---

## Author

**Harsh Saini**

AI Engineer | Machine Learning Enthusiast | Generative AI Developer
