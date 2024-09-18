---
title: "DLRover-RM: Resource Optimization for Deep Recommendation Models Training in the cloud"
collection: publications
category: manuscripts
permalink: /publication/dlrover
excerpt: ""
date: 2024-10-1
venue: 'PVLDB'
paperurl: 'https://www.vldb.org/pvldb/vol17/p4130-tang.pdf'
citation: 'Wang Q, Lan T, Tang Y, et al. DLRover-RM: Resource Optimization for Deep Recommendation Models Training in the Cloud[J].'
---

Deep learning recommendation models (DLRM) rely on large embedding tables to manage categorical sparse features. Expanding such embedding tables can significantly enhance model performance, but at the cost of increased GPU/CPU/memory usage. Meanwhile, tech companies have built extensive cloud-based services to accelerate training DLRM models at scale. In this paper, we conduct a deep investigation of the DLRM training platforms at AntGroup and reveal two critical challenges: low resource utilization due to suboptimal configurations by users and the tendency to encounter abnormalities due to an unstable cloud environment. To overcome them, we introduce DLRover, an elastic training framework for DLRMs designed to increase resource utilization and handle the instability of a cloud environment. DLRover develops a resource-performance model by considering the unique characteristics of DLRMs and a three-stage heuristic strategy to automatically allocate and dynamically adjust resources for DLRM training jobs for higher resource utilization. Further, DLRover develops multiple mechanisms to ensure efficient and reliable execution of DLRM training jobs. Our extensive evaluation shows that DLRover reduces job completion times by 31%, increases the job completion rate by 6%, enhances CPU usage by 15%, and improves memory utilization by 20%, compared to state-of-the-art resource scheduling frameworks. DLRover has been widely deployed at AntGroup and processes thousands of DLRM training jobs on a daily basis. DLRover is open-sourced and has been adopted by 10+ companies.