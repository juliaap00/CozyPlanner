<script setup>
import { ref } from 'vue';
import axios from 'axios'; 
const showGif = ref(false);
const isRolling = ref(false);
const isWinning = ref(false);
const showCongrats = ref(false);
const showLetterBouncing = ref(false);
const showLetterOpening = ref(false);
const showPrizeCard = ref(false);
const showCoinSelection = ref(true);

const planDetails = ref({ title: "", description: "", icon: "", indoorOutdoor: "" });

const isCardVisible = ref(false);

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
    setTimeout(() => {
      isRolling.value = false;
      isWinning.value = true;
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
      title: response.data.titulo,
      description: response.data.descripcion,
      icon: response.data.icono,
      indoorOutdoor: response.data.indoor_outdoor
    };
  } catch (error) {
    console.error("Error en la solicitud:", error);
  }
};


const revealLetter = () => {
  showCongrats.value = false;
  showLetterBouncing.value = true;
};

const openLetter = () => {
  showLetterBouncing.value = false;
  showLetterOpening.value = true;
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
          <div class="coin-wrapper" @click="handleCoinClick('gold')" style="cursor: pointer;">
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
      <p>{{ displayedMessage }}</p>
      <p v-if="showContinueButton" class="continue-button" @click="revealLetter">▶ Continuar</p>
    </div>

    <!-- Animaciones de letra -->
    <div v-if="showLetterBouncing" class="overlay" @click="openLetter">
      <img src="@/assets/letter_bouncing.apng" class="letter-animation" />
    </div>
    <div v-if="showLetterOpening" class="overlay">
      <img src="@/assets/letter_opening.apng" class="letter-animation" />
    </div>

    <!-- Carta de premio -->
    <div v-if="isCardVisible" class="prize-card-overlay">
    <div class="prize-card container">
      <button class="close-btn" @click="closeCard">
    <span class="pixel-x">
        <span class="pixel top-left"></span>
        <span class="pixel top-right"></span>
        <span class="pixel bottom-left"></span>
        <span class="pixel bottom-right"></span>
    </span>
</button>
<div class="icono">
          <img :src="planDetails.icon" alt="Icono del plan" class="plan-icon" />
        </div>
        <div class="descripcion-plan">
          <h2>{{ planDetails.title }}</h2>
        </div>
        <div class="iconos-extra">
          <img v-if="selectedCoin === 'bronze'" src="@/assets/bronze_crop.png" class="tier-icon" />
          <img v-else-if="selectedCoin === 'silver'" src="@/assets/silver_crop.png" class="tier-icon" />
          <img v-else-if="selectedCoin === 'gold'" src="@/assets/gold_crop.png" class="tier-icon" />
          <img v-if="planDetails.indoorOutdoor === 'indoor' || planDetails.indoorOutdoor === 'both'" src="@/assets/house.png" class="location-icon" />
          <img v-if="planDetails.indoorOutdoor === 'outdoor' || planDetails.indoorOutdoor === 'both'" src="@/assets/tree.png" class="location-icon" />
        </div>
        <div class="descripcion-detallada">
          <p>{{ planDetails.description }}</p>
      </div>
    </div>
  </div>
    
  </div>
</template>

<style scoped>

</style>
