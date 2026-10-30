"""
Test suite for sphere drag coefficient function.

This file contains the tests that are run by the pytest notebook.
The drag_coefficient function is defined in the notebook, but for
pytest to discover and run the tests, we need to import it here.
"""
import math
import pytest


def drag_coefficient(Re: float) -> float:
    """Drag coefficient of a smooth sphere vs. Reynolds number."""
    if Re <= 0:
        raise ValueError("Reynolds number must be positive")
    if Re < 1.0:
        return 24.0 / Re + 6.0 / (1.0 + math.sqrt(Re))
    if Re < 1000.0:
        return 24.0 / Re * (1.0 + 0.15 * Re**0.687)
    if Re < 2e5:
        return 0.47
    return 0.2


# Module-level reference data (used by parametrize)
REFERENCE_CASES = [
    (1e-3, 24000.0, 1e-3),   # Stokes regime
    (1.0, 27.6, 1e-2),       # Schiller-Naumann regime
    (1e5, 0.47, 1e-6),       # subcritical (classic value)
    (1e6, 0.2, 1e-6),        # supercritical
]


@pytest.fixture
def fluid():
    """Shared test data: air at 20 C, 1 atm (density, dynamic viscosity)."""
    return {"rho": 1.204, "mu": 1.825e-5}


def test_known_value_subcritical():
    """Cd = 0.47 for a sphere at Re = 1e5 (textbook value)."""
    assert drag_coefficient(1e5) == pytest.approx(0.47, abs=1e-6)


@pytest.mark.parametrize("Re, expected, tol", REFERENCE_CASES)
def test_correlation_matches_reference(Re, expected, tol):
    assert drag_coefficient(Re) == pytest.approx(expected, rel=tol)


def test_zero_reynolds_raises():
    with pytest.raises(ValueError):
        drag_coefficient(0.0)


def test_negative_reynolds_raises():
    with pytest.raises(ValueError):
        drag_coefficient(-5.0)


def test_fixture_is_available(fluid):
    """The fixture provides shared physical constants to any test."""
    assert fluid["rho"] > 0
    assert fluid["mu"] > 0
