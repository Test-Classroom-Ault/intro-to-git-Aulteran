import assign_to_student

def test_assign_to_student():
    try:
        # these two assertions are the actual tests
        assert assign_to_student.submission(2) == 4 
        assert assign_to_student.submission(-1) == -2
        print("All Tests Passed") # print statements should appear in "actions" tab
    except:
        raise Exception("Tests Failed")

    # if you want to specify what testcase failed,
    #  you can create separate try/except clauses with other exceptions
    # ==OR== create a list "testcases" with tuples as such: (input, output)
    # then create a for loop around the try/except and run each testcase through it
