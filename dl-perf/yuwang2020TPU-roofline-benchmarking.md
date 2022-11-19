# ParaDNN: benchmarking TPU, GPU and CPU and roofline analysis

- Paper url
  - https://arxiv.org/pdf/1907.10701.pdf
  - https://yuemmawang.github.io/publications/wang-mlsys2020.pdf
- ParaDNN github: https://github.com/Emma926/paradnn

```bibtex
@article{wang2019benchmarking,
  title={Benchmarking TPU, GPU, and CPU platforms for deep learning},
  author={Wang, Yu Emma and Wei, Gu-Yeon and Brooks, David},
  journal={arXiv preprint arXiv:1907.10701},
  year={2019}
}

@inproceedings{wang2020systematic,
  title={A Systematic Methodology for Analysis of Deep Learning Hardware and Software Platforms},
  author={Wang, Yu Emma and Wei, Gu-Yeon and Brooks, David},
  booktitle={The 3rd Conference on Machine Learning and Systems (MLSys)},
  year={2020}
}
```
---
### Oct 2022

This paper studies the DL training performance on one GPU/TPU/GPU.
 Specifically, it compares TPU v2 to v3 and TPU to NVIDIA V100.
 It utilizes the Roofline model to study the GFLOPS utilization vs
 batch size, model size, etc, as well as the computation breakdown of the FC/RNN.
 It also provides parameterized FC/CNN/RNN benchmarking models.
 The roofline analysis part is in Section 4.2, and it's very insightful.

The ParamDnn benchmark suite is available [here](https://github.com/Emma926/paradnn).
 The whole stuff works with TensorFlow but not PyTorch.
 The parameterized FC/CNN/DNN benchmarking script can be port to PyTorch.

This paper also involves some MLPerf or other typical DL benchmarking results,
 but I did not look into them carefully. I care about the roofline analysis and the
 FC/CNN/RNN hyperparameter configuration most.
