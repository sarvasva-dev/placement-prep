/**
 * Focus Timer (Pomodoro & Stopwatch) Engine
 */

export class StudyTimer {
  constructor(displayElement, onTick, onComplete) {
    this.displayElement = displayElement;
    this.onTick = onTick;
    this.onComplete = onComplete;
    this.remainingSeconds = 25 * 60;
    this.initialDuration = 25 * 60;
    this.intervalId = null;
    this.isRunning = false;
  }

  setDuration(minutes) {
    this.stop();
    this.initialDuration = minutes * 60;
    this.remainingSeconds = this.initialDuration;
    this.render();
  }

  start() {
    if (this.isRunning) return;
    this.isRunning = true;
    this.intervalId = setInterval(() => {
      this.remainingSeconds--;
      this.render();
      if (this.onTick) this.onTick(this.remainingSeconds);

      if (this.remainingSeconds <= 0) {
        this.stop();
        if (this.onComplete) this.onComplete();
        this.playAlarm();
      }
    }, 1000);
  }

  pause() {
    this.isRunning = false;
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  stop() {
    this.pause();
    this.remainingSeconds = this.initialDuration;
    this.render();
  }

  formatTime(totalSeconds) {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  render() {
    if (this.displayElement) {
      this.displayElement.textContent = this.formatTime(this.remainingSeconds);
    }
  }

  playAlarm() {
    try {
      // Browser Web Audio API Synthesizer (Zero external sound file dependencies)
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.type = 'sine';
      osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);
      osc.start();
      osc.stop(ctx.currentTime + 0.8);
    } catch {
      // AudioContext unavailable
    }
  }
}
