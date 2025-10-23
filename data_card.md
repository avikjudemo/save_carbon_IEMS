# Data Card: I-EMS (Intelligent Engine Management System)

## Overview
This data card documents the datasets, assumptions, and ethical considerations for the I-EMS project focused on reducing vehicle emissions through intelligent engine management.

## Dataset Information

### 1. Traffic Signal Data
**Source:** Synthetic simulation (production: LISA Traffic Light Dataset, Bosch Small Traffic Lights)
**Type:** Image data → Signal color classification
**Size:** 50,000+ annotated traffic scenes (production)
**Format:** RGB images with bounding box annotations
**Classes:** Red, Yellow, Green, Unknown
**Bias Considerations:** 
- Geographic bias toward European signal designs
- Weather conditions (rain, fog, night) under-represented
- Seasonal variations in lighting conditions

### 2. Vehicle Detection Data
**Source:** Synthetic simulation (production: COCO dataset, BDD100K)
**Type:** Object detection for vehicles
**Size:** 200,000+ vehicle instances (production)
**Classes:** Car, Motorcycle, Bus, Truck
**Accuracy:** >95% mAP@0.5 in controlled conditions
**Limitations:** 
- Occluded vehicles challenging to detect
- Motorcycles and bicycles have lower detection rates
- Varying vehicle sizes and colors

### 3. Emissions Calculation Data
**Source:** European Environment Agency, IPCC Guidelines
**Type:** Tabular data - emission factors and constants
**Key Parameters:**
```python
fuel_consumption = {
    'petrol_idle': 0.8,      # liters/hour (EU average)
    'diesel_idle': 0.6,      # liters/hour (EU average)
    'start_stop_penalty': 0.005  # liters per restart
}

emission_factors = {
    'petrol_co2': 2.31,      # kg CO₂/liter (EEA 2023)
    'diesel_co2': 2.68,      # kg CO₂/liter (EEA 2023)
    'petrol_nox': 0.0021,    # kg NOx/liter
    'diesel_nox': 0.0045     # kg NOx/liter
}