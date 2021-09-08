def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([]) == None

def range_overlap(ranges):
    """Return common overlap among a set of [left, right] ranges."""
    if ranges == []:
        result = None
        return (result)
    else:
        max_left = min(ranges[0]) 
        min_right = max(ranges[0])
        for (left, right) in ranges:
            max_left = max(max_left, left)
            min_right = min(min_right, right)
        if max_left >= min_right:
            result = None
        else:
            result = (max_left, min_right)
        return (result)

test_range_overlap()
x = range_overlap([ (0, 2), (1, 5), (-1, 3)])
print(x)
