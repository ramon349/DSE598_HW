# DSE 598 Project: The City and County Energy Profiles
by Jiwoong Jason Jeong and Ramon Luis Correa

## Introduction and context of the dataset:
**City and County Energy Profiles (2016)**

The City and County Energy Profiles lookup table is a dataset curated in 2016. The dataset provides modeled electricity and natural gas consumption and expenditures, on-road vehicle fuel consumption, vehicle miles traveled, and associated emissions for each U.S. city and county. Many sections of the dataset has a high level of granularity and groupings from 4 emissions factors, 8 different climate zones, 8 greenhouse gas (GHG) emissions, 26 categories of subregions of electrical grids, 44 different consumption codes, 88 different expenditure codes, and thousands of city and county codes. This data is part of a suite of state and local energy profile data available at the "State and Local Energy Profile Data Suite" and builds on Cities-LEAP energy modeling.

## Objectives/Deliverables:
For our project, we are interested in two tasks involving the development of a data generation model and the testing of a hypothesis. We will first develop a data generation model to estimate the energy consumption of a given region. The goal will be accomplished by fitting a linear regression model. Upon completion, we will be able to study the goodness of fit of our model and study possible outliers. Due to the interpretable nature of linear models, we will also be able to study the model coefficients and understand what factors impact energy consumption the most. 

Our second task will be to study if there is a difference in energy consumption/GHC emissions by egrid subregion/DOE climate zone. This will be an interesting task as studies have shown that the effect of global warming is getting worse and the world is getting warmer faster and faster. So, it will be interesting to see the energy consumption and GHG emissions across different climate zones and egrid subregions. If there is a difference between the zones, especially if the warmer zones have a higher energy consumption or GHG emissions, that might give strong reasons for working against climate change.

## Tasks:
### Visualization
* [x] develop visualization method to account for different levels of granularity and metrics
* [ ] develop a visualization method for city level granularity

### Data consolidation
* [ ] make a script/pipeline to consolidate all the different levels of emissions and energy spending (e.g. combine to residential, commercial, industry, vs on-road; gas vs electricity)

### Linear regression (data generation) model
* [ ] develop a linear regression model
* [ ] provide feature reduction method to feed into the linear regression model
* [ ] provide interpretability of the model coefficients

### Test of significance between geographical locations and DOE climate zones
* [ ] running hypothesis/significance testing on different levels of granularity: climate zones, states, counties, etc.

# Brain Storming

- use linear regression model. if it works to simulate effects of "global warming" by modifying effect changes the linear model can also be used to demonstrate differences between states.
- simulation of climate zone temperature changes.
- Demonstrate the effect of using Lasso . Would allow for the "interpretability" of coefficients.
- Guide our analysis of simulation by using features with the highest coefficients.
- significance test of  consumption.  by region.
- run a statistical hypothesis test.  to  compare climate zones. 
