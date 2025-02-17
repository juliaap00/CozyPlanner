<script setup>
import { ref } from 'vue';
import axios from 'axios'; 
import { useRouter } from 'vue-router';
import { beepSound, winningSound, coinSound } from '@/utils/sounds'; 
import { backgroundMusic } from '@/utils/sounds';

backgroundMusic.play();
backgroundMusic.setVolume(0.2);  // Llamar para comenzar la música de fondo

import { paperSound } from '../utils/sounds';

const router = useRouter();

const showGif = ref(false);
const isRolling = ref(false);
const isWinning = ref(false);
const showCongrats = ref(false);
const showLetterBouncing = ref(false);
const showLetterOpening = ref(false);
const showPrizeCard = ref(false);
const showCoinSelection = ref(true);

const planDetails = ref({
  title: "",
  description: "",
  materials: "",
  icon: "/prize.png", // 🔥 Valor predeterminado para evitar el error
  indoorOutdoor: ""
});


const isCardVisible = ref(false);

const fullMessage = "¡Enhorabuena, abre tu premio!";
const displayedMessage = ref(""); 
const showContinueButton = ref(false);

const selectedCoin = ref(null); // Variable global para almacenar la moneda seleccionada

const typeMessage = () => {
  let index = 0;
  const interval = setInterval(() => {
    if (index < fullMessage.length) {
      displayedMessage.value += fullMessage[index];
      index++;
    } else {
      clearInterval(interval);
      showContinueButton.value = true;
    }
  }, 50);
};

const selectCoin = () => {
  if (!selectedCoin.value) return; // Si no se ha seleccionado una moneda, no hace nada

  showCoinSelection.value = false;
  showGif.value = true;

  setTimeout(() => {
    showGif.value = false;
    isRolling.value = true;
    beepSound.play(); // Sonido de beep
    setTimeout(() => {
      isRolling.value = false;
      isWinning.value = true;
      
      // Reproducir el sonido winning
      winningSound.play();
      
      // Desvanecer el sonido durante 1.2 segundos
      let volume = 0.5; // Volumen inicial
      const fadeOutInterval = setInterval(() => {
        volume -= 0.05; // Reducir el volumen
        if (volume <= 0) {
          clearInterval(fadeOutInterval); // Detener el intervalo cuando el volumen llega a 0
          winningSound.audio.pause(); // Detener el sonido
          winningSound.audio.currentTime = 0; // Reiniciar el sonido
        } else {
          winningSound.audio.volume = volume; // Ajustar el volumen
        }
      }, 100); // Cambiar el volumen cada 100ms

      // Detener el sonido completamente después de 1.2 segundos
      setTimeout(() => {
        clearInterval(fadeOutInterval); // Limpiar el intervalo si se terminó el fade
        winningSound.audio.pause();
        winningSound.audio.currentTime = 0;
      }, 1300); // 1.2 segundos
       
      setTimeout(() => {
        showCongrats.value = true;
        displayedMessage.value = "";
        typeMessage();
      }, 2000);
    }, 3000);
  }, 1000);
};

const fetchPlan = async (tier) => {
  try {
    const response = await axios.get(`http://localhost:5000/plan_random?tier=${tier}`);
    if (response.data.error) {
      console.error("Error obteniendo el plan:", response.data.error);
      return;
    }
    planDetails.value = {
      title: response.data.titulo || "Sin título",
      description: response.data.descripcion || "Sin descripción",
      materials: response.data.materials || "No especificado",
      icon: response.data.icono && response.data.icono.trim() !== "" 
        ? `data:image/png;base64,${response.data.icono}`
        : "/prize.png",  // 🔥 Usa un valor por defecto si es vacío o no existe
      indoorOutdoor: response.data.indoor_outdoor || "No especificado"
    };
  } catch (error) {
    console.error("Error en la solicitud:", error);
  }
};

const goToSlotMachine = () => {
  router.push({ path: '/slot-machine', query: { fromMenu: true } });
};
const revealLetter = () => {
  showCongrats.value = false;
  showLetterBouncing.value = true;

};

const openLetter = () => {
  showLetterBouncing.value = false;
  showLetterOpening.value = true;
  paperSound.play()
  setTimeout(() => {
    showLetterOpening.value = false;
    showPrizeCard.value = true;
    isCardVisible.value = true;
  }, 2000);
};

const closeCard = () => {
  isCardVisible.value = false;
  // Reaparece el menú de selección de monedas al cerrar la carta
  showCoinSelection.value = true;
};

const handleCoinClick = async (coinType)=> {
  selectedCoin.value = coinType; // Establece la moneda seleccionada
  coinSound.play();
  console.log('Moneda seleccionada:', selectedCoin.value); // Puedes usar esto para depurar
  await fetchPlan(coinType);
  selectCoin(); // Llama a selectCoin después de hacer clic
};


</script>

<template>
  <div class="slot-machine-container">
    <!-- Menú de selección de monedas -->
    <div v-if="showCoinSelection" class="overlay">
      <div class="coin-selection-overlay">
        <div class="back-button" @click="router.push({ path: '/', query: { fromMenu: true } })">
          <img src="@/assets/back.png" alt="Back" />
        </div>
        <p class="coin-text">¡Selecciona una moneda!</p>
        <div class="coin-container">
          <div class="coin-wrapper" @click="handleCoinClick('bronze')" style="cursor: pointer;">
            <img src="@/assets/bronze_crop.png" class="coin" />
            <img src="@/assets/bronze_flipping_crop.apng" class="coin-hover" />
          </div>
          <div class="coin-wrapper" @click="handleCoinClick('silver')" style="cursor: pointer;">
            <img src="@/assets/silver_crop.png" class="coin" />
            <img src="@/assets/silver_flipping_crop.apng" class="coin-hover" />
          </div>
          <div class="coin-wrapper gold-coin" @click="" style="cursor:  not-allowed;">
            <img src="@/assets/gold_crop.png" class="coin" />
            <img src="@/assets/gold_flipping_crop.apng" class="coin-hover" />
          </div>
        </div>
      </div>
    </div>
    <div class="slot-machine">
    <transition name="fade">
    <img v-if="!showGif && !isRolling && !isWinning" src="@/assets/slot-machine.png" class="slot-image" key="default" />
    <img v-else-if="showGif" src="@/assets/slot_pull.apng" class="slot-image" key="pull" />
    <img v-else-if="isRolling" src="@/assets/slot-machine-roll.apng" class="slot-image" key="roll" />
    <img v-else-if="isWinning" src="@/assets/slot-machine-win.apng" class="slot-image" key="win" />
    </transition>
  </div>
    <!-- Mensaje de éxito -->
    <div v-if="showCongrats" class="congrats-overlay">
      <p class="congrats-text">{{ displayedMessage }}</p>
      <p v-if="showContinueButton" class="continue-button" @click="revealLetter">▶ Continuar</p>
    </div>

    <!-- Animaciones de letra -->
    <div v-if="showLetterBouncing" class="overlay" @click="openLetter">
      <img src="@/assets/letter_bouncing.apng" class="letter-animation" />
    </div>
    <div v-if="showLetterOpening" class="overlay">
      <img src="@/assets/letter_opening.apng" class="letter-animation" />
    </div>

    <div v-if="isCardVisible" class="prize-card-overlay">
  <div class="prize-card container">
    <div class="close-btn" @click="closeCard"></div>
    <div class="icono">
    <img v-if="planDetails.icon" :src="planDetails.icon" alt="Icono del plan" class="plan-icon" />

    </div>
    <div class="descripcion-plan">
      <h2 class="plan_title">{{ planDetails.title }}</h2>
    </div>
    <div class="iconos-extra">
      <img v-if="selectedCoin === 'bronze'" src="@/assets/bronze_crop.png" class="tier-icon" />
      <img v-else-if="selectedCoin === 'silver'" src="@/assets/silver_crop.png" class="tier-icon" />
      <img v-else-if="selectedCoin === 'gold'" src="@/assets/gold_crop.png" class="tier-icon" />
      <img v-if="planDetails.indoorOutdoor === 'indoor' || planDetails.indoorOutdoor === 'both'" src="@/assets/house.png" class="location-icon" />
      <img v-if="planDetails.indoorOutdoor === 'outdoor' || planDetails.indoorOutdoor === 'both'" src="@/assets/tree.png" class="location-icon" />
    </div>
    <div class="descripcion-detallada">
      <p class="plan_description" id="description">{{ planDetails.description }}
      <br><b>Materiales:</b> <br>{{ planDetails.materials }}</p>
    </div>
  </div>
</div>
  </div>
</template>
<script>
const description = document.getElementById("description");
description.innerHTML = description.innerHTML.replace(/\./g, '.<br>'); // Reemplaza cada punto por un salto de línea
</script>
<style>
.descripcion-detallada p {
  text-align: justify;
}

.plan_description {
  white-space: pre-line; /* Permite saltos de línea si hay \n en el contenido */
}
</style>
