# ML Application Template

An application template to wrap your machine learning code as a [FAST](https://fastapi.tiangolo.com/) RESTful API, complete with [Dockerfiles](https://docs.docker.com/engine/reference/builder/), [TensorBoard](https://www.tensorflow.org/guide/summaries_and_tensorboard), etc. Check out these simple projects for examples of how this template can be leveraged. → <img src="https://raw.githubusercontent.com/madewithml/images/master/images/tensorflow.png" width="20rem"> [TensorFlow](https://github.com/madewithml/lessons/tree/master/notebooks/03_APIs/tf-text-classification) or <img src="https://raw.githubusercontent.com/madewithml/images/master/images/pytorch.png" width="20rem"> [PyTorch](https://github.com/madewithml/lessons/tree/master/notebooks/03_APIs/pt-text-classification)

### Set Up
```bash
pip install cookiecutter invoke requests
cookiecutter gh:madewithml/ml-app-template
```

### Steps
1. Add ML functionality inside `{{ cookiecutter.package_name }}`.
2. Add API functionality inside `app.py`.
3. Add unit tests in `tests` as you develop.
4. Complete `README.md` with the appropriate details.