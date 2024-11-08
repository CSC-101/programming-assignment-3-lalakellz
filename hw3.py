from data import CountyDemographics

#part 1
# Function to calculate the total 2014 population across a list of counties
# input: list of CountyDemographics objects
# output: total population for 2014 as an integer
def population_total(counties: list[CountyDemographics]) -> int:
    return sum(county.population.get('2014 Population', 0) for county in counties)

#part 2
# Function to filter counties by state
# input: list of CountyDemographics objects, a two-letter state abbreviation as a string
# output: list of CountyDemographics objects for counties within the specified state
def filter_by_state(counties: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state_abbr]

#part 3
# Function to calculate the total population for a specified education level across counties.
# input: list of CountyDemographics objects, string representing the education key of interest
# output: float representing the total population for the specified education level
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = 0.0
    for county in counties:
        # Check if the education key exists in the county's data
        if education_key in county.education:
            # Calculate the subpopulation for the specified education key
            percent_with_education = county.education[education_key]
            county_population_2014 = county.population['2014 Population']
            sub_population = (percent_with_education / 100) * county_population_2014
            total_population += sub_population
    return total_population

# Function to calculate the total population for a given ethnicity key
# input: list of CountyDemographics objects, ethnicity key (string)
# output: total population for the given ethnicity key
# Function to calculate the total subpopulation by ethnicity
# input: list of CountyDemographics objects, the key for ethnicity of interest as a string
# output: float value of the total 2014 subpopulation for the specified ethnicity
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0.0

    for county in counties:
        # Check if 2014 population and the ethnicity key exist for the county
        if '2014 Population' in county.population and ethnicity_key in county.ethnicities:
            # Calculate subpopulation for the ethnicity
            total_population += county.population['2014 Population'] * county.ethnicities[ethnicity_key] / 100

    return total_population

# Function to calculate total population below poverty level across counties
# input: list of CountyDemographics
# output: float representing total population below poverty level in 2014
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_poverty_population = 0.0
    for county in counties:
        # Add to the total if 'Persons Below Poverty Level' exists in income data
        if 'Persons Below Poverty Level' in county.income:
            poverty_percentage = county.income['Persons Below Poverty Level']
            population_2014 = county.population.get('2014 Population', 0)
            # Calculate the population below poverty level for this county
            total_poverty_population += (poverty_percentage / 100) * population_2014
    return total_poverty_population

#part 4
# Function to calculate the percentage of a sub-population for a given education key
# input: list of CountyDemographics, education key (str)
# output: percentage of population with specified education level
def percent_by_education(counties, education_key):
    total_population = population_total(counties)  # Get the total 2014 population
    education_population = population_by_education(counties, education_key)  # Get the population for the specified education key
    if total_population == 0:
        return 0
    # Calculate and return the percentage
    return (education_population / total_population) * 100


# Function to calculate the percentage of a sub-population for a given ethnicity key
# input: list of CountyDemographics, ethnicity key (str)
# output: percentage of population for the specified ethnicity
def percent_by_ethnicity(counties, ethnicity_key):
    total_population = population_total(counties)  # Get the total 2014 population
    ethnicity_population = population_by_ethnicity(counties, ethnicity_key)
    if total_population == 0:
        return 0  # Avoid division by zero if there's no total population
    # Calculate and return the percentage
    return (ethnicity_population / total_population) * 100

