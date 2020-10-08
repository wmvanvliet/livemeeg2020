[![Talk at LiveMEEG2020](livemeeg2020_small.png)](https://youtu.be/OlxVhkuiGPU)

# An example analysis pipeline that is well designed.

This will do a very bare-bones analysis of the EEG evoked potentials in the Brain Invaders dataset:

[Louis Korczowski, Ekaterina Ostaschenko, Anton Andreev, Grégoire Cattan, Pedro Luiz Coelho Rodrigues, Violette Gautheret, Marco Congedo. Brain Invaders calibration-less P300-based BCI using dry EEG electrodes Dataset (bi2014a)](https://hal.archives-ouvertes.fr/hal-02171575/)

This analysis consists of 4 steps:
 1. download the data
 2. bandpass filter
 3. cut epochs and compute evokeds
 4. compute grand average evokeds
 
The pipeline is based on the study template provided [here](https://github.com/AaltoImagingLanguage/study_template)

## Running the analysis pipeline
1. Download the  template by clicking [here](https://github.com/wmvanvliet/livemeeg2020/archive/master.zip)
1. Extract the downloaded zip file
1. Open a terminal and move into the folder containing the study template
1. Make sure all required python packages are installed by running: `pip install -r requirements.txt`
1. Modify `config.py` and add your system to the list at the top, indication where your data is, how many cores you have on your machine, etc.
1. Run the analysis with the command: `python -m doit`
  
After the analysis has been completed:
 * the processed data should be in the `processed/` folder
 * the generated figures should be in the `figures/` folder.
