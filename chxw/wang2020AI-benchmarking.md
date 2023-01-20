# Benchmarking the Performance and Energy Efficiency of AI Accelerators for AI Training

Paper url: https://ieeexplore.ieee.org/abstract/document/9139681

```bibtex
@INPROCEEDINGS{wangyuxin2020benchamrking,
  author={Wang, Yuxin and Wang, Qiang and Shi, Shaohuai and He, Xin and Tang, Zhenheng and Zhao, Kaiyong and Chu, Xiaowen},
  booktitle={2020 20th IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGRID)}, 
  title={Benchmarking the Performance and Energy Efficiency of AI Accelerators for AI Training}, 
  year={2020},
  pages={744-751},
  doi={10.1109/CCGrid49817.2020.00-15}}
```


---
### Jan 20 2023

This is a work done in 2020. They benchmarked four platforms: Intel CPU with
AVX (advanced vector extension), NVIDIA GPU (V100, P100, Titan X),
AMD GPU (Radeon VII) and TPU (v2, v3). They include some real world DL benchmarks
as long as CUDA C++ matrix multiplication and convolution kernels.

Summary of findings is provided in Table II, while GPU platform comparison is
listed in Table III. Fig 2-9 show the benchmarking results.

TPU is very fast in terms of performance. When talking about energy efficiency,
GPU V100 and the transformer model is the best.

The metric of performance is samples/second and J/samples of energy efficiency.

