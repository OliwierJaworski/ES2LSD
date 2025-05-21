
# Project: Sensor Data Logging en Verwerking naar Loxone

## Inhoud
- Gebruikte sensoren
- Raspberry Pi 3 Model B v1.2
- Libelium Waspmote + Agriculture Sensor Board v3.0
- Software en dataverwerking
- Behuizingsevolutie
- Gebruiksscenario
- Onderzoek naar compact alternatief
- Conclusie

---

## Gebruikte sensoren

### ⚠️ Watermark 200SS
- **Type:** Bodemvochtigheidssensor (weerstand-gebaseerd)
- **Output:** 550 – 50kΩ, uitleesbaar via frequentie
- **Meetwaarden:** in centibar (cb) of via frequentie (~7500 Hz = nat, <1000 Hz = droog)

### ☀️ Apogee SQ-110 (PAR-sensor)
- **Meet:** Photosynthetically Active Radiation (PAR) in µmol/m²/s
- **Output:** 0–2.5 V analoog
- **Toepassing:** landbouw, tuinbouw, weerstations

### ❄️ PT1000 Temperatuursensor (1712)
- **Type:** RTD sensor, 1000Ω bij 0 °C
- **Bereik:** -50 °C tot +250 °C
- **Nauwkeurigheid:** Klasse A ± 0.15 °C

---

## Raspberry Pi 3 Model B v1.2

- **CPU:** Quad-core 1.2GHz ARM Cortex-A53
- **RAM:** 1GB LPDDR2
- **WiFi/Bluetooth:** 802.11n / BLE 4.1
- **GPIO:** 40-pins header
- **Opslag:** microSD
- **Gebruik:** uitlezing sensoren, datadoorvoer via WiFi naar Loxone

---

## Libelium Waspmote + Agriculture Sensor Board v3.0

- **MCU:** ATmega1281 @ 14.74 MHz
- **Geheugen:** 128KB Flash / 8KB SRAM / 4KB EEPROM
- **Aansluitingen:** analoog, digitaal, UART, I2C, SPI
- **Sensoren:** bodemvocht, temperatuur, licht, luchtvochtigheid
- **Voeding:** 3.3 – 4.2V Li-ion batterij / zonnepaneel
- **Opslag:** microSD-kaart
- **Gebruik:** uitlezen van alle gekoppelde sensoren

---

## Software

1. **Installatie Raspberry Pi OS**
2. **Installatie van PuTTY** om via USB data van Libelium in te lezen
3. **Inschakelen van SSH** voor remote toegang en testing
4. **Eigen Python-code en launchescript** om data via WiFi naar het IP-adres van de Loxone Mini-Server te sturen

---

## Behuizingsevolutie

### 🔹 Eerste versie: 3D-geprint blauwgroen
- Te fragiel, niet waterdicht, geen plaats voor Raspberry Pi

### 🔹 Tweede versie: standaard grijze aftakdoos
- Te klein, geen interne schroefpunten, slechte kabeldoorvoer

### 🔹 Derde versie: hergebruikte Libelium Meshlium behuizing
- Genoeg ruimte, professionele afwerking, interne bevestiging, wartels aanwezig

---

## Gebruik

1. **Voeding via USB (5V)**
2. **Automatische opstart** van de Pi en het script
3. **WiFi-verbinding** met het schoolnetwerk
4. **Sensoruitlezing via USB** van Libelium
5. **Doorsturen van data naar de Loxone Mini-Server** voor logging/visualisatie

---

## Onderzoek naar compacter alternatief

Een poging werd gedaan om het systeem compacter te maken met een **SparkFun sensorboard + ESP32**. Het idee was dat het SparkFun-board data van Libelium zou ontvangen en de ESP32 deze via WiFi zou doorsturen.

### Problemen:
- Serieel uitlezen via SparkFun werkte niet stabiel
- ADC van de ESP32 niet nauwkeurig genoeg voor Watermark en PT1000
- WiFi-communicatie naar Loxone was niet robuust genoeg

**Besluit:** systeem was onbetrouwbaar en werd verworpen

---

## Conclusie

Het eindresultaat is een betrouwbaar, automatisch werkend meetsysteem op basis van een Libelium Waspmote en Raspberry Pi. Sensorwaarden worden via USB ingelezen en doorgestuurd naar een Loxone Mini-Server. Na testen van alternatieve hardware (SparkFun, ESP32) en behuizingen werd een professionele, herbruikte Meshlium-behuizing gekozen die voldoet aan alle eisen. Het systeem is klaar voor gebruik in een smart agriculture context.




Uitgebreid verslag in .pdf - [Project_sensordata.pdf](Project_sensordata.pdf)
