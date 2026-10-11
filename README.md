# Byte Agent - A Simple Natural Language Data Analysis Agent

My submission for byte @ mait for 2026 under the applied ML category. It's a simple data analysis agent that uses tools built with Python, pandas,
and Google's Gemini API. It accepts natural language queries about a tabular dataset, accordingly selects the appropriate tools, executes those tools
and then interprets the returned result to produce an answer.

## Features

The agent provides five analysis tools:

- Inspection - returns the number of rows, column names, data types, and missing values.
- Filtering - returns records matching a specific column value, with validation for unknown columns.
- Grouped aggregation - performs aggregate function (sum, mean, max, min, and count) for grouped data.
- Cleaning data - creates a copy of the dataset that replaces missing values in the dataset with the median of the column for numerical data types or the mode otherwise. It also leaves completely empty columns alone, so as to not fabricate any data.
- Visualisation - creates a plot from selected columns and saves it as plot.png.

## How does it work?

1. The user enters a natural language query about the dataset
2. The model receives the question and the available tool definitions.
3. The model selects the appropriate tools and supplies their arguments.
4. Python executes the selected tools using pandas/matplotlib.
5. The tool results are returned to the model.
6. The agent repeats this process until the model produces a final answer or the iteration limit is reached.

The model chooses which operations to perform, whereas the execution of the operations are performed by python tools.
The agent also handles tool errors and converts results into JSON-compatible values before sending them back to the model.

## Project structure

```bash
.
├── data
│   └── employee.csv
├── README.md
├── requirements.txt
├── src
│   ├── agent.py
│   └── tools.py
└── tests
    └── tool_tests.py

```

### Files

- `src/agent.py` - The agent loop and interaction with Gemini.
- `src/tools.py` - The pandas/matplotlib analysis tools used by the agent.
- `data/employee.csv` - A sample dataset used for the project.
- `tests/tool_tests.py` - Tests for the analysis tools.
- `requirements.txt` - Python dependencies.

## Installation

### Prerequisites

- Python 3.11 or newer
- A Google Gemini API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/FiringRac/byte-agent
cd byte-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Linux / macOS (Bash or Zsh):**

```bash
source .venv/bin/activate
```

**Linux (Fish shell):**

```fish
source .venv/bin/activate.fish
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the API key

Set the `GEMINI_API_KEY` environment variable to your Google Gemini API key.

**Linux / macOS (Bash or Zsh):**

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

**Linux (Fish shell):**

```fish
set -x GEMINI_API_KEY "YOUR_API_KEY"
```

**Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
```
Replace `YOUR_API_KEY` with your own key.

## Usage

Run the agent from the project root directory:

```bash
python src/agent.py
```

Enter a natural-language question about the dataset when prompted. The agent will select and execute relevant analysis tools and return an answer.

The sample dataset is located at `data/employee.csv`.

Example questions:

- How many rows are in the dataset?
- What is the average salary for each city?
- Show all records where the city is Delhi.
- Which columns contain missing values?

The plotting tool saves its output as `plot.png` in the current working directory.

## Running Tests

Run the tool tests from the project root:

```bash
python tests/tool_tests.py
```

These tests check the analysis tools, including inspection, filtering, grouped aggregation, missing-value handling, and validation of invalid inputs.

## Limitations

- The agent currently loads the sample CSV from `data/employee.csv`.
- The cleaning tool returns a cleaned copy; it does not modify the original dataset used by the other tools.
- Completely empty columns remain missing because no replacement value can be inferred from the available data.
- Plot output is saved to `plot.png` in the current working directory.
- Responses depend on the availability and quota limits of the Gemini API.