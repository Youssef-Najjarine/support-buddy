from support_buddy.router import classify_problem

def test_classify_stress():
    assert classify_problem("I feel anxious about everything") == "stress"

def test_classify_relationship():
    assert classify_problem("My girlfriend and I had a fight") == "relationship"

def test_classify_career():
    assert classify_problem("I have a job interview tomorrow") == "career"
