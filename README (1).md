# India AQI CNN-LSTM Repository

This repository is built only for Objective 1 training using the following sources:
- INSAT-3D AOD
- Sentinel-5P TROPOMI NO2, SO2, CO, O3, HCHO
- CPCB surface air quality data
- MODIS/VIIRS fire counts
- Reanalysis meteorology from ERA5 / IMDAA / MERRA-2

## Goal
Train a CNN-LSTM model to predict surface pollutant concentrations from satellite, ground, and meteorology data, then derive AQI-ready outputs.

## Folder structure
See `docs/FOLDER_STRUCTURE.md`.

## Expected input files
Place your CSV files in `data/raw/` or point to Google Drive paths when training in Colab.

## Main training file
- `src/train_objective1.py`

## Data prep file
- `src/data_builder.py`

## Colab workflow
1. Clone this repo in Colab.
2. Mount Google Drive.
3. Install `requirements.txt`.
4. Run `scripts/train_colab.sh`.
