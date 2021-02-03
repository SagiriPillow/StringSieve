======
StringSieve

__SourceCode__:    [GitHub] (https://github.com/UnknownMistyRain/StringSieve)
__License__:     [MIT] (https://github.com/UnknownMistyRain/StringSieve/blob/master/LICENSE)

#What is it ?

It is a module that it can filter the string by template and save it to dict.

#How can I use it ?

1.Import this module

.. code:: python

    import stringsieve

2.Set up a template

.. code:: python

    template = 'Hi! I am %name%, I can %capacity%!'

3.Create a string for filtering

.. code:: python

    string = 'Hi! I am Unknown Misty Rain, I can make programs!'

4.Use the provided methods to filter

.. code:: python

    filtrated = stringsieve.sieve(string, template, '%')

5.Print the result

.. code:: python

    print(filtrated)

6.Returned

.. code:: python

    {'name'='Unknown Misty Rain', 'capacity':'make programs'}
