# TPU usage in colab with single line of code

## Before installation Make sure your TPU is on

![](https://camo.githubusercontent.com/dd817760c179975842deecf76ca0f31f4ac5a0dfddd6d57a393c1e8ac2156a58/68747470733a2f2f692e737461636b2e696d6775722e636f6d2f41444e666f2e706e67)

## Installation

To install the package from the PyPi repository you can execute the following
command:

```sh
pip install tpu_tf2
```
If you prefer, you can clone it and run the setup.py file. Use the following commands to get a copy from GitHub and install all dependencies:
```bash
git clone https://github.com/ashishpatel26/regressionmetrics.git
cd tpu_tf2
pip install .
```
## Usage

> usage in colab : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/tpu_tf2/blob/main/demo_colab.ipynb)

```python
from tpu_tf2.tpu import strategy
strategy.num_replicas_in_sync

> output : 8
```

💁 Thanks for reading and forking.
---
