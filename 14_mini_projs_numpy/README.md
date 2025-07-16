# 💡 Mini Projects Using NumPy

This folder contains beginner-friendly mini projects built with **NumPy**. Each project explores different concepts through fun, practical use cases that strengthen foundational Python + NumPy skills.

---

## 📁 Projects

### 🎲 Dice Roll Simulator  
**Simulates rolling two dice multiple times** and analyzes the frequency distribution of their summed outcomes.

**Built with:**
- Core Python (for logic & flow control)
- NumPy (for randomness and array efficiency)

**Concepts Practiced:**
- Random number generation
- Conditional logic & loops
- Dictionary usage
- NumPy arrays
- Counting unique values with `np.unique`

**File:** `dice_roll_simulator.ipynb`

---

### 📊 Grade Analytics Tool  
Analyzes student grade data to compute averages, evaluate performance, and identify top scorers using NumPy.

**Built with:**
- NumPy (for statistical analysis and efficient data handling)

**Concepts Practiced:**
- Array creation and manipulation
- Statistical functions (`mean`, `min`, `max`)
- Conditional filtering
- Basic data summarization

**File:** `grade_analytics_tool.ipynb`

---

### ✅ Sudoku Validator  
Validates a 9×9 Sudoku board by checking whether all rows, columns, and 3×3 subgrids contain unique digits from 1 to 9.

**Built with:**
- NumPy (for matrix manipulation and logic)

**Concepts Practiced:**
- 2D array slicing and flattening
- Uniqueness checks with `np.unique`
- Logical validations across axes
- Grid-based indexing

**File:** `sudoku_validator.ipynb`

---

### 🩺 Patient Vitals Monitor  
Simulates vitals for 10 patients over 7 days and analyzes patterns using 3D NumPy arrays.

**Vitals Tracked:**
- Temperature (°C)
- Pulse (bpm)
- Oxygen Saturation (%)

**Data Shape:** `(10 patients × 7 days × 3 vitals)`

**Tasks Covered:**
1. Generate realistic random vitals
2. Compute per-patient averages
3. Identify fever days (Temp > 37.5°C)
4. Flag patients with O₂ < 92%

**Concepts Practiced:**
- 3D array creation and reshaping
- Indexing, slicing, and masking
- Aggregation (`mean`, `any`)
- Boolean conditions with `np.where`

**File:** `patient_vitals_monitor.ipynb`

---

## Requirements
- Python 3.x  
- NumPy

---

## How to Run
Open the `.ipynb` files in **Jupyter Notebook** or **VS Code**, and run the cells interactively.

---

## Purpose
These mini-projects are part of my hands-on journey to master **NumPy** and build real-world intuition for **data analysis and array operations**.

More projects coming soon! 🌱✨
