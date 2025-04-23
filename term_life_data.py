
def get_term_data():

        term_life_data = []

        # Define possible values
        ages = [20]  # 20, 25, 30, ..., 65
        smokers = ["N","Y"]
        genders = ["M","F"]
        # premium_type = ["annual"]  # As specified
        critical_illnesses = ["N","Y"]

        # Non-DPI Specific Values
        non_dpi_coverage_terms = ["1 to 5", "6 to 10", "11 to 15", "16 to 20", "21 to 25", "26 to 30", "31 to 35", "36 to 40", "Above 40"]
        non_dpi_sum_assured_values = ["S$ 50,000", "S$ 100,000", "S$ 200,000", "S$ 300,000", "S$ 400,000", "S$ 500,000", "S$ 750,000", "S$ 1,000,000"]




        # Generate combinations for Non-DPI
        for age in ages:
            for smoker in smokers:
                for gender in genders:
                    for critical_illness in critical_illnesses:
                        for coverage_term in non_dpi_coverage_terms:
                            for sum_assured in non_dpi_sum_assured_values:
                                term_life_data.append({
                                    "age": age,
                                    "smoker": smoker,
                                    "gender": gender,
                                    "coverage_term": coverage_term,
                                    "sum_assured": sum_assured,
                                    "critical_illness": critical_illness,
                                    "category": "non-dpi"
                                })

        # print(term_life_data)
        print(len(term_life_data))

        return term_life_data



# get_term_data()