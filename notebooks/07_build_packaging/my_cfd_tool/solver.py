"""1-D steady heat conduction solver."""


def solve(k: float, L: float, T_left: float, T_right: float, n: int = 100) -> list[float]:
    """Solve 1-D steady conduction: d2T/dx2 = 0 with Dirichlet BCs.

    The exact solution is linear: T(x) = T_left + (T_right - T_left) * x / L.
    """
    if L <= 0:
        raise ValueError("Length must be positive")
    xs = [i * L / (n - 1) for i in range(n)]
    return [T_left + (T_right - T_left) * x / L for x in xs]
