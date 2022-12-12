# Highly scalable deep learning training system with mixed-precision: Training ImageNet in four minutes

- Paper url: https://arxiv.org/pdf/1807.11205.pdf

```bibtex
@INPROCEEDINGS{jia2018highly,
  title={Highly scalable deep learning training system with mixed-precision: Training {ImageNet} in four minutes},
  author={Jia, Xianyan and Song, Shutao and He, Wei and Wang, Yangzihao and Rong, Haidong and Zhou, Feihu and Xie, Liqiang and Guo, Zhenyu and Yang, Yuanzhou and Yu, Liwei and others},
  booktitle={NeurIPS Workshop on Systems for ML and Open Source Software, Montreal, Canada}, 
  year={2018},
  month={12}
}
```

---
### Nov 19 2022

This paper introduces on how to achieve extraordinary performance on large
scale GPU systems. Can compare its contents to the recent posts published
by NVIDIA on the extra-scale MLPerf training.

- The bottleneck of AlexNet is communication while it is computation for
ResNet-50.
- Software: OpenMPI, TensorFlow, NCCL. Hardware: RDMA (?).

- 3 optimization techniques
  1) Mixed-precision training model. Section 4.1. Pure low F16 precision training
might cause the gradients to vanish and degrade the training process. Figure 2 shows
the data type casting process: the forward and backward operations are calculated
in FP16, but gradients and weights are cast twice.
  2) AlexNet model updates. Section 4.2. Figure 4. Also has the SGD method optimization
in Eq (2)-(3).
  3) Optimized all-reduce algorithm. Section 4.3. 
     - Tensor fusion. Pack small tensor together before all-reduce.
     - Hierarchical all-reduce. Figure 5 on the 3 stage communication method.
     - Hybrid all-reduce. Switch between the ring-based all-reduce and the above method.

- Challenge in large batch size training: larger batch size leads to high performance
**across the GPUs** but may decrease
the model accuracy (measured in top-1 test accuracy). Note here ImageNet is expensive
to train on a single GPU because of memory limit.
- Effectiveness is in Section 5. Figure 11 shows that the scaling efficiency of ResNet-50
is almost 100%.
- Further reading & thoughts:
  - [ ] [Shi Shaohuai's DAG SGD modeling work](https://arxiv.org/pdf/1805.03812.pdf)
  - [ ] NCCL, RDMA
  - [ ] NVIDIA's recent libraries on data loading and communication optimization
  - [ ] This paper talks a lot about the synchronized SGD. As now NNs tend to use
  Adam or other momentum-based optimizers, how is their scaling and communication pattern?
