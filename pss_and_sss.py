def generate_pss(N_id_2):
    x = [0, 1, 1, 0, 1, 1, 1]

    for i in range(7, 127):
        x.append((x[i - 3] + x[i - 7]) % 2)

    m = [(n + 43 * N_id_2) % 127 for n in range(127)]
    
    pss = [(1 - 2 * x[_m]) for _m in m]

    return pss

def generate_sss(N_id_1, N_id_2):
    x_0 = [1, 0, 0, 0, 0, 0, 0]
    x_1 = [1, 0, 0, 0, 0, 0, 0]

    for i in range(7, 127):
        x_0.append((x_0[i - 3] + x_0[i - 7]) % 2)
        x_1.append((x_1[i - 6] + x_1[i - 7]) % 2)

    m_0 = 15*(N_id_1//112) + 5*N_id_2
    m_1 = N_id_1 % 112

    sss = [(1-2*x_0[(n+m_0)%127])*(1-2*x_1[(n+m_1)%127]) for n in range(127)]

    return sss

if __name__ == "__main__":
    for n_2 in range(3):
        print(f"PSS for N_id_2 = {n_2}: ", generate_pss(n_2))

    for n_1 in range(336):
        for n_2 in range(3):
            pci = 3*n_1 + n_2
            print(f"PCI = {pci}, PSS = {n_2}, SSS for N_id_1 = {n_1}: ", generate_sss(n_1, n_2))
