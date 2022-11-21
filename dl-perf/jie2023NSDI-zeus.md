# Zeus: Understanding and Optimizing GPU Energy Consumption of DNN Training

- Paper link: https://arxiv.org/pdf/2208.06102.pdf
- Github repo: https://github.com/SymbioticLab/Zeus
- Orgnization webpage: https://ml.energy/zeus/

```bibtex
@inproceedings{zeus-nsdi23,
    title     = {Zeus: Understanding and Optimizing {GPU} Energy Consumption of {DNN} Training},
    author    = {Jie You and Jae-Won Chung and Mosharaf Chowdhury},
    booktitle = {USENIX NSDI},
    year      = {2023}
}
```

---
### Nov 15 2022

- High-throughput DL applications usually come with low energy efficiency.
- The problem comes down to finding the optimal batch_size and power_cap.
 They formulate the batch_size problem as a Multi-Armed Bandit (MAB) and run
 online optimization using Thomas Sampling policy.
- The system they developed with PyTorch can reduce 15.3-75.8% energy, compared
 to the maximum batch_size and power_cap. Maximum power_cap is NVIDIA's
 current policy. Energy saving numbers are in Figure 1.


