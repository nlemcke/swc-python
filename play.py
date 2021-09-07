def test_range_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None
    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)
    assert range_overlap([]) == None

def range_overlap(ranges):
    """Return common overlap among a set of [left, right] ranges."""
    for (left, right) in ranges:
        max_left = left
        min_right = right
        max_left = max(max_left, left)
        min_right = min(min_right, right)
    return (max_left, min_right)

test_range_overlap()

