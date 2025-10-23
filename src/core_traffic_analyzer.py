# src/core_traffic_analyzer.py
import numpy as np
import pandas as pd


class TrafficAnalyzer:
    def __init__(self):
        self.signal_states = ['red', 'yellow', 'green', 'unknown']
        self.vehicle_count_threshold = 8

    def simulate_traffic_analysis(self, image_path=None):
        """
        Simulate traffic analysis (replace with actual CV model in production)
        Returns signal color and vehicle count
        """
        # For simulation without OpenCV, return realistic values
        import random

        signal_color = random.choice(['red', 'green'])
        vehicle_count = random.randint(0, 15)

        return signal_color, vehicle_count

    def should_recommend_shutdown(self, signal_color, vehicle_count):
        """
        Determine if engine shutdown should be recommended
        """
        return signal_color == 'red' and vehicle_count < self.vehicle_count_threshold

    def analyze_traffic_scenario(self, image_path=None):
        """
        Complete traffic analysis pipeline
        """
        signal_color, vehicle_count = self.simulate_traffic_analysis(image_path)
        shutdown_recommended = self.should_recommend_shutdown(signal_color, vehicle_count)

        return {
            'signal_color': signal_color,
            'vehicle_count': vehicle_count,
            'shutdown_recommended': shutdown_recommended,
            'threshold': self.vehicle_count_threshold
        }

    def run_demo(self, num_scenarios=5):
        """
        Run demo scenarios to show how the system works
        """
        print("🚦 I-EMS Traffic Analysis Demo")
        print("=" * 40)

        for i in range(num_scenarios):
            result = self.analyze_traffic_scenario()
            print(f"Scenario {i + 1}:")
            print(f"  Signal: {result['signal_color'].upper()}")
            print(f"  Vehicles ahead: {result['vehicle_count']}")
            print(f"  Shutdown recommended: {result['shutdown_recommended']}")
            print(f"  Alert: {'SWITCH OFF ENGINE' if result['shutdown_recommended'] else 'Continue idling'}")
            print("-" * 30)