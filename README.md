🧱 Osdag – Tension Member (Bolted) Design
Block Shear & Governing Capacity | PyTest-Based Validation
📌 Project Overview

This project implements and validates the design strength calculations for bolted steel tension members as per IS 800:2007.
The focus is on software development and testing, aligning with the Osdag (Open Steel Design and Graphics) philosophy.

The work covers:

Individual failure modes of tension members

Governing design strength logic

Robust unit and integration testing using PyTest

This repository is structured to closely resemble real Osdag module paths, making it suitable for extension or direct integration.

📐 Engineering Scope (IS 800:2007)

The following design checks are implemented and tested:

1️⃣ Gross Section Yielding (Clause 6.2)
𝑇
𝑑
𝑔
=
𝐴
𝑔
𝑓
𝑦
𝛾
𝑚
0
T
dg
	​

=
γ
m0
	​

A
g
	​

f
y
	​

	​


Ensures yielding does not occur in the gross section

Partial safety factor: γₘ₀ = 1.1

2️⃣ Net Section Rupture (Clause 6.3.1)
𝑇
𝑑
𝑛
=
0.9
𝐴
𝑛
𝑓
𝑢
𝛾
𝑚
1
T
dn
	​

=
γ
m1
	​

0.9A
n
	​

f
u
	​

	​


Accounts for bolt holes and shear lag

Reduction factor 0.9 as per IS 800

Partial safety factor: γₘ₁ = 1.25

3️⃣ Block Shear Strength (Clause 6.4)

Two possible block shear failure paths are evaluated, and the minimum governs:

𝑇
𝑑
𝑏
1
=
𝐴
𝑣
𝑔
𝑓
𝑦
𝛾
𝑚
0
+
0.9
𝐴
𝑡
𝑛
𝑓
𝑢
𝛾
𝑚
1
T
db1
	​

=
γ
m0
	​

A
vg
	​

f
y
	​

	​

+
γ
m1
	​

0.9A
tn
	​

f
u
	​

	​

𝑇
𝑑
𝑏
2
=
0.9
𝐴
𝑣
𝑔
𝑓
𝑢
𝛾
𝑚
1
+
𝐴
𝑡
𝑛
𝑓
𝑦
𝛾
𝑚
0
T
db2
	​

=
γ
m1
	​

0.9A
vg
	​

f
u
	​

	​

+
γ
m0
	​

A
tn
	​

f
y
	​

	​

4️⃣ Overall Tension Capacity

The governing design strength is taken as:

𝑇
𝑑
=
min
⁡
(
𝑇
𝑑
𝑔
,
𝑇
𝑑
𝑛
,
𝑇
𝑑
𝑏
)
T
d
	​

=min(T
dg
	​

,T
dn
	​

,T
db
	​

)

This ensures a safe and code-compliant design.

🧪 Testing Strategy (PyTest)

The project uses PyTest to validate both individual checks and overall behavior.

✔ Unit Tests

Gross section yielding

Net section rupture

Block shear strength

Invalid input handling (negative areas, invalid values)

✔ Integration Test

Ensures the minimum (governing) capacity is correctly identified

✔ Edge Cases

Very small areas

Invalid geometrical inputs

Block shear governing over yielding/rupture

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

▶️ How to Run
1️⃣ Activate virtual environment
venv\Scripts\activate

2️⃣ Run only tension member tests
python -m pytest tests\tension\test_tension_bolted.py -v

3️⃣ Run full test suite
python -m pytest -v

✅ Sample Output
collected 8 items
8 passed in 0.04s

🎯 Why This Work Is Relevant to Osdag / FOSSEE

Closely follows IS 800:2007 clauses

Modular design compatible with Osdag’s architecture

Strong emphasis on test-driven validation

Demonstrates ability to convert structural design theory → reliable software

Easy to extend to:

Welded tension members

Compression members

Connection design modules

🚀 Possible Extensions

Add compression member buckling curves (IS 800 Cl. 7)

Add welded tension member checks

Add coverage reporting using pytest-cov

Integrate with Osdag section property database

Automate design optimization loops

👤 Author

Gurujukota Gowri Nandhan
B.Tech – Computer Science (AI & ML)
Interest Area: Engineering Software Development & Testing
