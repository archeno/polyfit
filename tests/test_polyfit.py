import sys, os
import numpy as np
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from fy_polyfit.polyfit import PolyfitLinear, PolyfitQuadratic

def test_polyfit():
    x = np.array([1, 2, 3, 4, 5])
    y = 2 * x + 1 + np.random.uniform(-0.5, 0.5, size=x.shape)
    
    # 调用 PolyfitLinear
    coefficients = PolyfitLinear(x, y)
    
    # 期望的系数
    expected_coefficients = np.polyfit(x, y, 1)
    
    # 断言系数接近期望值
    np.testing.assert_almost_equal(coefficients, expected_coefficients, decimal=2)

def test_polyfit_quadratic():
    # 示例数据
    x = np.array([1, 2, 3, 4, 5])
    y = 3 * x**2 + 2 * x + 1 + np.random.uniform(-1, 1, size=x.shape)
    
    # 调用 PolyfitQuadratic
    coefficients = PolyfitQuadratic(x, y)
    
    # 期望的系数
    expected_coefficients = np.polyfit(x, y, 2)
    
    # 断言系数接近期望值
    np.testing.assert_almost_equal(coefficients, expected_coefficients, decimal=2)


if __name__ == "__main__":
    pytest.main()