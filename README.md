# 🎯 Azentrix TypedModel

Azentrix TypedModel is a strict nested data modeling framework built on top of Pydantic.

---

## Background

Modern applications consume heterogeneous data inputs:

* API payloads (JSON)
* CLI arguments (string-based)
* Database records
* Environment variables
* Event streams
* ML pipeline metadata

These inputs may contain:

* `str`
* `int`
* `float`
* `bool`
* `datetime`
* `list`
* `tuple`
* `Enum`
* Nested structured objects

While Pydantic provides powerful BaseModel validation, developers often:

* Accept raw dictionaries
* Return dict responses
* Break strong typing
* Lose nested model guarantees
* Pass around unvalidated structures

This creates:

* Runtime validation errors
* Schema drift
* Inconsistent nested object typing
* Weak domain modeling
* Hard-to-maintain large systems

---

# 🚩 Core Problem

Build a Python pip package that:

1. Accepts arbitrary primitive input types:

   * string
   * integer
   * float
   * boolean
   * list
   * tuple
   * datetime
   * optional types

2. Converts and validates them into:

   * Strongly typed BaseModel objects
   * Fully nested BaseModel structures
   * No dictionary outputs
   * Only typed model objects or typed collections of models

3. Guarantees:

   * Output is ALWAYS a Pydantic BaseModel or nested BaseModel
   * No raw dict output allowed
   * No loosely structured data
   * Full type safety end-to-end

---

# 🧠 Functional Requirements

## Input

The system must accept:

```python
str
int
float
bool
list[Any]
tuple[Any]
datetime
Union types
Optional types
```

## Output

Must return:

```python
BaseModel
Nested BaseModel
List[BaseModel]
Tuple[BaseModel]
```

❌ Must NOT return:

* dict
* Any untyped structure
* Raw JSON

---

# 🏗 Architectural Goals

1. Strict typing
2. Nested schema composition
3. Model registry
4. Type coercion layer
5. Configurable validation policies
6. Extensible base abstraction

---

# 📂 Modern Production Folder Structure

We use `src/` layout.

```
azentrix-typedmodel/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
│
├── src/
│   └── azentrix_typedmodel/
│       │
│       ├── __init__.py
│       ├── base.py
│       ├── registry.py
│       ├── factory.py
│       ├── validators.py
│       ├── exceptions.py
│       ├── config.py
│       │
│       ├── nested/
│       │   ├── __init__.py
│       │   ├── builder.py
│       │   └── composer.py
│       │
│       └── typing/
│           ├── __init__.py
│           └── primitives.py
│
├── tests/
│   ├── test_base.py
│   ├── test_nested.py
│   └── test_factory.py
│
└── docs/
    ├── architecture.md
    └── usage.md
```

---

# 🧩 High-Level Architecture

```
Input Data
   ↓
Type Coercion Layer
   ↓
Validation Layer (Pydantic)
   ↓
Model Builder
   ↓
Nested Composer
   ↓
Typed Output (BaseModel)
```

---

# 🔧 pyproject.toml (Modern Format)

```toml
[build-system]
requires = ["setuptools>=65.0"]
build-backend = "setuptools.build_meta"

[project]
name = "azentrix-typedmodel"
version = "0.1.0"
description = "Strict nested typed data modeling framework built on Pydantic"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [{name="Azentrix Technologies"}]

dependencies = [
    "pydantic>=2.0"
]

[project.optional-dependencies]
dev = [
    "pytest",
    "mypy",
    "ruff",
    "black"
]

[tool.setuptools.packages.find]
where = ["src"]
```

---

# 🧱 Core Module Design

## 1️⃣ base.py

Defines strict base abstraction:

```python
from pydantic import BaseModel

class StrictBaseModel(BaseModel):
    model_config = {
        "extra": "forbid",
        "validate_assignment": True
    }
```

Ensures:

* No extra keys
* Strict schema enforcement

---

## 2️⃣ factory.py

Responsible for:

* Accepting arbitrary input
* Mapping to appropriate model
* Enforcing BaseModel-only return

---

## 3️⃣ nested/composer.py

Responsible for:

* Building nested model trees
* Ensuring nested structures are BaseModels
* Preventing dict leakage

---

## 4️⃣ registry.py

Model registration system:

* Register domain models
* Dynamic mapping from input schema → model class

---

# 🧪 Testing Strategy

Using:

* pytest

Test goals:

* Primitive coercion
* Nested validation
* Union type validation
* Type mismatch handling
* Strict no-dict enforcement

---

# 🔐 Validation Rules

| Rule             | Description               |
| ---------------- | ------------------------- |
| Strict Types     | No implicit dict returns  |
| Nested Only      | Deep nesting allowed      |
| Configurable     | Strict or permissive mode |
| Immutable Option | Frozen model config       |

---

## 📜 License

MIT License

---

# 🧩 Future Roadmap

* Schema introspection engine
* Graph-based model composition
* Domain DSL layer
* JSON schema exporter
* Plugin-based validation rules

---
