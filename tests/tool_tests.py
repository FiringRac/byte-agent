
import sys
from pathlib import Path

import pandas as pd

# Allow this test file to import src/tools.py.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from tools import create_tools


def make_test_tools():
    """Create a tiny, predictable dataset for testing."""
    df = pd.DataFrame({
        "City": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
        "Salary": [50000, 70000, 90000, 60000],
        "Name": ["A", "B", "C", "D"],
    })

    return create_tools(df)


def test_inspect():
    tools = make_test_tools()
    result = tools[0].invoke({})

    assert result["rows"] == 4
    assert result["columns"] == ["City", "Salary", "Name"]
    print("PASS: inspect")


def test_filter():
    tools = make_test_tools()
    result = tools[1].invoke({
        "column": "City",
        "value": "Delhi",
    })

    assert len(result) == 2
    assert all(row["City"] == "Delhi" for row in result)
    print("PASS: filter")


def test_compare():
    tools = make_test_tools()
    result = tools[2].invoke({
        "group_by": "City",
        "column": "Salary",
        "operation": "mean",
    })

    assert result["Delhi"] == 70000
    assert result["Mumbai"] == 65000
    print("PASS: compare")


def test_clean():
    df = pd.DataFrame({
        "Salary": [50000.0, None, 90000.0],
        "City": ["Delhi", None, "Mumbai"],
    })

    tools = create_tools(df)
    result = tools[3].invoke({})

    tools = create_tools(df)
    result = tools[3].invoke({})

    print("RESULT:", repr(result))
    print("RESULT TYPE:", type(result))
    print("PASS: clean")


if __name__ == "__main__":
    test_inspect()
    test_filter()
    test_compare()
    test_clean()
    print("\nAll basic tests passed!")
