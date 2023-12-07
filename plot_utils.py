import pandas as pd
import folium
import requests
from folium.plugins import HeatMap


# function to convert county_id to FIPS (Federal Information Processing System) Codes
def conv_to_fips(row):
  s = str(row)
  if len(s)<=4:
      return "0500000US0" + s
  else:
      return "0500000US" + s

def convert_state_level(df, column):
  # convert data into state levels
  state_ids = []
  columns = []
  for i in df.state_abbr.unique():
    state_ids.append(i)
    df_state = df[df['state_abbr'] == i]
    columns.append(df_state[column].sum())
  state_df = pd.DataFrame({'state_abbr': state_ids, column: columns})
  return state_df

def make_map(df, column, level='state'):
  """
  df: dataframe of the data with 'state_id', 'county_id' or 'city_id' - all in FIPS codes for visualization
  column: column to plot the values of 'population', 'doe_climate_zone', 'consumption (MWh)', etc.
  level: argument to check the level of mapping during granularity: state, county, city - only state and county for now, no default city json from Folium
  """
  # get data and convert level id to fips
  if level == 'county':
    df['{}_fips'.format(level)] = df['{}_id'.format(level)].apply(conv_to_fips)

  # get geography from Folium
  if level == 'state':
    geo = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
    ).json()
  elif level == 'county':
    geo = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us_counties_20m_topo.json"
    ).json()
  else:
    m = folium.Map(location=[48, -102], zoom_start=3)
    # make a workaround so that heatmaps work for city points
    heat_data = []
    for i in range(len(df)):
      # find the number of "counts" to make relative to the column
      count_multiple = int(100*df[column].iloc[i]/df[column].max())
      if count_multiple < 1:
        continue
      for j in range(count_multiple):
        heat_data.append([df['latitude'].iloc[i], df['longitude'].iloc[i]])

    # Plot it on the map
    HeatMap(heat_data).add_to(m)
    return m

  # plot folium map - generalized to show the whole contiguous US
  m = folium.Map(location=[48, -102], zoom_start=3)
  folium.Choropleth(
      geo_data=geo,
      name="choropleth",
      data=df,
      columns=["{}_fips".format(level), column] if level == 'county' else ["state_abbr", column],
      key_on="feature.id",
      fill_color="YlGn",
      fill_opacity=0.7,
      line_opacity=0.2,
      legend_name="{} {}".format(level, column),
      topojson='objects.us_counties_20m' if level == 'county' else None
  ).add_to(m)
  return m