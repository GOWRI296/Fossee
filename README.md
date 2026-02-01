🧱 Osdag – Tension Member (Bolted) Module
Block Shear & Governing Capacity Validation using PyTest
📌 Overview

This project focuses on software development and testing for the bolted tension member design module inspired by Osdag (Open Steel Design and Graphics).

The objective is to:

Implement key failure mode checks for tension members

Ensure IS 800:2007 compliance

Validate correctness using unit and integration tests

Demonstrate engineering-grade test design, not just basic scripting

This work is suitable for FOSSEE / Osdag internship evaluation under the Software Development area of interest.

🏗️ Engineering Checks Covered (IS 800:2007)

The following limit states for bolted tension members are implemented and tested:

1️⃣ Gross Section Yielding

Ensures yielding does not occur across the full cross-section

Based on material yield strength

Clause reference: IS 800 – Clause 6.2

2️⃣ Net Section Rupture

Accounts for reduction due to bolt holes and shear lag

Includes the mandatory 0.9 reduction factor

Clause reference: IS 800 – Clause 6.3.1

3️⃣ Block Shear Failure

Evaluates combined shear and tension failure paths

Both possible block shear paths are checked

Governing (minimum) value is selected

Clause reference: IS 800 – Clause 6.4

4️⃣ Governing Tension Capacity

The final design strength is taken as the minimum of:

Gross yielding

Net rupture

Block shear

This mirrors real-world steel design practice used in Osdag

🧪 Testing Strategy

Testing is implemented using PyTest with a clear separation between unit tests and integration tests.

✔ Unit Tests

Gross section yielding calculation

Net section rupture calculation

Block shear strength evaluation

Input validation (negative areas, invalid values)

✔ Integration Test

Confirms that the correct governing failure mode is selected for a given member

✔ Edge Case Handling

Very small sectional areas

Invalid geometrical inputs

Scenarios where block shear governs over yielding or rupture

📁 Project Structure
osdag_pytest_project/
│
├── osdag/
│   └── design/
│       └── tension_member_bolted.py
│
├── tests/
│   ├── test_beam.py
│   └── tension/
│       ├── __init__.py
│       └── test_tension_bolted.py
│
├── venv/
└── README.md


This structure mirrors actual Osdag module paths, making the work easy to integrate or extend.

▶️ How to Run
1️⃣ Activate virtual environment
venv\Scripts\activate

2️⃣ Run tension member tests
python -m pytest tests\tension\test_tension_bolted.py -v

3️⃣ Run full test suite
python -m pytest -v

✅ Expected Output
collected 8 items
8 passed in ~0.04s


This confirms:

Correct implementation

Stable test discovery

No silent failures

🎯 Relevance to FOSSEE / Osdag

This project demonstrates:

Translation of structural design clauses into software logic

Use of test-driven validation for engineering software

Proper handling of governing limit states

Clean, modular, and extensible code structure

Readiness for extension into other Osdag modules

This aligns directly with Osdag’s goal of reliable, open-source structural design software.

🚀 Possible Extensions

Welded tension member module

Compression member buckling checks

Beam flexure and shear interaction

Coverage reporting using pytest-cov

Integration with Osdag section property databases

👤 Author

Gurujukota Gowri Nandhan
B.Tech – Computer Science & Engineering (AI & ML)
Interest Area: Engineering Software Development & Testing
