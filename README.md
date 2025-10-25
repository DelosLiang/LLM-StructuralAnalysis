<p align="center">
  <img src="assets/logo.png" style="width: 60%; height: auto;">
</p>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/nateliang/LLM_FEM_UoA" target="_blank"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-LLM_FEM_UoA-14C290?logo=github"/></a>
  <a href="https://github.com/nateliang/LLM_FEM_UoA/issues" target="_blank"><img alt="Issues" src="https://img.shields.io/badge/Issues-Report%20Bug-red?logo=github"/></a>
  <a href="https://github.com/nateliang/LLM_FEM_UoA/stargazers" target="_blank"><img alt="Stars" src="https://img.shields.io/badge/Stars-⭐-yellow?logo=github"/></a>
</div>

---

# LLM_FEM_UoA: LLM-Powered Finite Element Method Framework

> 🎉 **LLM_FEM_UoA** - A novel approach to finite element method analysis using Large Language Models for automated problem solving and analysis.

<div align="center">

🚀 [LLM_FEM_UoA Framework](#llm_fem_uoa-framework) | ⚡ [Installation & Setup](#installation-and-setup) | 🎬 [Demo](#demo) | 📦 [Usage](#usage) | 🤝 [Contributing](#contributing) | 📄 [Citation](#citation)

</div>

## LLM_FEM_UoA Framework

LLM_FEM_UoA is an innovative framework that combines Large Language Models with Finite Element Method analysis. The system leverages LLM capabilities to automate problem setup, analysis, and interpretation of FEM results, making complex engineering analysis more accessible and efficient.

<p align="center">
  <img src="assets/framework_diagram.png" style="width: 100%; height: auto;">
</p>

> This framework is designed for research and educational purposes. Analysis results may vary based on model parameters, problem complexity, and other factors. Always verify results through traditional FEM methods for critical applications.

Our framework decomposes complex FEM problems into manageable components, ensuring robust and scalable analysis approaches.

### Core Components
- **Problem Parser**: Interprets natural language problem descriptions and converts them to FEM parameters
- **Mesh Generator**: Automatically generates appropriate mesh configurations based on problem specifications
- **Solver Interface**: Integrates with FEM solvers and manages computational workflows
- **Result Interpreter**: Analyzes and interprets FEM results using LLM reasoning

<p align="center">
  <img src="assets/components.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

### Analysis Pipeline
- Comprises automated problem setup, mesh generation, solving, and post-processing stages that work together to provide comprehensive FEM analysis.

<p align="center">
  <img src="assets/pipeline.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

### Database Management
- Manages in-context learning contexts and problem sets through integrated database systems for efficient data handling and retrieval.

<p align="center">
  <img src="assets/database.png" width="70%" style="display: inline-block; margin: 0 2%;">
</p>

## Installation and Setup

### Installation

Clone LLM_FEM_UoA:
```bash
git clone https://github.com/nateliang/LLM_FEM_UoA.git
cd LLM_FEM_UoA
```

Create a virtual environment:
```bash
conda create -n llm_fem python=3.9
conda activate llm_fem
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Required APIs

You will need API access for the LLM components. Configure your API keys:

```bash
export OPENAI_API_KEY=$YOUR_OPENAI_API_KEY
# Add other API keys as needed
```

Alternatively, create a `.env` file in the project root:
```bash
cp .env.example .env
# Edit .env with your actual API keys
```

## Demo

The main demonstration is available in `main.ipynb`, which shows how the model works for Example 15.

<p align="center">
  <img src="assets/demo_screenshot.png" width="100%" style="display: inline-block; margin: 0 2%;">
</p>

## Usage

### Python Usage

To use LLM_FEM_UoA in your code:

```python
from llm_fem.core import LLMFEMAnalyzer
from llm_fem.config import DEFAULT_CONFIG

analyzer = LLMFEMAnalyzer(debug=True, config=DEFAULT_CONFIG.copy())

# Run analysis
result = analyzer.analyze("Example 15", problem_description)
print(result)
```

### Configuration

You can customize the configuration for different analysis types:

```python
from llm_fem.core import LLMFEMAnalyzer
from llm_fem.config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["model"] = "gpt-4"  # Use a different model
config["mesh_density"] = "high"  # Adjust mesh parameters
config["solver_type"] = "iterative"  # Choose solver type

# Initialize with custom config
analyzer = LLMFEMAnalyzer(debug=True, config=config)

# Run analysis
result = analyzer.analyze("Custom Problem", problem_description)
print(result)
```

## Project Structure

- **main.ipynb**: Shows an example of how our model works for Example 15
- **full document/**: Contains the core files for running the program
  - **gpt_test_v2.py**: The main program
  - **ICL.db**: Consists of in-context learning contexts as system instructions
  - **request.db**: Consists of the full problem set
  - **database_utils.py**: Database management utilities
  - **ICLChecker.py**: ICL context validation
  - **RequestChecker.py**: Request validation
  - **post_proc.py**: Post-processing utilities

## Contributing

We welcome contributions from the community! Whether it's fixing a bug, improving documentation, or suggesting a new feature, your input helps make this project better.

## Citation

Please reference our work if you find *LLM_FEM_UoA* provides you with some help :)

```
@misc{liang2024llmfem,
      title={LLM_FEM_UoA: LLM-Powered Finite Element Method Framework}, 
      author={Nate Liang},
      year={2024},
      url={https://github.com/nateliang/LLM_FEM_UoA}, 
}
```