#!/bin/bash

# Configurar colores para la salida
GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[31m"
RESET="\e[0m"

echo -e "${YELLOW}🚀 Iniciando backend y frontend...${RESET}"

# Ir al backend y activarlo
cd backend || { echo -e "${RED}Error: No se encontró la carpeta backend.${RESET}"; exit 1; }

# Activar el entorno virtual y correr Flask
echo -e "${GREEN}🟢 Iniciando backend Flask en http://127.0.0.1:5000...${RESET}"
source venv/bin/activate
python run.py &
BACKEND_PID=$!
deactivate
cd ..

# Ir al frontend y activarlo
cd frontend || { echo -e "${RED}Error: No se encontró la carpeta frontend.${RESET}"; exit 1; }

echo -e "${GREEN}🟢 Iniciando frontend Vue en http://localhost:5173...${RESET}"
npm run dev &
FRONTEND_PID=$!
cd ..

# Mensaje final
echo -e "${YELLOW}✨ El proyecto está corriendo. Presiona Ctrl+C para detenerlo.${RESET}"

# Capturar Ctrl+C para cerrar los procesos correctamente
trap "echo -e '\n${RED}🛑 Deteniendo backend y frontend...${RESET}'; kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT

# Mantener el script activo
wait
