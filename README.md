# ¿Qué es el modelo SIR?
Un modelo SIR es un tipo de modelo epidemiológico que predice el número de individuos que se infectarán con una enfermedad
contagiosa en una población cerrada a lo largo del tiempo. Se considera la base de los modelos dinámicos utilizados para el
estudio de las enfermedades infecciosas.  

Por tanto, si queremos saber cómo se propaga una enfermedad infecciosa en una población, el modelo SIR es una forma sencilla
de hacerlo utilizando matemáticas. Para ello se divide a la población en tres grupos:  

1. **S - Susceptibles:** Son las personas que están sanas pero que pueden contagiarse la enfermedad porque no tienen inmunidad.
Al principio de una epidemia, casi toda la población está en este grupo.

2. **I - Infectados:** Son las personas que están enfermas en ese momento y pueden contagiar a los Susceptibles.
   
3. **R - Recuperados/Removidos:** Son las personas que ya tuvieron la enfermedad y ahora son inmunes (no pueden volver a enfermarse ni contagiar),
   o lamentablemente fallecieron a causa de ella. En cualquier caso, ya no participan en la propagación. 

# ¿Cómo funciona el modelo?

El modelo SIR describe cómo las personas se mueven de un grupo a otro con el tiempo: 

+ **De S a I:** Una persona Susceptible (S) entra en contacto con una persona Infectada (I) y se contagia. Pasa entonces al grupo de 
Infectados (I). La velocidad a la que esto ocurre depende de cuántos infectados haya y qué tan contagiosa sea la enfermedad. 

+ **De I a R:** Una persona Infectada (I), después de un tiempo (la duración de la enfermedad), se recupera y desarrolla inmunidad 
(o fallece). Pasa entonces al grupo de Recuperados/Removidos (R). La velocidad a la que esto ocurre depende de cuánto tiempo dure la enfermedad en promedio. 

# Puntos Clave

**Simplificación:** Es un modelo básico. No considera cosas como nacimientos, muertes por otras causas, gente que entra o sale de la 
población, o que la inmunidad pueda desaparecer con el tiempo (aunque hay modelos más complejos que sí lo hacen). 

**Número Básico de Reproducción (R₀):** Un concepto muy importante relacionado con el modelo SIR es el R₀ (se lee "R sub cero"). 
Representa el número promedio de personas que una sola persona infectada contagiará si toda la población a su alrededor es susceptible.  

**Si R₀ > 1: La epidemia crecerá (cada enfermo contagia a más de una persona).**

**Si R₀ < 1: La epidemia se extinguirá por sí sola (cada enfermo contagia a menos de una persona).**

**Si R₀ = 1: La enfermedad se mantendrá estable (cada enfermo contagia justo a una persona).**

**Utilidad:** A pesar de ser simple, el modelo SIR ayuda a los epidemiólogos y a las autoridades de salud a:

+ Entender la dinámica general de una epidemia.
+ Predecir cuándo ocurrirá el "pico" de infecciones (el momento con más enfermos).
+ Estimar cuántas personas podrían enfermarse en total.
+ Evaluar el posible impacto de medidas de control (como la vacunación o el distanciamiento social, que buscan reducir la tasa de contagio y, por lo tanto, el R₀).
