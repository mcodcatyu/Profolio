## Project :  Drug-Induced Protein Conformational Transition Analysis

## Abstract
This project investigates drug-induced conformational changes in proteins by analyzing the distance variations between four key amino acid pairs. Using **Principal Component Analysis (PCA)** and **K-Means Clustering**, identified a distinct transition path: **Initial (Native) ➔ Intermediate ➔ Drug-Induced Stable State**. The emergence of a "Third Configuration" provides quantitative evidence of drug efficacy.---

## Simulations & Data
This analysis combines distance distribution observations with dimensionality reduction trajectories from high-dimensional data. The following are key data and results charts:

<div align="center">
  <img src="https://github.com/user-attachments/assets/792f0bea-a258-4349-b920-43c588ce41d4" width="700">
  <p><i><b>Figure 1:</b> Distances Distribution of 4 pairs (No Drug) - Distance distribution in the original state</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/dc79f87d-0e93-40ba-80cb-de59016af149" width="700">
  <p><i><b>Figure 2:</b> Distances Distribution of 4 pairs (Drug) - Significant shift and multi-peak distribution were observed after drug administration.</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/539695d4-7774-4e0f-bc26-4e03c9ad05ce" width="600">
  <p><i><b>Figure 3:</b> K-Means Clustering Results in PCA Space (drug)- Protein conformational evolution path trajectory diagram</i></p>
</div>

---

##  Scientific Logic 

### 1. Distance distribution as the basis of configuration (Distance as Descriptors)
* **No Drug (Fig 1)**：The relatively concentrated distribution of distance indicates that the protein belongs to a primitive state.
* **Drug (Fig 2)**：The distribution exhibited a significant population shift, confirming that the drug induced structural changes, prompting the protein to explore new stability points.

### 2. Transition Trajectory
PCA is used to reduce the dimensionality of 4-dimensional data and label the time series (Fig 3):
* **Pathway Evolution**: The protein starts in the **yellow region (initial state)**, passes through the **green region (transition state)**, and finally stabilizes in the **purple region (drug-controlled stable state)**, where the number of dots is highest.

* **Pathway Conclusion**: The evolutionary path is **Yellow ➔ Green ➔ Purple**, confirming the drug's ability to guide structural transformation.

## Key Metrics

Based on the analysis results of K-Means and Silhouette:

| Configuration  | Frequency | Rep. Frame  | Physical meaning |
| :--- | :--- | :--- | :--- |
| **Config 0 (Purple)** | **66.05%** | **2810** | **Dominant Stable State** (Final equilibrium post-drug administration)|
| **Config 2 (Yellow)** | **20.25%** | **584** | **Initial State** (Native structural region)|
| **Config 1 (Green)** | **13.70%** | **1996** | **Transition State** (Transient intermediate structure)|

* **Style Quality (Silhouette Score)**: **0.676** (Confirms that the three configurations have clear physical boundaries)
