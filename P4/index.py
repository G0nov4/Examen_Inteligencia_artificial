from kanren import Relation, facts, run, eq, var


padre = Relation()
madre = Relation()
abuelo = Relation()
tio = Relation()
primo = Relation()

facts(padre, ("Gonzalo","Gary"),("Gonzalo","Franco"),("Juan","Jorge"),("Juan","Melisa"),("Richard","Nicol"),("Luis","Nando"),("Luis","Jenny"),("Luis","Joan"),("Pedro","Ariana"),("Pedro","Briana"),("Marcelo","Clarivel"),("Marcelo","Mishel"),("Marcelo","Litzel"),)
facts(padre, ("Beatriz","Gary"),("Beatriz","Franco"),("Janneth","Jorge"),("Janneth","Melisa"),("Juana","Nicol"),("Lucy","Nando"),("Lucy","Jenny"),("Lucy","Joan"),("Gabriela","Ariana"),("Gabriela","Briana"),("Susana","Clarivel"),("Susana","Mishel"),("Susana","Litzel"))

facts(abuelo, ("Alberto","Gary"),("Alberto","Franco"),("Alberto","Jorge"),("Alberto","Melisa"),("Alberto","Nando"),("Alberto","Joan"),("Alberto","Jenny"));
facts(abuelo, ("Justina","Gary"),("Justina","Franco"),("Justina","Jorge"),("Justina","Melisa"),("Justina","Nando"),("Justina","Joan"),("Justina","Jenny"));

facts(tio, ("Juan","Gary"),("Luis","Gary"),("Pedro","Gary"),("Janneth","Gary"),("Jhovanna","Gary"),("Hilda","Gary"),("Lucy","Gary"),("Richard","Gary"),("Gabriela","Gary"),("Patricia","Gary"),("Susana","Gary"),("Marcelo","Gary"),("Claudio","Gary"),("Estela","Gary"))
facts(tio, ("Juan","Franco"),("Juan","Franco"),("Luis","Franco"),("Pedro","Franco"),("Janneth","Franco"),("Jhovanna","Franco"),("Hilda","Franco"),("Lucy","Franco"),("Richard","Franco"),("Gabriela","Franco"),("Patricia","Franco"),("Susana","Franco"),("Marcelo","Franco"),("Claudio","Franco"),("Estela","Franco"))
facts(tio, ("Luis","Jorge"),("Jhovanna","Jorge"),("Hilda","Jorge"),("Lucy","Jorge"),("Beatriz","Jorge"),("Gonzalo","Jorge"),)
facts(tio, ("Luis","Melisa"),("Jhovanna","Melisa"),("Hilda","Melisa"),("Lucy","Melisa"),("Beatriz","Melisa"),("Gonzalo","Melisa"))
facts(tio, ("Juan","Nando"),("Pedro","Nando"),("Jhovanna","Nando"),("Hilda","Nando"),("Janneth","Nando"),("Beatriz","Nando"),("Gonzalo","Nando"))
facts(tio, ("Juan","Joan"),("Pedro","Joan"),("Jhovanna","Joan"),("Hilda","Joan"),("Janneth","Joan"),("Beatriz","Joan"),("Gonzalo","Joan"))
facts(tio, ("Gabriela","Nicol"),("Patricia","Nicol"),("Susana","Nicol"),("Marcelo","Nicol"),("Claudio","Nicol"),("Estela","Nicol"))
facts(tio, ("Richard","Ariana"),("Patricia","Ariana"),("Susana","Ariana"),("Marcelo","Ariana"),("Claudio","Ariana"),("Estela","Ariana"))
facts(tio, ("Richard","Briana"),("Patricia","Briana"),("Susana","Briana"),("Marcelo","Briana"),("Claudio","Briana"),("Estela","Briana"))
facts(tio, ("Gabriela","Clarivel"),("Richard","Clarivel"),("Patricia","Clarivel"),("Claudio","Clarivel"),("Estela","Clarivel"))
facts(tio, ("Gabriela","Mishel"),("Richard","Mishel"),("Patricia","Mishel"),("Claudio","Mishel"),("Estela","Mishel"))
facts(tio, ("Gabriela","Litzel"),("Richard","Litzel"),("Patricia","Litzel"),("Claudio","Litzel"),("Estela","Litzel"))

facts(primo, ("Gary","Jorge"),("Gary","Melisa"),("Gary","Nicol"),("Gary","Nando"),("Gary","Jenny"),("Gary","Joan"),("Gary","Ariana"),("Gary","Briana"),("Gary","Clarivel"),("Gary","Mishel"),("Gary","Litzel"))
facts(primo, ("Franco","Jorge"),("Franco","Melisa"),("Franco","Nicol"),("Franco","Nando"),("Franco","Jenny"),("Franco","Joan"),("Franco","Ariana"),("Franco","Briana"),("Franco","Clarivel"),("Franco","Mishel"),("Franco","Litzel"))
facts(primo, ("Nicol","Gary"),("Nicol","Franco"),("Nicol","Ariana"),("Nicol","Briana"),("Nicol","Clarivel"),("Nicol","Mishel"),("Nicol","Litzel"))
facts(primo, ("Ariana","Gary"),("Ariana","Franco"),("Ariana","Nicol"),("Ariana","Briana"),("Ariana","Clarivel"),("Ariana","Mishel"),("Ariana","Litzel"))
facts(primo, ("Briana","Gary"),("Briana","Franco"),("Briana","Ariana"),("Briana","Nicol"),("Briana","Clarivel"),("Briana","Mishel"),("Briana","Litzel"))
facts(primo, ("Clarivel","Gary"),("Clarivel","Franco"),("Clarivel","Ariana"),("Clarivel","Briana"),("Clarivel","Nicol"),("Clarivel","Mishel"),("Clarivel","Litzel"))
facts(primo, ("Mishel","Gary"),("Mishel","Franco"),("Mishel","Ariana"),("Mishel","Briana"),("Mishel","Clarivel"),("Mishel","Nicol"),("Mishel","Litzel"))
facts(primo, ("Litzel","Gary"),("Litzel","Franco"),("Litzel","Ariana"),("Litzel","Briana"),("Litzel","Clarivel"),("Litzel","Mishel"),("Litzel","Nicole"))
facts(primo, ("Jorge","Gary"),("Jorge","Franco"),("Jorge","Nando"),("Jorge","Jenny"),("Jorge","Joan"))
facts(primo, ("Melisa","Gary"),("Melisa","Franco"),("Melisa","Nando"),("Melisa","Jenny"),("Melisa","Joan"))
facts(primo, ("Nando","Gary"),("Nando","Franco"),("Nando","Jorge"),("Nando","Melisa"))
facts(primo, ("Jenny","Gary"),("Jenny","Franco"),("Jenny","Jorge"),("Jenny","Melisa"))
facts(primo, ("Joan","Gary"),("Joan","Franco"),("Joan","Jorge"),("Joan","Melisa"))

# Definición de variables
X = var()
Y = var()
Z = var()

nombre = "Gary"

# Consultas
print(f"Padres de {nombre}")
print(run(0, X, padre(X, nombre)))

print(f"Hijos de {nombre}")
print(run(0, X, padre(nombre, X)))

print(f"Abuelos de {nombre}:")
print(run(0, X, abuelo(X, nombre)))

print(f"Tíos de {nombre}:")
print(run(0, X, tio(X, nombre)))

print(f"Primos de {nombre}:")
print(run(0, X, primo(nombre,X)))