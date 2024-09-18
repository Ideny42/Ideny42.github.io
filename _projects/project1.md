---
title: "DLRover: An Automatic Distributed Deep Learning System"
collection: projects
start_date: 2023.07
end_date: 2024.07
github_url: https://github.com/intelligent-machine-learning/dlrover
excerpt: "DLRover: An Automatic Distributed Deep Learning System <br/><img src='/images/dlrover.png' width='500' height='auto'>"
cv: |
    In the DLRover project, I participated in the development and testing of several sub-projects, gained valuable experience, and made significant contributions:<br/>
    <div style="margin-left: 20px;">
        <strong>Auto Accelerate Testing</strong> I contributed to the testing of the Auto Accelerate module, focusing on bug fixes and feature enhancements. I was mainly responsible for testing conventional methods and Bayesian methods, discovering and fixing multiple bugs, and improving existing features to enhance user experience. I also provided a resource calculation algorithm for the Auto Accelerate module.<br/>
        <strong>Llama2 and NanoGPT Instance Testing</strong> I was involved in testing the entire project under the Llama2 and NanoGPT instances, mainly focusing on scenarios such as FSDP and DDP. I submitted relevant test codes, test results, and documentation.<br/>
        <strong>Flash-checkpoint Development and Testing</strong> I participated in the development and testing of Flash-checkpoint, conducted in-depth research on the latest papers in the field, extracted design experiences from these papers, proposed solutions, and tested and adjusted the core code.<br/>
    </div>

---


DLRover makes the distributed training of large AI models easy, stable, fast and green.
It can automatically train the Deep Learning model on the distributed cluster.
It helps model developers to focus on model arichtecture, without taking care of
any engineering stuff, say, hardware acceleration, distributed running, etc.
Now, it provides automated operation and maintenance for deep learning
training jobs on K8s/Ray. Major features as

- **Fault-Tolerance**: The distributed training can continue running in the event of failures.
- **Flash Checkpoint**: The distributed training can recover failures from the in-memory checkpoint in seconds.
- **Auto-Scaling**: The distributed training can scale up/down resources to improve the stability, throughput
and resource utilization.

What's more, DLRover provides extension libraries of PyTorch and TensorFlow to Speed Up Training.

- [ATorch](atorch/README.md): an extension library of PyTorch to Speed Up Training of Large LLM.
- [TFPlus](tfplus/README.md): an extension library of TensorFlow to Speed Up Training of Search, Recommendation and Advertisement.
