def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()
# Traceback (most recent call last):
#   File "C:\Users\danii\OneDrive\Рабочий стол\PY\homework\Urban\Others\namespaces\hw.py", line 7, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
