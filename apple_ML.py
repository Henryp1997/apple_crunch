import sklearn

print(sklearn.__version__)

# In this file the model will be trained. The aim is to take in the audio data
# extracted by extract_waveform_data.py and use sci-kit learn's classification
# methods to train a model to predict the crunchiness of an unlabelled apple.
#
# The main obstacles to tackle are:
#
# 1. What will make up the feature set? This could be things like the frequencies
#    in the fft, the relaxation time of one of the waveforms etc
# 2. What model is the most appropriate for the labelling? The apple crunchiness
#    is measured on a scale of 1 to 5 and allows half integer values. So should
#    this be considered a continuous variable or a categorical one (9 categories)?
# 3. Is my perception of a, say, a 3/5 crunchiness different from a different person's?
#    This might not be an issue if the dataset is large, but it could mean I should
#    try an unsupervised learning approach to try and find patterns in the data
#    instead
# 4. How should the extraction of noise be achieved?