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
# Create .env file and add your OpenAI API key
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
echo "ICL_DB_PATH=data/ICL.db" >> .env
echo "REQUEST_DB_PATH=data/request.db" >> .env
echo "OPENAI_MODEL=gpt-4o-2024-11-20" >> .env
echo "ICL_NUM=1" >> .env
echo "TEST_NUM=1" >> .env
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

**Note**: The database contains 20 different structural analysis word problems (SAWPs). You can change the `TEST_NUM` value (1-20) in your `.env` file to test different problem descriptions and see how the LLM handles various structural analysis scenarios.

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

> A unified framework integrating Large Language Models (LLMs) with the OpenSeesPy finite element engine for automated 2D frame analysis. The data layer structures user requirements and system instructions via a SQLite database; the model layer decomposes problems into parameter extraction, FE modeling, and visualization stages, invoking the LLM sequentially to generate executable Python scripts; and the output layer compiles numerical and graphical results (deformed shapes and internal force diagrams) into structured reports, achieving end-to-end structural analysis from natural language input.

## Instruction Examples

<p align="center">
  <img src="assets/Instruction_examples.png" style="width: 100%; height: auto;">
</p>

> Illustrations of embedded reasoning strategies—direction, number, and spatial rationality—used to enhance LLM structural understanding. Direction reasoning ensures correct load placement based on nodal coordinates; number reasoning validates element counts against problem descriptions; and space rationality reasoning enforces geometric consistency (e.g., vertical members share x-coordinates, horizontal members share y-coordinates). These rule-based instructions bridge the gap between textual problem descriptions and accurate structural code generation.

## Results

<p align="center">
  <img src="assets/stability.png" style="width: 100%; height: auto;">
</p>

> Quantitative evaluation of the generative stability of the proposed framework on 20 structural analysis word problems (SAWPs). Each bar represents the success rate (%) across five independent runs per problem. GPT-4o achieved consistent 100% accuracy on symmetric frame configurations but exhibited lower stability (40–80%) in asymmetric or multi-story cases, reflecting challenges in spatial reasoning under text-only inputs. The results confirm that structured instruction tuning significantly improves reproducibility and execution reliability of LLM-generated structural analyses.

## Dataset

The framework uses the **SAWP-20 Benchmark Dataset** for structural analysis word problems:

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-blue)](https://huggingface.co/datasets/NateLiang/SAWP20)

**[SAWP-20 Dataset](https://huggingface.co/datasets/NateLiang/SAWP20)** - A comprehensive benchmark containing 20 structural analysis word problems with ground truth schematics and problem descriptions.

### Dataset Features:
- **20 Structural Analysis Problems**: Diverse 2D frame configurations
- **Ground Truth Schematics**: Visual representations of each problem
- **Detailed Problem Descriptions**: Complete structural parameters and loading conditions
- **Standardized Format**: Consistent problem structure for benchmarking

### Problem Types Include:
- Simple 2D frames with columns and girders
- Multi-story and multi-bay configurations
- Diagonal bracing systems
- Cantilever beam structures
- Various loading conditions (point loads, distributed loads)

The dataset provides a robust foundation for evaluating LLM performance in structural analysis code generation across different complexity levels.

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