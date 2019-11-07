# Synthetic Data Generation Using Graphic Model

Due to privacy protection, socioeconomical data is released at aggregated regional levels, but practitioners often find individual level data far more appealing, as aggregated data lacks information such as variances and distributions of residents within that region. In order to utilize privacy-protected data, aggregated data needs to be downscaled at individual level. In this project, a synthetic dataset is generated from a demographic dataset at individual level and TransUnion dataset at aggregated level by using graphic model, more specifically, Gaussian Copula model.

## Methods for Synthetic Data Generation


### 1. Generative adversarial network (GAN) -- A Deep Learning Approach

GANs can be used to produce new data. It discovers structure in the data that allows them to make realistic data. It is useful if we cannot see that structure on our own or cannot pull it out with other methods. Although GAN is capable of synthetic data generaton, it can only augment original data, meaning the output of the model is the same shape as the original input data. It lacks the ability to downscale aggregated data.

### 2. Grahpic Model -- A Machine Learning Approach

It is a probabilistic model for which a graph expresses the conditional dependence structure between random variables, and the method used in this project.

Copulas allow us to decompose a joint probability distribution into their marginals (which by definition have no correlation). It is a function which couples (hence the name) them together and thus allows us to specify the correlation seperately. The copula is that coupling function.
