========
StringSieve
========
:SourceCode:    `GitHub <https://github.com/SagiriPillow/StringSieve>`

What is it ?
----
It is a module that it can filter the string by template and save it to dict.

How can I use it ?
----


1.Import this module

.. code:: python

    import stringsieve

2.Set up a template

.. code:: python

    template = 'Hi! I am %name%, I can %capacity%!'

3.Create a string for filtering

.. code:: python

    string = 'Hi! I am Sagiri Pillow, I can make programs!'

4.Use the provided methods to filter

.. code:: python

    filtrated = stringsieve.sieve(string, template, '%')

5.Print the result

.. code:: python

    print(filtrated)

6.Returned

.. code:: python

    {'name'='Sagiri Pillow', 'capacity':'make programs'}


