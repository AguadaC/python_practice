# Exception Handling in Python

This Python module illustrates how exceptions propagate through "except/raise" blocks or when they are left uncaught. The goal is to demonstrate different approaches to exception handling in Python and how they affect the program flow.

## Custom Exception Classes

In this module, we have defined a custom exception class called `ErrorException`. This exception is used as an example to show how custom exceptions can be raised and caught.

## Intermediate Functions

We have created a function called `generator_of_exceptions` that attempts to convert a string into an integer. If the conversion fails, it raises a `ValueError`. Additionally, if the resulting integer is less than 10, it raises an `ErrorException`.

## Main Functions

1. `function_with_raise(number: Union[str, int]) -> None`: This function calls `generator_of_exceptions` with the given number, catches any exception raised, and re-raises it. If an `ErrorException` is caught, it is re-raised.

2. `function_raise_exception(number: Union[str, int]) -> None`: This function also calls `generator_of_exceptions` with the given number, but it catches and raises a new `Exception` regardless of the original exception. If an `ErrorException` is caught, it is re-raised as a new `Exception`.

3. `function_without_try_except(number: Union[str, int]) -> None`: This function simply calls `generator_of_exceptions` with the given number without using `try/except` blocks.

## Main Function "main"

The `main` function is the entry point of the module and shows how the functions behave when passed the input "Hi" or the number 2. The goal is to compare the results in terms of caught and raised exceptions.

## Module Execution

To execute the module, simply run the main script from the command line. The results will be printed in the console, showing the caught and raised exceptions based on the different inputs provided.

It is important to understand how exceptions propagate and how to properly catch them to handle unexpected situations in our programs. Proper exception handling improves the robustness and reliability of our applications, which is essential for developing high-quality software.

---

# Manejo de Excepciones en Python

Este módulo de Python ilustra cómo se mueven las excepciones a partir de los bloques "except/raise" o cuando no se capturan. El objetivo es mostrar diferentes enfoques para el manejo de excepciones en Python y cómo afectan el flujo del programa.

## Clases de Excepciones Personalizadas

En este módulo, hemos definido una clase de excepción personalizada llamada `ErrorException`. Esta excepción se utiliza como ejemplo para demostrar cómo se pueden levantar y capturar excepciones personalizadas.

## Funciones Intermedias

Hemos creado una función llamada `generator_of_exceptions` que intenta convertir una cadena en un número entero. Si la conversión falla, levanta una excepción `ValueError`. Además, si el número entero resultante es menor que 10, levanta una excepción `ErrorException`.

## Funciones Principales

1. `function_with_raise(number: Union[str, int]) -> None`: Esta función llama a `generator_of_exceptions` con un número dado, y captura y vuelve a levantar cualquier excepción. Si se captura una `ErrorException`, se vuelve a levantar.

2. `function_raise_exception(number: Union[str, int]) -> None`: Esta función también llama a `generator_of_exceptions` con un número dado, pero captura y levanta una nueva excepción `Exception` sin importar la excepción original. Si se captura una `ErrorException`, se vuelve a levantar una excepción `Exception`.

3. `function_without_try_except(number: Union[str, int]) -> None`: Esta función simplemente llama a `generator_of_exceptions` con un número dado, sin usar bloques `try/except`.

## Función Principal "main"

La función `main` es el punto de entrada del módulo y muestra cómo se comportan las funciones mencionadas anteriormente cuando se les pasa un argumento de entrada "Hi" o el número 2. El objetivo es comparar los resultados en términos de excepciones capturadas y excepciones levantadas.

## Ejecución del Módulo

Para ejecutar el módulo, simplemente ejecute el script principal desde la línea de comandos. Los resultados se imprimirán en la consola, mostrando las excepciones capturadas y levantadas en función de las diferentes entradas proporcionadas.

Es importante entender cómo se propagan las excepciones y cómo capturarlas adecuadamente para manejar situaciones inesperadas en nuestros programas. El manejo adecuado de excepciones mejora la robustez y fiabilidad de nuestras aplicaciones, lo que es fundamental para el desarrollo de software de alta calidad.

