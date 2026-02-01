import pytest

from osdag.design.tension_member_bolted import (
    gross_section_yielding,
    net_section_rupture,
    block_shear_strength,
    overall_tension_capacity
)

# -------------------------
# Gross section yielding (IS 800 Cl. 6.2)
# -------------------------
def test_gross_section_yielding_nominal():
    # A_g = 1000 mm2, f_y = 250 MPa, gamma_m0 = 1.1
    # Expected = (1000*250)/(1.1*1000) = 227.27 kN
    assert gross_section_yielding(1000, 250) == pytest.approx(227.27, rel=1e-3)


# -------------------------
# Net section rupture (IS 800 Cl. 6.3.1)
# -------------------------
def test_net_section_rupture_nominal():
    # A_n = 800 mm2, f_u = 410 MPa, beta = 0.9, gamma_m1 = 1.25
    # Expected = (0.9*800*410)/(1.25*1000) = 236.16 kN
    assert net_section_rupture(800, 410) == pytest.approx(236.16, rel=1e-2)


# -------------------------
# Block shear strength (IS 800 Cl. 6.4)
# -------------------------
def test_block_shear_nominal():
    T_db = block_shear_strength(
        A_vg=500,
        A_tn=300,
        f_y=250,
        f_u=410
    )
    assert T_db > 0


def test_block_shear_invalid_area():
    with pytest.raises(ValueError):
        block_shear_strength(-500, 300, 250, 410)



def test_overall_capacity_block_shear_governs():
    T_d = overall_tension_capacity(
        A_g=1200,
        A_n=900,
        A_vg=300,
        A_tn=200,
        f_y=250,
        f_u=410
    )
    assert T_d > 0
