# Python Engineering Libraries

An educational project covering Python libraries for engineering applications, with a focus on CFD, simulation, optimization, and digital twins.

## Structure

```
python-engineering-libraries/
├── notebooks/
│   ├── 01_core/           # Core scientific computing
│   ├── 02_optimization/   # Optimization & DOE
│   ├── 03_cad_meshing/    # CAD & meshing for CFD
│   ├── 04_ml/             # Machine learning for engineering
│   ├── 05_data/           # Data workflows & CFD post-processing (incl. OpenFOAM)
│   ├── 06_testing_quality/# Testing & code quality
│   └── 07_build_packaging/# Build & packaging
├── examples/              # Standalone Python scripts
├── tests/                 # Test suite
├── requirements.txt       # Python dependencies
└── README.md
```

## Libraries Covered

### Core Scientific Computing
- `numpy` — Array operations, linear algebra
- `scipy` — Optimization, integration, ODEs
- `matplotlib` — 2D/3D plotting
- `pandas` — Data manipulation
- `sympy` — Symbolic math

### Optimization & DOE
- `pyDOE` — Design of experiments
- `piglot` — Derivative-free optimization
- `deap` — Evolutionary algorithms
- `salib` — Sensitivity analysis

### CAD & Meshing for CFD
- `cadquery` — Parametric CAD
- `gmsh` — Mesh generation
- `trimesh` — Mesh processing

### Machine Learning
- `torch` — Neural networks, PINNs
- `scikit-learn` — Classical ML
- `xgboost` — Gradient boosting

### Data & Visualization
- `plotly` — Interactive plots
- `streamlit` — Web dashboards
- `OpenFOAM` — CFD solver integration

### Testing & Quality
- `pytest` — Testing
- `mypy` — Type checking
- `ruff` — Linter/formatter

### Build & Packaging
- `poetry` — Dependency management
- `uv` — Fast package installer
- `hatch` — Build system

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open notebooks in Jupyter:
   ```bash
   jupyter notebook
   ```

3. Work through notebooks in order (01 → 07)

**Total: 25 notebooks**

## Use Case

This project is designed for engineers working with OpenFOAM, CFD simulations, and digital twins. Each notebook includes:
- Theory background
- Practical examples
- Engineering applications
- Exercises for practice

## License

MIT
