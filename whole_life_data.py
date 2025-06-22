
def get_whole_data():

        term_whole_data = []

        # Define possible values
        ages = [20]  # 20, 25, 30, ..., 65
        smokers = ["N","Y"]
        genders = ["M","F"]
        # premium_type = ["annual"]  # As specified
        critical_illnesses = ["N","Y"]

        # Non-DPI Specific Values
        non_dpi_premium_term = ["11 to 15", "16 to 20"]
        non_dpi_sum_assured_values = ["S$ 200,000"]




        # Generate combinations for Non-DPI
        for age in ages:
            for smoker in smokers:
                for gender in genders:
                    for critical_illness in critical_illnesses:
                        for premium_term in non_dpi_premium_term:
                            for sum_assured in non_dpi_sum_assured_values:
                                term_whole_data.append({
                                    "age": age,
                                    "smoker": smoker,
                                    "gender": gender,
                                    "premium_term": premium_term,
                                    "sum_assured": sum_assured,
                                    "critical_illness": critical_illness,
                                    "category": "non-dpi"
                                })

        # print(term_whole_data)
        print(len(term_whole_data))

        return term_whole_data



# get_term_data()