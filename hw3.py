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
            # Calculate the sub-population for the specified education key
            percent_with_education = county.education[education_key]
            county_population_2014 = county.population['2014 Population']
            sub_population = (percent_with_education / 100) * county_population_2014
            total_population += sub_population
    return total_population

# Function to calculate the total population for a given ethnicity key
# input: list of CountyDemographics objects, ethnicity key (string)
# output: total population for the given ethnicity key
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0.0

    for county in counties:
        # Check if the ethnicity key exists in the county's ethnicities data
        if ethnicity_key in county.ethnicities:
            # Calculate the sub-population for the ethnicity key by multiplying the percentage by the total population
            population_percent = county.ethnicities[ethnicity_key]
            total_population += population_percent * county.population[
                '2014 Population'] / 100  # Divide by 100 to convert percentage to fraction

    return total_population

