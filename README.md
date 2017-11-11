## En Construcción ...

# DNI Code Generator
Genera el código OCR del reverso del DNIe y DNI a partir de los datos:
- Número de serie del soporte (solo en el caso del DNI electrónico)
- Número de DNI o NIE
- Fecha de nacimiento
- Fecha de expiración del documento

Datos opcionales:
- Sexo ("M" por defecto)
- Nacionalidad ("ESP" por defecto)
- País ("ESP" por defecto)
- Tipo de Documento ("ID" por defecto)

## Funcionamiento
El programa calcula los hashes de los datos proporcionados, ordena todos los datos y finalmente da como salida el código exacto reflejado en el reverso del DNI y DNIe españoles.

## Ejemplo de uso:
- Datos dados:
  - Número de serie:      ABC456789
  - Número DNI:           12345678A
  - Fecha de nacimiento:  07/11/1999
  - Fecha de expiración:  31/12/2025
  
- Utilización DNIe:
```
print(DNIeCodeGenerator("ABC456789", "12345678A", "991107", "251231"))
```
- Salida DNIe:
```
IDESPABC456789612345678A<<<<<<
9911075M2512314ESP<<<<<<<<<<<2
```
- Utilización DNI antiguo:
```
print(DNICodeGenerator("12345678A", "991107", "251231"))
```
- Salida DNI viejo:
```
IDESP12345678A8<<<<<<<<<<<<<<<
9911075M2512314ESP<<<<<<<<<<<4
```
## Mejoras realizadas:
- Añadido soporte para NIE
- Cálculo automático de la letra del DNI; es decir, en el campo del número del DNI se puede dar con o sin letra
- Añadidas funciones de validación para todos los campos computables generando ValueError en caso de no ajustarse al formato correcto.

## En construcción ...
