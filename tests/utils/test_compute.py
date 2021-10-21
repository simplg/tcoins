from app.utils.compute import sum


def test_sum():
    tests = [{
        "x": 2,
        "y": 0,
        "result": 2,
    },{
        "x": 2,
        "y": 0,
        "result": 2,
    },{
        "x": 2,
        "y": 0,
        "result": 2,
    },{
        "x": 2,
        "y": 0,
        "result": 2,
    }]
    for test in tests:
        assert sum(test["x"], test["y"]) == test["result"]