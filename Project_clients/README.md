Proyecto FastAPI - Gestión de Clientes, Facturas y Transacciones
Este proyecto implementa una API con FastAPI organizada en módulos y routers para manejar clientes, facturas y transacciones.

Pasos realizados
1. Estructura del proyecto
Se organizó el proyecto en la carpeta app/ con subcarpetas para modelos y enrutador.

2. Creación de __init__.py
Se agregó __init__.py en app/, modelos/ y enrutador/ para que las carpetas sean reconocidas como paquetes de Python.

3. Routers con APIRouter
Se implementaron routers CRUD en enrutador/:

clientes.py → Endpoints para listar, crear, editar y eliminar clientes. Cada router se conecta en main.py mediante app.include_router(...).
4. Archivo requirements.txt
Se creó el archivo requirements.txt en la raíz del proyecto con las dependencias necesarias. Esto permite instalarlas con:

pip install -r requirements.txt
Ejecución
fastapi dev app/main.py
Documentación interactiva disponible en: http://127.0.0.1:8000/docs

🆕 Actualización — 1 de Julio de 2026
Conexión con base de datos — se preparó la estructura para integrar una base de datos real, reemplazando las listas en memoria.
Organización de módulos y enrutadores — se corrigió la estructura de imports entre modelos/ y enrutador/ para que cada paquete sea reconocido correctamente.
Corrección de errores — se resolvieron errores de importación causados por nombres inconsistentes entre archivos (factura vs facturas, Transaccion vs Transacciones).
Hecho por David Samuel Pérez — Ficha: 3407186