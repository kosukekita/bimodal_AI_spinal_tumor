# bimodal_AI_spinal_tumor

[Abstract]

Preoperative diagnosis of spinal cord tumors is challenging for physicians, and artificial intelligence (AI) can be helpful. To improve the diagnosing accuracy of such AI, we proposed a bimodal AI model that integrates patient background information and images. Our proposed model combines these two modalities using artificial neural networks designed for respective modalities: TabNet, a state-of-the-art deep learning model that handles tabular data, for patient background information, and a convolutional neural network for images. We collected 259 spinal cord tumor patients with patient information paired with magnetic resonance images for the validation study. For the comparative analysis, we created an image-only, table-only, and bimodal model similar to the proposed model but with a gradient-boosting decision tree, a conventional machine learning model, for table input. The results showed that our proposed bimodal model using TabNet had the best performance (the area under the receiver operating characteristic curve; 0.91±0.04). Furthermore, we also compared the results with physicians and found that our bimodal model outperformed physicians' performance (the area under the receiver operating characteristic curve; 0.93±0.01 vs. 0.82±0.06). These results demonstrate that the proposed holistic approach using bimodal analysis that tightly integrates patient background and image information is effective for differentiating spinal cord tumors.



[Brief description of the results]

The proposed bimodal model with TabNet outperformed a conventional machine learning bimodal model, and unimodal models. Additionally, the proposed bimodal model outperformed physicians. The proposed model was especially efficient in cases with atypical appearances in the images.

 

[Interest and Significance]

1, Proposing a bimodal deep learning model for holistic preoperative diagnosis of spinal cord tumors

2, The proposed model achieved the area under the curve of 0.91 ± 0.04 and outperformed conventional methods and physicians.
