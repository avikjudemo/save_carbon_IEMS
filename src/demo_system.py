# src/demo_system.py
from core_traffic_analyzer import TrafficAnalyzer
from audio_alert_system import AudioAlertSystem
from impact_calculator import ImpactCalculator


def run_complete_demo():
    """Run a complete demo of the I-EMS system"""
    print("🚗 I-EMS: Intelligent Engine Management System")
    print("=" * 50)

    # Initialize systems
    traffic_analyzer = TrafficAnalyzer()
    audio_system = AudioAlertSystem()
    impact_calculator = ImpactCalculator()

    # Demo traffic analysis
    print("\n1. TRAFFIC ANALYSIS DEMO:")
    print("-" * 30)
    traffic_analyzer.run_demo(3)

    # Demo audio alerts
    print("\n2. AUDIO ALERT SYSTEM:")
    print("-" * 30)
    test_scenarios = [True, False]  # shutdown recommended, not recommended
    for shutdown in test_scenarios:
        alert = audio_system.generate_alert(shutdown)
        print(f"Shutdown recommended: {shutdown}")
        print(f"Audio alert: {alert}")
        print()

    # Demo impact calculations
    print("\n3. IMPACT CALCULATIONS:")
    print("-" * 30)
    impact_calculator.print_detailed_summary()

    print("\n✅ Demo completed successfully!")


if __name__ == "__main__":
    run_complete_demo()