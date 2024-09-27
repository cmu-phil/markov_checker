# Description: This script is used to generate plots for all the result files in the alg_output/markov_check_data/ directory.
# The plots are generated using the extract_data_and_plot.py script.

import os

import extract_data_and_plot as ep

directory = "alg_output_with_true/markov_check_lg/"

# for y_var in ['|G|', 'bic']:
# for y_var in ['loglik', 'pvalue', 'ap', 'ar', 'ahp', 'ahr', 'f1_all', 'f0.5', 'f2.0']:
for y_var in ['|G|', 'bic', 'f1', 'shd', 'cfi', 'nfi', 'chisq', 'dof', 'loglik', 'pvalue', 'ap', 'ar', 'ahp', 'ahr', 'f1_all', 'f0.5', 'f2.0']:
    for filename in os.listdir(directory):
        if filename.startswith("result") and filename.endswith(".txt"):  # Process only result files
            file_path = os.path.join(directory, filename)
            df = ep.extract_first_dataset(file_path)

            output_file = filename.replace(".txt", "_" + y_var + ".png")  # Save each plot with a corresponding .png name
            ep.generate_plot(df, "simulation", filename, "kldiv", y_var, output_file=output_file, p_value_var='p_ad',
                             transparency=0.7, alpha=0.05, palette="Set3")

# directory = "alg_output/markov_check_us_crime/"
#
# for y_var in ['chisq', 'dof', 'pvalue']:
# # for y_var in ['|G|', 'bic', 'cfi', 'nfi']:
#     for filename in os.listdir(directory):
#         if filename.startswith("result") and filename.endswith(".txt"):  # Process only result files
#             file_path = os.path.join(directory, filename)
#             df = ep.extract_first_dataset(file_path)
#
#             output_file = filename.replace(".txt", ".png")  # Save each plot with a corresponding .png name
#             ep.generate_plot(df, "us_crime", filename, "kldiv", y_var, output_file=output_file, p_value_var='p_ad',
#                              transparency=0.7, alpha=0.2, palette="Set3")
