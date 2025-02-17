<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { backgroundMusic } from '@/utils/sounds';

backgroundMusic.play();
const router = useRouter();
const showLetter = ref(true);
const showMenu = ref(false);

const closeLetter = () => {
  showLetter.value = false;
  showMenu.value = true;
};

const goToSlotMachine = () => {
  router.push('/slot-machine');
};

// Ajustar contenido al tamaño de la ventana
const resizeHandler = () => {
  document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`);
};

onMounted(() => {
  resizeHandler();
  window.addEventListener('resize', resizeHandler);

  // Verifica si se regresa desde slot-machine
  if (router.currentRoute.value.query.fromMenu) {
    showLetter.value = false;
    showMenu.value = true;
  }
});
</script>

<template>
  <div class="background">
    <div class="clouds">
      <div class="cloud cloud-1"></div>
      <div class="cloud cloud-2"></div>
      <div class="cloud cloud-3"></div>
    </div>

    <!-- Carta de bienvenida -->
    <div v-if="showLetter" class="overlay" @click="closeLetter">
      <div class="letter" @click.stop>
        <h1>
        <img src="@/assets/letter_basic.png" alt="Prize Icon" class="title-icon" /> 
        Feliz San Valentín 
        <img src="@/assets/letter_basic.png" alt="Prize Icon" class="title-icon" />
        </h1>
        <p>Te he preparado un pequeño regalo. He querido ponerme un poco en tus zapatos.</p>
        <p>Me sigue pareciendo un terror hacer front pero pensar en ti mientras lo hacía me ha encantado.</p>
        <p>Espero que te guste.</p>
        <p>Te quiero,</p>
        <p>J</p>

        <button @click="closeLetter">Siguiente ➡</button>
      </div>
    </div>

    <!-- Menú principal -->
    <div v-if="showMenu" class="menu">
      <h1>Planner Selector</h1>
      <button @click="goToSlotMachine">Start</button>
      <button>More</button>
      <button>Exit</button>
    </div>
  </div>
</template>


