# Proyecto Vue con Vite

Este proyecto está configurado con Vue.js y Vite para el desarrollo rápido y eficiente de aplicaciones web. A continuación, se explica la estructura del proyecto y cómo puedes modificar y añadir componentes.

## Estructura del Proyecto

```
.
├── vite.config.js         # Configuración de Vite
├── src/                   # Código fuente de la aplicación
│   ├── components/        # Componentes de Vue
│   ├── views/             # Vistas principales de la aplicación
│   ├── App.vue            # Componente raíz de la aplicación
│   ├── main.js            # Punto de entrada principal
│   └── router.js          # Configuración del enrutador (si aplica)
├── public/                # Archivos estáticos (imágenes, fuentes, etc.)
├── package.json           # Dependencias y scripts del proyecto
├── package-lock.json      # Registro de versiones exactas de paquetes
├── node_modules/          # Módulos de dependencias instaladas
├── index.html             # Archivo HTML principal
├── .vscode/               # Configuración opcional para VS Code
├── .gitignore             # Archivos y carpetas ignorados por Git
└── README.md              # Documentación del proyecto
```

## Descripción de Archivos Clave

- **vite.config.js**: Archivo de configuración de Vite.
- **src/**: Contiene el código fuente de la aplicación.
  - **components/**: Carpeta donde se encuentran los componentes reutilizables de Vue.
  - **views/**: Contiene las vistas principales de la aplicación.
  - **App.vue**: Componente raíz que gestiona toda la aplicación.
  - **main.js**: Punto de entrada donde se inicializa Vue y se monta en el DOM.
- **public/**: Almacena recursos estáticos que no se procesan por Vite.
- **package.json**: Lista las dependencias y los scripts del proyecto.
- **index.html**: Punto de entrada principal donde se monta la aplicación Vue.
- **node_modules/**: Contiene los paquetes instalados con npm o yarn.

## Cómo Modificar y Añadir Componentes

### 1. Modificar un Componente Existente
1. Dirígete a la carpeta `src/components/`.
2. Abre el archivo del componente que deseas modificar (por ejemplo, `MyComponent.vue`).
3. Edita la estructura HTML, la lógica de Vue (script) o los estilos CSS según sea necesario.

Ejemplo de componente:
```vue
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hola Mundo desde Vue!'
    };
  }
};
</script>

<style scoped>
div {
  color: blue;
}
</style>
```

### 2. Crear un Nuevo Componente
1. Dentro de `src/components/`, crea un archivo nuevo, por ejemplo, `NuevoComponente.vue`.
2. Define la estructura del componente en formato `.vue`.
3. Importa el componente en `App.vue` u otra vista para utilizarlo:

```vue
<script>
import NuevoComponente from './components/NuevoComponente.vue';

export default {
  components: {
    NuevoComponente
  }
};
</script>

<template>
  <div>
    <NuevoComponente />
  </div>
</template>
```

### 3. Ejecutar el Proyecto
Para ver los cambios en tu aplicación, asegúrate de ejecutar el proyecto con:

```sh
npm install  # Instala las dependencias si es la primera vez
npm run dev  # Inicia el servidor de desarrollo
```

Luego, abre el navegador en `http://localhost:5173/` (o el puerto indicado en la terminal).

---

Ahora tienes una idea clara de cómo funciona tu proyecto Vue con Vite y cómo puedes modificarlo. 🚀

