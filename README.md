# A template for new data analysis pipelines

When starting a new data analysis project, you can use this repository as a template to get you started.
It is a barebones implementation that incorporates all the tips featured in:

[Marijn van Vliet (2019): Guidelines for data analysis scripts](https://arxiv.org/abs/1904.06163)

This template contains a mock analysis pipeline with some mock data:
 * 2 subjects
 * 2 analysis steps
 * 2 figures

## Running the analysis pipeline
1. Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
1. Extract the downloaded zip file
1. Open a terminal and move into the folder containing the study template
1. Make sure all required python packages are installed by running: `pip install -r requirements.txt`

1. Run the analysis by either:
   * run `doit` to use a build system to run all the analysis steps
   * alternatively, run `python master.py` to use a simple master script to run all the analysis steps
  
After the analysis has been completed:
 * the processed data should be in the `processed/` folder
 * the HTML reports should be in the `reports/` folder
 * the generated figures should be in the `figures/` folder.

## Getting started with a new data analysis pipeline based on the study template
1. Download the study template by clicking [here](https://github.com/AaltoImagingLanguage/study_template/archive/master.zip)
1. Extract the downloaded zip file

1. Modify `config.py`
   1. Add your system to the list at the top, indication where your data is, how many cores you have on your machine, etc.
   1. Add all parameters relevant to your analysis to the script
   1. Add all filenames relevant to your analysis to the script

1. Add new scripts for each analysis step and each figure

1. Modify the master script to execute the scripts you have added by either:
   * Add new tasks to the `dodo.py` script to use the `doit` build system to run all the analysis steps. Delete `master.py`.
   * alternatively, add new lines to execute the scripts you have added to the `master.py` file to use a simple master script to run all the analysis steps. Delete `dodo.py`.

1. Modify `requirements.txt`
   1. Add all python packages your analysis pipeline needs
