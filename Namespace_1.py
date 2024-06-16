def test_function():
    pass
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
print('-----------------')
#inner_function() # ОШИБКА 'name 'inner_function' is not defined.'
