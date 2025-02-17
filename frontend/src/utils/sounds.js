class BackgroundMusic {
    constructor(src) {
        this.audio = new Audio(src);
        this.audio.loop = true;
        this.audio.volume = 0.5;  // Volumen por defecto
        this.isPlaying = false;
    }

    play() {
        if (!this.isPlaying) {
            this.audio.play()
                .then(() => {
                    this.isPlaying = true;
                })
                .catch(error => console.log("Error al reproducir audio:", error));
        }
    }

    stop() {
        this.audio.pause();
        this.isPlaying = false;
    }

    pause() {
        this.audio.pause();
        this.isPlaying = false;
    }

    resume() {
        if (!this.isPlaying) {
            this.audio.play()
                .then(() => {
                    this.isPlaying = true;
                })
                .catch(error => console.log("Error al reanudar la música:", error));
        }
    }

    setVolume(volume) {
        this.audio.volume = volume; // Cambia el volumen entre 0 y 1
    }
}

// Exportar una única instancia para toda la app
export const backgroundMusic = new BackgroundMusic("/assets/background.mp3");

class SoundEffect {
    constructor(src) {
        this.audio = new Audio(src);
        this.audio.volume = 0.5; // Ajusta volumen
    }

    play() {
        this.audio.currentTime = 0; // Reinicia el sonido si ya se estaba reproduciendo
        this.audio.play().catch(error => console.log("Error al reproducir sonido:", error));
    }
}

// Exportar el sonido para usarlo en los componentes
export const beepSound = new SoundEffect("/assets/beep.wav");
export const winningSound = new SoundEffect("/assets/winning2.wav");
export const coinSound = new SoundEffect("/assets/coin.wav");
export const paperSound = new SoundEffect("/assets/paper.wav");
export const clickSound = new SoundEffect("/assets/click.wav");




