# src/audio_alert_system.py
class AudioAlertSystem:
    def __init__(self):
        self.messages = {
            'shutdown_recommended': "Please switch off engine to save fuel and reduce emissions. Save Earth!",
            'shutdown_not_needed': "Multiple vehicles ahead. No need to switch off engine.",
            'system_ready': "I-EMS system activated and monitoring traffic."
        }

    def generate_alert(self, shutdown_recommended):
        """
        Generate appropriate audio alert based on analysis
        """
        if shutdown_recommended:
            return self.messages['shutdown_recommended']
        else:
            return self.messages['shutdown_not_needed']

    def simulate_audio_playback(self, message):
        """
        Simulate audio playback (replace with actual TTS in production)
        """
        print(f"🔊 AUDIO ALERT: {message}")
        return True