# Python Type-Annotated Functions Project

## Introduction

Type annotations in Python allow developers to **explicitly declare the expected types of function parameters and return values**.
While Python is a dynamically typed language, adding type hints improves **code readability**, **maintainability**, and **helps catch potential errors early** when combined with static type checkers like `mypy`.

This project demonstrates the use of type annotations in **basic functions, variable declarations, and more advanced constructs like closures and mixed-type operations**.
It provides practical examples of how annotations can make code **self-documenting** and easier to understand for other developers.

## Overview

This project consists of several Python functions that demonstrate the use of **type annotations** for function parameters and return values.
Type annotations improve **code readability**, provide **documentation**, and enable **static type checking** with tools like `mypy`.

---
### Tasks

| File                    | Function                                                                | Description                                                   |
| ----------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- |
| `0-add.py`              | `add(a: float, b: float) -> float`                                      | Returns the sum of two floats.                                |
| `1-concat.py`           | `concat(str1: str, str2: str) -> str`                                   | Concatenates two strings.                                     |
| `2-floor.py`            | `floor(n: float) -> int`                                                | Returns the floor of a float.                                 |
| `3-to_str.py`           | `to_str(n: float) -> str`                                               | Converts a float to its string representation.                |
| `4-define_variables.py` | `a: int, pi: float, i_understand_annotations: bool, school: str`        | Demonstrates variable type annotations.                       |
| `5-sum_list.py`         | `sum_list(input_list: List[float]) -> float`                            | Returns the sum of a list of floats.                          |
| `6-sum_mixed_list.py`   | `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`             | Returns the sum of a list containing ints and floats.         |
| `7-to_kv.py`            | `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`              | Returns a tuple of key and squared value.                     |
| `8-make_multiplier.py`  | `make_multiplier(multiplier: float) -> Callable[[float], float]`        | Returns a function that multiplies a float by the multiplier. |
| `9-element_length.py`   | `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` | Returns a list of tuples with each element and its length.    |

---

## Benefits of Type Annotations

* **Readability**: Makes it clear what type each parameter and return value should be.
* **Error Checking**: Tools like `mypy` can detect type mismatches before runtime.
* **Documentation**: Functions and variables become self-documented.
* **Maintainability**: Helps other developers understand and reuse the code safely.

---

## Python Type-Annotated Functions Glossary

| Type / Concept       | Description                                                                                                    | Example                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **int**              | Integer number                                                                                                 | `1`, `42`, `-7`                        |
| **float**            | Floating-point number (decimal)                                                                                | `3.14`, `0.5`                          |
| **str**              | String of characters                                                                                           | `"Hello"`, `"Holberton"`               |
| **bool**             | Boolean value                                                                                                  | `True`, `False`                        |
| **List[T]**          | List containing elements of type `T`                                                                           | `List[float]` → `[3.14, 1.0]`          |
| **Tuple[T1, T2]**    | Fixed-length tuple with specific types                                                                         | `Tuple[str, int]` → `("apple", 5)`     |
| **Iterable[T]**      | Any object that can be iterated over (e.g., list, tuple, set)                                                  | `Iterable[str]` → `["a", "b"]`         |
| **Sequence**         | Ordered collection supporting indexing and length                                                              | `str`, `list`, `tuple`                 |
| **Union[T1, T2]**    | Value can be either type `T1` or `T2`                                                                          | `Union[int, float]` → `3` or `3.14`    |
| **Callable[[T], R]** | Function that takes a parameter of type `T` and returns type `R`                                               | `Callable[[float], float]`             |
| **Annotations**      | Specify expected types for parameters and return values; improves readability and enables static type checking | `def add(a: float, b: float) -> float` |

---
Bien sûr ! Voici une section concise sur **mypy** que tu peux ajouter à ton README :

---

## Static Type Checking with mypy

[mypy](http://mypy-lang.org/) is a static type checker for Python.
It analyzes your code using type annotations to **detect type mismatches before runtime**, helping you catch potential errors early.

### How to use mypy:

1. Install mypy:

```bash
pip install mypy
```

2. Run mypy on your project:

```bash
mypy <your_project_folder>
```

3. Example:

```bash
mypy 5-sum_list.py
```

If types are correct, no errors are reported.
If a type mismatch exists, mypy will point out the problem, making your code safer and more reliable.

---
