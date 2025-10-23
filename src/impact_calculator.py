# src/impact_calculator.py
import pandas as pd
import numpy as np
import os


class ImpactCalculator:
    def __init__(self):
        # Emission factors and constants
        self.fuel_consumption = {
            'petrol_idle': 0.8,  # liters/hour
            'diesel_idle': 0.6,  # liters/hour
            'start_stop_penalty': 0.005  # liters per restart
        }
        self.emission_factors = {
            'petrol_co2': 2.31,  # kg CO₂/liter
            'diesel_co2': 2.68,  # kg CO₂/liter
            'petrol_nox': 0.0021,  # kg NOx/liter
            'diesel_nox': 0.0045  # kg NOx/liter
        }
        self.water_intensity = 4.5  # liters water per liter fuel produced
        self.fuel_price_eur_per_liter = 1.5  # Average fuel price in EUR

    def calculate_impact_projections(self):
        """Calculate impact projections for different scenarios"""

        # Base assumptions
        eu_fleet_size = 250_000_000
        scenarios = {
            'conservative': {'adoption_rate': 0.10, 'daily_shutdowns': 3},
            'moderate': {'adoption_rate': 0.25, 'daily_shutdowns': 5},
            'aggressive': {'adoption_rate': 0.40, 'daily_shutdowns': 8}
        }

        results = []

        for scenario_name, params in scenarios.items():
            vehicles_equipped = int(eu_fleet_size * params['adoption_rate'])
            daily_shutdowns = params['daily_shutdowns']
            avg_idling_avoided = 30  # seconds per shutdown

            # Annual fuel savings (liters)
            annual_fuel_savings = (
                    vehicles_equipped *
                    daily_shutdowns *
                    365 *
                    (avg_idling_avoided / 3600) *
                    self.fuel_consumption['petrol_idle']
            )

            # CO₂ reduction (kg)
            co2_reduction_kg = annual_fuel_savings * self.emission_factors['petrol_co2']

            # NOx reduction (kg)
            nox_reduction_kg = annual_fuel_savings * self.emission_factors['petrol_nox']

            # Water savings (liters) - from reduced fuel production
            water_savings_liters = annual_fuel_savings * self.water_intensity

            # Economic savings (€)
            economic_savings_eur = annual_fuel_savings * self.fuel_price_eur_per_liter

            results.append({
                'scenario': scenario_name,
                'adoption_rate_percent': params['adoption_rate'] * 100,
                'vehicles_equipped': vehicles_equipped,
                'daily_shutdowns_per_vehicle': daily_shutdowns,
                'annual_fuel_savings_liters': annual_fuel_savings,
                'co2_reduction_tons': co2_reduction_kg / 1000,
                'nox_reduction_tons': nox_reduction_kg / 1000,
                'water_savings_cubic_meters': water_savings_liters / 1000,
                'economic_savings_million_eur': economic_savings_eur / 1000000
            })

        return pd.DataFrame(results)

    def save_impact_math(self, filepath='../impact_math.csv'):
        """Calculate and save impact projections to CSV"""
        # Get the absolute path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_filepath = os.path.join(current_dir, filepath)

        impact_df = self.calculate_impact_projections()
        impact_df.to_csv(absolute_filepath, index=False)
        print(f"✅ Impact calculations saved to {absolute_filepath}")
        return impact_df

    def print_detailed_summary(self):
        """Print a formatted summary of impact calculations"""
        impact_df = self.calculate_impact_projections()

        print("=" * 70)
        print("I-EMS: INTELLIGENT ENGINE MANAGEMENT SYSTEM")
        print("IMPACT PROJECTIONS ANALYSIS")
        print("=" * 70)

        print("\nBASELINE ASSUMPTIONS:")
        print(f"• EU Passenger Vehicle Fleet: {250_000_000:,} vehicles")
        print(f"• Average Idling Avoided per Shutdown: 30 seconds")
        print(f"• Petrol Consumption While Idling: {self.fuel_consumption['petrol_idle']} liters/hour")
        print(f"• CO₂ Emission Factor: {self.emission_factors['petrol_co2']} kg/liter")
        print(f"• Fuel Price: €{self.fuel_price_eur_per_liter}/liter")
        print(f"• Water Intensity: {self.water_intensity} liters water/liter fuel")

        print("\n" + "=" * 70)
        print("SCENARIO ANALYSIS")
        print("=" * 70)

        for _, row in impact_df.iterrows():
            print(f"\n📊 {row['scenario'].upper()} SCENARIO ({row['adoption_rate_percent']}% Adoption):")
            print(f"   Vehicles Equipped: {row['vehicles_equipped']:,}")
            print(f"   Daily Shutdowns per Vehicle: {row['daily_shutdowns_per_vehicle']}")
            print(f"   Annual Fuel Savings: {row['annual_fuel_savings_liters']:,.0f} liters")
            print(f"   CO₂ Reduction: {row['co2_reduction_tons']:,.0f} tons")
            print(f"   NOx Reduction: {row['nox_reduction_tons']:,.0f} tons")
            print(f"   Water Savings: {row['water_savings_cubic_meters']:,.0f} m³")
            print(f"   Economic Savings: €{row['economic_savings_million_eur']:,.1f} million")

        print("\n" + "=" * 70)
        print("ENVIRONMENTAL EQUIVALENTS")
        print("=" * 70)

        moderate_scenario = impact_df[impact_df['scenario'] == 'moderate'].iloc[0]

        # Environmental equivalents
        trees_equivalent = moderate_scenario['co2_reduction_tons'] / 21  # tons CO2 per tree per year
        cars_off_road = moderate_scenario['co2_reduction_tons'] / 2400  # avg car emissions per year

        print(f"Moderate Scenario Equivalents:")
        print(f"• Carbon sequestered by {trees_equivalent:,.0f} trees annually")
        print(f"• Equivalent to removing {cars_off_road:,.0f} cars from roads")
        print(f"• Water savings enough for {moderate_scenario['water_savings_cubic_meters'] / 50:,.0f} households/year")


def main():
    """Main function to run impact calculations"""
    print("🚀 Starting I-EMS Impact Calculator...")

    calculator = ImpactCalculator()

    # Calculate and save impact projections
    impact_data = calculator.save_impact_math('../impact_math.csv')

    # Print detailed summary
    calculator.print_detailed_summary()

    print("\n✅ Impact analysis completed successfully!")


if __name__ == "__main__":
    main()