========
StringSieve
========
:SourceCode:    `GitHub <https://github.com/UnknownMistyRain/StringSieve>`
:License:     `MIT <https://github.com/UnknownMistyRain/StringSieve/blob/master/LICENSE>`

What is it ?
----
It is a module that it can filter the string by template and save it to dict.

How can I use it ?
----


1.Import this module

    import stringsieve

2.Set up a template

    template = 'Hi! I am *name*, I can *capacity*!'

3.Create a string for filtering

    string = 'Hi! I am Unknown Misty Rain, I can make programs!'

4.Use the provided methods to filter

    filtrated = stringsieve(string, template)

5.Print the result

    print(filtrated)
