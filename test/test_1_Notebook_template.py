from testbook import testbook

@testbook('1_Notebook_template.ipynb', execute=True)
def test_func_sum_10(tb):
    func_sum = tb.ref('func_sum')
    assert func_sum(5,5) == 10

@testbook('1_Notebook_template.ipynb', execute=True)
def test_func_sum_any(tb):
    func_sum = tb.ref('func_sum')
    assert func_sum(3,5) == 8

@testbook('1_Notebook_template.ipynb', execute=True)
def test_function_f(tb):
    function_f = tb.ref('function_f')
    assert function_f(2) == 5