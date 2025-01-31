# How to Think Step-by-Step

Code for the paper: "How to think step-by-step: A mechanistic understanding of chain-of-thought reasoning"

## Project Structure

```
.
├── src/                    # Source code
│   ├── probing/           # Probing analysis code
│   ├── attention/         # Attention analysis
│   ├── information_flow/  # Information flow analysis
│   └── utils/             # Utility functions
├── notebooks/             # Jupyter notebooks for analysis and visualization
├── data/                  # Data directory
│   ├── raw/              # Raw data
│   └── processed/        # Processed data
├── tests/                # Test files
├── configs/              # Configuration files
└── results/              # Output results and figures
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Code

The analysis pipeline consists of several stages that should be run in sequence. Here's the recommended order:

### 1. Dataset Creation and Preprocessing
```bash
# Generate the dataset of fictional ontologies
cd src/dataset_creation
python createDatasetCOTPatching.py

# Process and prepare the data
jupyter notebook notebooks/addLastDataset.ipynb
```

### 2. Head Identification Analysis

Run these notebooks in sequence to identify different types of attention heads:

1. **Attention Head Identification**:
   ```bash
   jupyter notebook notebooks/head_performance_analysis.ipynb
   ```
   - Identifies and categorizes attention heads
   - Generates `results/head_identification.json`

2. **Information Flow Analysis**:
   ```bash
   cd src/information_flow
   python decisionHorizon.py
   ```
   - Analyzes information flow patterns
   - Outputs results to `results/information_flow/`

### 3. Probing Analysis

Run the probing analysis to understand the model's internal representations:

1. **Setup Probing Environment**:
   ```bash
   cd src/probing
   # Configure probing parameters in configs/default_config.py
   ```

2. **Run Probing Analysis**:
   ```bash
   python run_probing.py
   ```
   - Generates probing results in `results/probing/`

### 4. Performance Analysis

Analyze the performance of identified heads:

1. **Head Performance Analysis**:
   ```bash
   jupyter notebook notebooks/head_performance_analysis.ipynb
   ```
   - Analyzes performance across different subtasks
   - Generates visualizations and statistical analysis

2. **Horizon Analysis**:
   ```bash
   cd src/horizon
   python horizonActivationPatching.py
   ```
   - Analyzes decision horizons
   - Outputs to `results/horizon/`

### 5. Visualization and Results

Generate final visualizations and compile results:

1. Run visualization notebooks:
   ```bash
   jupyter notebook notebooks/visualization/
   ```
   - Creates figures for paper
   - Generates summary statistics

2. Check results in `results/` directory:
   - Performance metrics
   - Statistical analyses
   - Generated figures

## Configuration

Key configuration files:

- `configs/default_config.py`: Main configuration file
- Individual configuration files in respective module directories

Modify these files to adjust:
- Model parameters
- Analysis settings
- Data paths
- Visualization preferences

## Results

The analysis pipeline generates several types of results:

1. **Head Identification**
   - Lists of identified heads by function
   - Head distribution analysis

2. **Performance Analysis**
   - Head performance across subtasks
   - Layer-wise analysis
   - Statistical significance tests

3. **Visualizations**
   - Performance plots
   - Attention pattern visualizations
   - Layer-wise distribution plots

Results are saved in the `results/` directory with the following structure:
```
results/
├── head_identification/
├── probing/
├── information_flow/
├── horizon/
└── visualizations/
```

## Citation

If you use this code in your research, please cite:

[Citation information]

## License

[License information]
