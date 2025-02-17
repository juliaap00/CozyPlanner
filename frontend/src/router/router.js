import { createRouter, createWebHistory } from 'vue-router';
import Menu from '../components/Menu.vue';
import SlotMachine from '../components/SlotMachine.vue'; // Importamos SlotMachine.vue

const routes = [
  {
    path: '/',
    name: 'home',
    component: Menu,
  },
  {
    path: '/slot-machine',
    name: 'slotMachine',
    component: SlotMachine, // Nueva ruta para la máquina tragamonedas
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
