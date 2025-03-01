# Linear Algebra Concepts in Python 📊

<div style="text-align: center;"> 
  
![Linear Algebra](https://media.giphy.com/media/3o7aCWDyW0PJCsxHna/giphy.gif?cid=790b7611c7krx0w13vqq3o5a9rfysherckkbhwor4uaiwubh&ep=v1_gifs_search&rid=giphy.gif&ct=g) 
</div>


This repository contains implementations of various linear algebra concepts using Python and the NumPy library. The code is well-documented to serve as an educational resource for learning matrix operations and their practical implementations.

---

## 📋 Features
- **Matrix Creation**: Generate matrices of any size.
- **Matrix Addition & Subtraction**: Perform element-wise operations.
- **Matrix Multiplication**: Use dot product for matrix multiplication.
- **Transpose**: Get the transpose of a matrix.
- **Determinant Calculation**: Find determinants of square matrices.
- **Matrix Inversion**: Compute the inverse of a matrix.

---

## 🛠️ Requirements
- Python 3.7 or higher
- NumPy library

Install the necessary packages using:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
linear-algebra-concepts-python/
├── README.md               # Project information and usage
├── requirements.txt        # Required libraries
├── src/
│   ├── matrices.py         # Matrix operations implementations
├── tests/
│   ├── test_matrices.py    # Unit tests for matrix operations
```

---

## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/linear-algebra-concepts-python.git
```

2. **Navigate into the project directory:**

```bash
cd linear-algebra-concepts-python
```

3. **Create a virtual environment and activate it:**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🖩 Example Usage

Here is a quick example of how to use the functions:

```python
from src.matrices import create_matrix, add_matrices, matrix_determinant

A = create_matrix(2, 2, [1, 2, 3, 4])
B = create_matrix(2, 2, [5, 6, 7, 8])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", add_matrices(A, B))
print("Determinant of A:", matrix_determinant(A))
```

---

## 🧪 Running Tests

To run the tests, use:

```bash
pytest tests/
```

---

## 🛠️ Contributing

1. **Fork** the repository.
2. **Create** a new branch: `git checkout -b my-feature`.
3. **Commit** your changes: `git commit -m 'Add some feature'`.
4. **Push** to the branch: `git push origin my-feature`.
5. **Open a Pull Request**.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments

- This project is built using the amazing [NumPy](https://numpy.org/) library.
- Inspired by linear algebra concepts in data science and machine learning.

---

Made with ❤️ by [Aya Nabil](https://github.com/1AyaNabil1)

