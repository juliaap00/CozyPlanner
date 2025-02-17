<script setup>
import { onMounted, onBeforeUnmount } from 'vue';
import { clickSound, backgroundMusic } from '@/utils/sounds'; // Asegúrate de importar tu sonido de clic

onMounted(() => {
  // Reproducir la música de fondo al montar el componente
  backgroundMusic.play();

  // Escuchar todos los clics en el documento
  const handleClick = (event) => {
    clickSound.play(); // Sonido al hacer clic
  };

  document.addEventListener('click', handleClick);

  onBeforeUnmount(() => {
    // Limpiar el event listener cuando el componente se destruya
    document.removeEventListener('click', handleClick);
  });
});
</script>

<template>
  <div>
    <router-view />
  </div>
</template>
