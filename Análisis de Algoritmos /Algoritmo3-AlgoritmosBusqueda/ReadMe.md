## Programa de Visualización de Algoritmos de Ordenamiento

### Descripción
Este programa implementa y visualiza tres algoritmos de ordenamiento con detalle paso a paso:
1. **Inserción Local** (Local Insertion Sort)
2. **Ordenamiento de Árbol** (Tree Sort)
3. **Radix LSD Sort** (para valores hexadecimales)

Muestra cada operación intermedia durante el proceso de ordenamiento, permitiendo observar cómo los algoritmos transforman los datos.

---

### Requisitos
- Python 3.x

---

### Uso
```bash
python Ordenamiento.py
```
Siga las instrucciones interactivas:
1. Seleccione algoritmo (1-3)
2. Ingrese datos según el algoritmo:
   - **Algoritmos 1-2**: Enteros separados por espacios (ej: `5 3 8 1`)
   - **Algoritmo 3**: Valores hexadecimales de hasta 2 dígitos (ej: `A3 1F 2B`)
3. Analice los pasos detallados
4. Repita con otra secuencia (s/n)

---

### Algoritmos Implementados

#### 1. Inserción Local (`ordenamiento_insercion`)
```mermaid
graph LR
    A[Estado inicial] --> B[Seleccionar elemento]
    B --> C[Comparar con elementos anteriores]
    C --> D[Desplazar elementos mayores]
    D --> E[Insertar en posición correcta]
    E --> F[Repetir para siguiente elemento]
```
- **Complejidad**: O(n²)
- **Visualización**: Muestra cada movimiento e inserción

#### 2. Ordenamiento de Árbol (`ordenar_arbol`)
```mermaid
graph TB
    A[Elementos] --> B[Construir ABB]
    B --> C[Recorrido in-order]
    C --> D[Secuencia ordenada]
    
    subgraph ABB
        B1[Insertar 5] --> B2[Insertar 3]
        B2 --> B3[Insertar 8]
        B3 --> B4[Insertar 1]
    end
```
- **Complejidad**: O(n log n) promedio
- **Visualización**: Registra cada inserción y visita durante el recorrido

#### 3. Radix LSD Sort (`ordenamiento_radix_lsd`)
```mermaid
graph LR
    A[Elementos] --> B[Identificar dígito LSD]
    B --> C[Counting Sort por dígito]
    C --> D[Mover a MSD]
    D --> E[Repetir para cada dígito]
```
- **Complejidad**: O(n * k) (k = longitud máxima)
- **Visualización**: Muestra conteo, acumulación y ordenamiento por cada dígito

---

### Componentes del Código
| Función | Descripción |
|---------|-------------|
| `NodoArbol` | Nodo para árbol binario |
| `insertar` | Inserta en ABB y registra pasos |
| `recorrido_en_orden` | Recorrido in-order con registro |
| `ordenar_arbol` | Implementa Tree Sort |
| `ordenamiento_insercion` | Implementa Inserción Local |
| `ordenamiento_cuenta` | Counting Sort para Radix |
| `ordenamiento_radix_lsd` | Implementa Radix LSD |
| `imprimir_pasos` | Muestra pasos enumerados |
| `main` | Interfaz de usuario principal |

---

### Ejemplos de Salida

### Inserción Local (entrada: `5 3 8 1`)

![Vista del Programa al eligir Inserción Local y ejecutarlo](/Análisis%20de%20Algoritmos%20/Algoritmo3-AlgoritmosBusqueda/Images/InsercionLoc.png)


#### Tree Sort (entrada: `5 3 8 1`)

![Vista del Programa al eligir Tree Sort y ejecutarlo](/Análisis%20de%20Algoritmos%20/Algoritmo3-AlgoritmosBusqueda/Images/OrdArb.png)


#### Radix LSD (entrada: `A3 1F 2B`)

![Vista del Programa al eligir Tree Sort y ejecutarlo](/Análisis%20de%20Algoritmos%20/Algoritmo3-AlgoritmosBusqueda/Images/Radix.png)
 
---

### Características Clave
1. **Visualización detallada**:
   - Cada operación se registra y numera
   - Explicaciones claras de cada paso
   - Estado actual del arreglo en puntos clave

2. **Validación de entradas**:
   - Verificación de hexadecimales en Radix Sort
   - Manejo de errores en selección de algoritmo

3. **Interfaz interactiva**:
   - Menú intuitivo
   - Posibilidad de múltiples ejecuciones
   - Mensajes de error descriptivos

---

### Limitaciones
1. **Radix LSD**:
   - Solo acepta valores hexadecimales (0-9, A-F)
   - Longitud máxima de 2 caracteres
   - No soporta minúsculas (usar mayúsculas)

2. **Tree Sort**:
   - Implementación con árbol no balanceado
   - Rendimiento degradado con secuencias ordenadas

3. **Tipos de datos**:
   - Inserción y Tree Sort solo para enteros
   - Radix solo para cadenas hexadecimales


---

### Conclusión
Este programa ofrece una herramienta para comprender el funcionamiento interno de tres algoritmos de ordenamiento fundamentales mediante la visualización detallada de cada paso del proceso. Su diseño sencillo y explicaciones claras lo hacen ideal para fines didácticos y de aprendizaje.