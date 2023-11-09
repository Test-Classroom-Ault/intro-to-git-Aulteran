import assign_to_student

def test_assign_to_student():
    assert assign_to_student.submission(2) == 4
    assert assign_to_student.submission(-1) == -2
