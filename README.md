# LLM-FEM Integration Framework

A framework for integrating Large Language Models (LLMs) with Finite Element Method (FEM) analysis for automated structural analysis.

## Project Structure

```
LLM_FEM_UoA/
├── src/                    # Source code
│   ├── structural_analysis.py  # Generated structural analysis code
│   ├── post_proc.py        # Post-processing module
│   └── full_program.py     # Complete program integration
├── config/                 # Configuration files
│   └── param_config.py     # Parameter configuration
├── utils/                  # Utility modules
│   ├── database_utils.py   # Database operations
│   ├── ICLChecker.py       # ICL data checker
│   ├── ICLDataSaver.py     # ICL data saver
│   ├── RequestChecker.py    # Request checker
│   └── RequestMerger.py     # Request merger
├── data/                   # Data files
│   ├── *.db               # SQLite databases
│   └── *.txt              # Text data files
├── main.py                 # Main entry point (GPT API integration)
├── requirements.txt        # Python dependencies
├── env.example            # Environment variables template
└── README.md              # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Windows OS (primary development platform)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/DelosLiang/LLM_FEM_UoA.git
cd LLM_FEM_UoA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp env.example .env
# Edit .env file with your OpenAI API key and other configurations
```

4. Configure your `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
ICL_DB_PATH=data/ICL.db
REQUEST_DB_PATH=data/request.db
OPENAI_MODEL=gpt-4o-2024-11-20
ICL_NUM=1
TEST_NUM=1
```

## Usage

### Basic Usage

Run the main program:
```bash
python main.py
```

### GPT API Testing

Test the GPT API integration:
```bash
python main.py
```

### Database Management

- **ICL Data Management**: Use `utils/ICLDataSaver.py` to manage ICL (In-Context Learning) data
- **Request Management**: Use `utils/RequestMerger.py` to manage request data
- **Data Checking**: Use `utils/ICLChecker.py` and `utils/RequestChecker.py` to verify data

## Framework Overview

<p align="center">
  <img src="assets/workflow.png" style="width: 100%; height: auto;">
</p>

## Instruction Examples

<p align="center">
  <img src="assets/Instruction_examples.png" style="width: 100%; height: auto;">
</p>

## Results

<p align="center">
  <img src="assets/stability.png" style="width: 100%; height: auto;">
</p>

## Features

- **Automated Code Generation**: Uses LLMs to generate OpenSeesPy structural analysis code
- **Database Integration**: SQLite-based storage for ICL examples and user requests
- **Modular Design**: Clean separation of concerns with utility modules
- **Environment Configuration**: Secure API key management through environment variables
- **Cross-platform Compatibility**: Designed for Windows with potential Linux/macOS support

## Dependencies

- `openseespy`: OpenSees Python interface for structural analysis
- `opsvis`: Visualization tools for OpenSees
- `matplotlib`: Plotting and visualization
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `sqlite3`: Database operations

## Configuration

The framework uses environment variables for configuration. Key variables include:

- `OPENAI_API_KEY`: Your OpenAI API key
- `ICL_DB_PATH`: Path to ICL database
- `REQUEST_DB_PATH`: Path to request database
- `OPENAI_MODEL`: OpenAI model to use
- `ICL_NUM`: ICL example number
- `TEST_NUM`: Test case number

## Citation

```bibtex
@article{liang2025integrating,
  title={Integrating Large Language Models for Automated Structural Analysis},
  author={Liang, Haoran and Kalaleh, Mohammad Talebi and Mei, Qipei},
  journal={arXiv preprint arXiv:2504.09754},
  year={2025}
}
```

## Disclaimer

**Research and Educational Purpose Only.**  
The LLM-FEM integration framework, methods, code, and data described in this project are developed solely for academic research and educational use. They are not intended, nor should they be relied upon, for direct application in real-world structural engineering design, analysis, or construction. The authors, their institutions, and any collaborators explicitly disclaim all liability for any consequences, including but not limited to structural analysis errors, computational inaccuracies, design deficiencies, or failures, arising from the use, misuse, or adaptation of the methods, parameters, or algorithms presented herein. Any attempt to implement or deploy the system in practice is done entirely at the user's own risk and responsibility.