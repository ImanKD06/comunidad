#  Community Manager

Plataforma full-stack para digitalizar y centralizar la gestión de comunidades de vecinos.

##  Sobre el proyecto

Community Manager nace de una idea sencilla: ¿por qué la gestión de una comunidad de vecinos sigue dependiendo tanto de Excel, WhatsApp, documentos y procesos manuales?

La plataforma centraliza en un único lugar la información relacionada con comunidades, vecinos, pagos, gastos, incidencias y reuniones, incorporando herramientas de Inteligencia Artificial para automatizar determinadas tareas.

## ✨ Funcionalidades

-  Gestión de comunidades
-  Gestión de vecinos
-  Gestión de pagos y cuotas
-  Gestión de gastos
-  Gestión y seguimiento de incidencias
-  Clasificación y priorización de incidencias mediante IA
-  Generación de actas mediante IA
- API REST para la comunicación entre frontend y backend

##  Tecnologías

### Frontend

- React
- Vite
- JavaScript
- React Router

### Backend

- Python
- FastAPI
- SQLAlchemy
- Mangum
- AWS Lambda
- AWS SAM

### Base de datos

- MySQL
- Aiven

### Inteligencia Artificial

- Modelo generativo de IA para generación de actas
- IA para análisis y clasificación de incidencias

### Despliegue

- Vercel — Frontend
- AWS Lambda — Backend
- AWS SAM — Infraestructura y despliegue
- Aiven — Base de datos

##  Arquitectura

```text
┌─────────────────┐
│    Frontend     │
│ React + Vite    │
│    Vercel       │
└────────┬────────┘
         │
         │ HTTP / REST API
         ▼
┌─────────────────┐
│     Backend     │
│ FastAPI         │
│ Mangum          │
│ AWS Lambda      │
└────────┬────────┘
         │
    ┌────┴─────┐
    ▼          ▼
┌─────────┐  ┌─────────────┐
│ MySQL   │  │     IA      │
│ Aiven   │  │ Generativa  │
└─────────┘  └─────────────┘
