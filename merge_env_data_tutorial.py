#%%
import xarray as xr
import numpy as np
import os

# List of dataset file paths, to add more fields, just add path to .nc file
# Data must already be on a common grid (example data is 180x360x41x12)
file_paths = [
    '/home/mv23682/Documents/Abil_Wiseman2025/scripts/env_data_processing/regridded_data/temperature.nc',
    '/home/mv23682/Documents/Abil_Wiseman2025/scripts/env_data_processing/regridded_data/no3.nc',
    '/home/mv23682/Documents/Abil_Wiseman2025/scripts/env_data_processing/regridded_data/o2.nc',
    '/home/mv23682/Documents/Abil_Wiseman2025/scripts/env_data_processing/regridded_data/PAR.nc', 
]

# Open all datasets
datasets = [xr.open_dataset(fp) for fp in file_paths]

# Align all datasets to the intersection of their coordinates
aligned_datasets = xr.align(*datasets, join='inner')

# Merge the aligned datasets
merged_ds = xr.merge(aligned_datasets)

# List of variables of interest
variables_of_interest = ["temperature","no3","o2","PAR"]  # Add all relevant variable names

# Create a mask for where any of the variables are NaN
variables_mask = xr.concat([merged_ds[var].isnull() for var in variables_of_interest], dim='var').any(dim='var')

# Apply the mask to all variables, setting values to NaN where any variable is missing
for var in variables_of_interest:
    merged_ds[var] = merged_ds[var].where(~variables_mask, np.nan)

# Define region of interest to subset
# For tutorial: Southern Ocean (Lat < 40S) Summer (D, J, F), Subpolar North Atlantic (Lat 50-65N) (Lon 40W-0) Summer (JJA)
# Tropical and Subtropical Eastern Pacific (15S-15N) (145W-80W) ()

ds_so = merged_ds.where(
    (merged_ds.lat <= -35) &
    (merged_ds.depth <= 25) &
    (merged_ds.time.isin([11, 12, 1, 2, 3])),
    drop = True
)

ds_na = merged_ds.where(
    (merged_ds.lat >= 45) & (merged_ds.lat <= 70) &
    (merged_ds.lon >= -60) & (merged_ds.lon <= 0) &
    (merged_ds.depth <= 25) &
    (merged_ds.time.isin([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])),
    drop=True
)

ds_pac = merged_ds.where(
    (merged_ds.lat >= -15) & (merged_ds.lat <= 15) &
    (merged_ds.lon >= -150) & (merged_ds.lon <= -75) &
    (merged_ds.depth <= 25) &
    (merged_ds.time.isin([8, 9, 10, 11, 12])),
    drop=True
)

def output_data(ds,filename):
    df = ds.to_dataframe()
    df = df.reset_index()
    df.dropna(inplace=True)
    df.to_csv(os.path.join(filename + ".csv"),index=False)

    ds['lat'].attrs['units'] = 'degrees_north'
    ds['lat'].attrs['long_name'] = 'latitude'

    ds['lon'].attrs['units'] = 'degrees_east'
    ds['lon'].attrs['long_name'] = 'longitude'

    ds['depth'].attrs['units'] = 'm'
    ds['depth'].attrs['positive'] = 'down'

    ds['time'].attrs['units'] = 'months'

    ds['temperature'].attrs['units'] = 'degrees_celsius'
    ds['temperature'].attrs['long_name'] = 'sea_water_temperature'
    ds['temperature'].attrs['description'] = 'Objectively analyzed mean fields for sea_water_temperature from WOA18 of Locarnini et al. (2019)'

    ds['no3'].attrs['units'] = 'umol.kg-1'
    ds['no3'].attrs['long_name'] = 'nitrate'
    ds['no3'].attrs['description'] = 'Objectively analyzed mean fields for moles_concentration_of_nitrate_in_sea_water from WOA18 of Garcia et al. (2019)'

    ds['o2'].attrs['units'] = 'umol.kg-1'
    ds['o2'].attrs['long_name'] = 'dissolved oxygen'
    ds['o2'].attrs['description']= 'Objectively analyzed mean fields for mole_concentration_of_dissolved_molecular_oxygen_in_sea_water from WOA18 of Garcia et al. (2019)'

    ds['PAR'].attrs['units'] = 'W.m-2'
    ds['PAR'].attrs['long_name'] = 'photosynthetically activate radiation'
    ds['PAR'].attrs['description'] = 'RS_PAR_ESM-based_fill_monthly_clim_1998-2022 from Castant et al. (2024)'

    # Save the result to a new NetCDF file
    ds.to_netcdf(os.path.join(filename + ".nc"))

output_data(ds_so,"/home/mv23682/Documents/Abil_tutorial/data/env_data_so")
output_data(ds_na,"/home/mv23682/Documents/Abil_tutorial/data/env_data_na")
output_data(ds_pac,"/home/mv23682/Documents/Abil_tutorial/data/env_data_pac")

print('fin')
# %%
