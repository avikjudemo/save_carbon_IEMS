# tests/test_traffic_analysis.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.core_traffic_analyzer import TrafficAnalyzer
from src.audio_alert_system import AudioAlertSystem
from src.impact_calculator import ImpactCalculator


def test_traffic_analyzer():
    """Test traffic analyzer functionality"""
    analyzer = TrafficAnalyzer()

    # Test shutdown recommendation logic
    assert analyzer.should_recommend_shutdown('red', 5) == True
    assert analyzer.should_recommend_shutdown('red', 10) == False
    assert analyzer.should_recommend_shutdown('green', 5) == False

    print("✅ Traffic analyzer tests passed!")


def test_audio_system():
    """Test audio alert system"""
    audio_system = AudioAlertSystem()

    alert_message = audio_system.generate_alert(True)
    assert "switch off engine" in alert_message.lower()

    print("✅ Audio alert system tests passed!")


def test_impact_calculator():
    """Test impact calculator"""
    calculator = ImpactCalculator()
    results = calculator.calculate_impact_projections()

    assert len(results) == 3
    assert all(col in results.columns for col in ['scenario', 'co2_reduction_tons', 'economic_savings_million_eur'])

    print("✅ Impact calculator tests passed!")


if __name__ == "__main__":
    test_traffic_analyzer()
    test_audio_system()
    test_impact_calculator()
    print("🎉 All tests passed!")