# Examen de selección

## Notas
Autor: Joaquín Fernando Ortega Silva
SO: Windows 10
Entorno virtual: Anaconda 3 ('base':conda)
Versión de python: 3.9.7 64-bit
Usar formato Black

Versión actual de Black:  22.1.0

`pip install --upgrade black`

Alt+96 para acento inverso / backtick

Versión anterior de Pandas: 1.3.4
Versión actual de Pandas: 1.4.1

Versión de anterior matplotlib: 3.4.3
Versión actual de matplotlib: 3.5.1

Se instalo *mypy* 
Trabajando en "branch-1"

Estoy trabajando en pollos_petrel/dummy_model.py

Las unidades de longitud son *mm* y las de masa con *g*

### Definiciones:
- Tarso: es un hueso de la parte inferior de la pata de las aves
- Stub: Un stub es, en el contexto del testeo del software, un trozo de código usado como sustituto de alguna otra funcionalidad. Un stub puede simular el comportamiento de código existente o ser el sustituto temporal para un código aún no desarrollado

- linting: In computer programming lint or lint-like tools performing static analysis of source code checking for symantec discrepancies
Mypy and flake8 are linting tools

## Análisis del problema
___
Queda pendiente reoslver cuales son la sunideades de longitud y masa.
En el archivo *tain.csv* tenemos las siguientes categorias, donde target sepresenta el número de días:

>-id,Masa,Longitud_tarso,Longitud_ala,Longitud_pico Longitud_pluma_interior_de_la_cola,Longitud_pluma_exterior_de_la_cola,target
## Conflictos
- ~~Cada que corro *dummy_model.py* me cambia el directorio de trabajo.~~
- Hay que tener cuidado de no modificar la función write_submissions puesto que se usa en /src y en github actions para validar el codigo
- ¿Como usar los comandos make?/¿Como correr un Makefile?
    - **How to run a makefile in Windows?** Ver [esto](https://stackoverflow.com/questions/2532234/how-to-run-a-makefile-in-windows#:~:text=First%20step%3A%20download%20mingw32%2Dmake,directory%20where%20makefile%20is%20located.)

    

    [] Primero instalar [chocolatey](https://chocolatey.org/install)
[] En la terminal como admin 
`choco install make`

- *skipping analyzing "pandas": module is installed, but missing library stubs or py.typed marker* 
    - Este problema se puede deber a que no tiene *Type Hints* como se describe en este [artículo](https://skeptric.com/python-type-stubs/).
    - [How mypy handles imports](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)
    
    
    - [Missing library stubs or py.typed marker](https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports)
        - >Mypy will not try inferring the types of any 3rd party libraries you have installed unless they either have declared themselves to be PEP 561 compliant stub package (e.g. with a py.typed file) or have registered themselves on typeshed, the repository of types for the standard library and some 3rd party libraries


    En algunos casos actualizar los modulos, hace que se incluyan - pero en este caso no me funciono actulizarlo solamente.
    - *[Type hinting](https://blog.jetbrains.com/pycharm/2015/11/python-3-5-type-hinting-in-pycharm-5/)*: 
    >...you only need to stub the methods you actually use, and the task is manageable. Trying to annotate the whole warcio codebase is quite a task, although this approach gets you a long way
    - **Writing Stubs**... creating a [stub](https://mypy.readthedocs.io/en/stable/stubs.html#stub-files)
    " stub files (.pyi files)"

    - He intentado descargar los stubs stubs para matplotlib, numy y pandas con la siguiente instrucción

        `pip install data-science-types`
    
        de [aquí](https://pypi.org/project/data-science-types/).
        
        Tras implementar esto y ejecutar: 
        
        `mypy /dummy_model.py`

        ocurrieron más errores pero únicamente sobre los datos de **pandas**, matplotlib ya no dio problemas por ahora.
    

    
_____
### Más sobre Pandas
 
`(base) PS C:\Users\Fernando\Desktop\GECI-Seleccion_analista\seleccion_analista_2022_JFOS> mypy pollos_petrel\dummy_model.py`
> pollos_petrel\dummy_model.py:57:    error: Module has no attribute "__version__"
pollos_petrel\dummy_model.py:72: error: "Series[Any]" not callable


## Pendiente
- Hacer un *script* para generar *JFOS_submission* al final, de manera que pase las pruebas.
## Anexos
____
- [Análisis Exploratorio de Datos](https://islas.dev/2018/06/28/analisis-exploratorio)

**Diponibilidad de datos:** Tabla donde cada renglón representa una categoría y las columnas son: nombre de la categoría, cantidad de datos, promedio, desviación estándar y resumen de 5 números
- [How to install and use "make" in Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
### Resumen de 5 numeros
1. Sample minimum
2. Lower quartile 
3. Median
4. Upper quartile
5. Sample maximum
____
1. Control Chart:
>The control chart is a graph used to study how a process changes over time. Data are plotted in time order. A control chart always has a central line for the average, an upper line for the upper control limit, and a lower line for the lower control limit.

2. Histogram:

>A frequency distribution shows how often each different value in a set of data occurs. A histogram is the most commonly used graph to show frequency distributions. It looks very much like a bar chart, but there are important differences between them


