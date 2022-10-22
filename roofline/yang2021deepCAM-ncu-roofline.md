# Hierarchical roofline performance analysis for deep learning applications 

Paper link: https://arxiv.org/pdf/2009.05257.pdf

```bibtex
@incollection{yang2021hierarchical,
  title={Hierarchical roofline performance analysis for deep learning applications},
  author={Yang, Charlene and Wang, Yunsong and Kurth, Thorsten and Farrell, Steven and Williams, Samuel},
  booktitle={Intelligent Computing},
  pages={473--491},
  year={2021},
  publisher={Springer}
}
```
---
This paper is a guide on how to analyze/tune the DL workloads with the Roofline model.
 It tunes [DeepCAM](https://github.com/azrael417/mlperf-deepcam), a 2018 Goden Bell winner
 implemented with both PyTorch and TensorFlow, and plot the performance of different kernels
 in roofline charts. 

The tool used on the GPU side is “Nsight Compute”, with commands like
```bash
nv-nsight-cu-cli –metrics ${metric} ./${application} 
```
Table 2 gives the details of Nsight Compute (NCU) metrics to calculate the FLOPS, bytes and time.

Though this work is done on a V100 GPU, it gives many insights on how to get GPU NCU
 roofline metrics, how to analyze the performance bottlenecks & further improvements, the AMP functionality,
 tensor core utilization, etc. 

#### Some findings
- There is profiling overhead, so the metrics are got from separate runs.
- [**AMP**](https://developer.nvidia.com/automatic-mixed-precision):
 the experiment is done with special AMP (NVIDIA's Automatic Mixed Precision package, 
 converts F32 into F16 automatically) optimization levels.
 PyTorch has O0/O1/O2 levels, and the paper confirms that O1 is much more efficient than O0.
 O2 might lead to some convergence problems. Overall, AMP is very effective. 

- It turns out TensorFlow utilizes the Tensor Cores (TC) pretty well, so some kernels almost
 achieve the peak performance of TC for both the forward pass and the backward pass.
 The No-1 time-consuming kernel in PyTorch backward pass does not utilize the tensor cores,
 and shows poor performance with high arithmetic intensity. 

- TensorFlow forward pass shows high L2 cache locality and poor L1 locality. 
- TensorFlow has dominant (in runtime) kernels but PyTorch does not have any in forward pass. 
- Non-AI workloads (no FP operation is performed, i.e., data type converting, rearranging the data layout, etc.)
 accounts for 50% of the time. They should be overlapped better. 
