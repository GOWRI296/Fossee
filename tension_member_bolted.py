def gross_section_yielding(A_g, f_y, gamma_m0=1.1):
    if A_g <= 0 or f_y <= 0:
        raise ValueError("Invalid gross section inputs")
    return (A_g * f_y) / (gamma_m0 * 1000)  # kN


def net_section_rupture(A_n, f_u, gamma_m1=1.25, beta=0.9):
    if A_n <= 0 or f_u <= 0:
        raise ValueError("Invalid net section inputs")
    return (beta * A_n * f_u) / (gamma_m1 * 1000)  # kN


def block_shear_strength(
    A_vg,
    A_tn,
    f_y,
    f_u,
    gamma_m0=1.1,
    gamma_m1=1.25
):
    if A_vg <= 0 or A_tn <= 0:
        raise ValueError("Invalid block shear areas")

    # IS 800 Cl. 6.4 – two block shear paths
    T_db1 = (A_vg * f_y) / (gamma_m0 * 1000) + (0.9 * A_tn * f_u) / (gamma_m1 * 1000)
    T_db2 = (0.9 * A_vg * f_u) / (gamma_m1 * 1000) + (A_tn * f_y) / (gamma_m0 * 1000)

    return min(T_db1, T_db2)


def overall_tension_capacity(
    A_g,
    A_n,
    A_vg,
    A_tn,
    f_y,
    f_u
):
    T_dg = gross_section_yielding(A_g, f_y)
    T_dn = net_section_rupture(A_n, f_u)
    T_db = block_shear_strength(A_vg, A_tn, f_y, f_u)

    return min(T_dg, T_dn, T_db)
