import pandas as pd
from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def plot_pred(path, label_name=None, p=None, first=True, color=None, style=None):
    if "T2" in path:
        seq = "T2"
    elif "T1_E" in path:
        seq = "T1_E"
    #seq = path1.split("/")[-1].split("_with_pb.csv")[0]
    if seq=="T1_E":
        seq = seq+"_"
    
    df_result = pd.read_csv(path)

    if path.split("/")[1]=="Only_Patient_Background":
        pred_col1 = "pred"
    elif path.split("/")[1]=="Case_Level":
        pred_col1=f"pred_{seq}sag"
    elif path.split("/")[1]=="Patient_Background+Image_Probability":
      pred_col1=f"pred_{seq}sag"

    fpr1, tpr1, thresholds1 = metrics.roc_curve(df_result["target"],
                                                df_result[pred_col1])
                                            #df_result[f"pred_{seq}sag"])
    best_thresh1 = thresholds1[np.argmax(tpr1 - fpr1)]
    auc1 = metrics.auc(fpr1, tpr1)
    #if first:
     #   plt.figure(figsize=(10, 10))
    if label_name:
      if p:
        if color:
          if style:
            plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]} (P{p})', color=color, linestyle=style)
          else:
            plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]} (P{p})', color=color)
        else:
          plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]} (P{p})')
      else:
        if color:
          if style:
            plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]}', color=color, linestyle=style)
          else:
            plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]}', color=color)
        else:
          plt.plot(fpr1, tpr1, label=f'{label_name} : AUC = {str(auc1)[:5]}')
    else:
      if color:
        if style:
          plt.plot(fpr1, tpr1, color=color, linestyle=style)
        else:
          plt.plot(fpr1, tpr1, color=color)
      else:
        plt.plot(fpr1, tpr1)      
    plt.xlabel('1 - Specificity', fontsize=18)
    plt.ylabel('Sensitivity', fontsize=18)
    #plt.legend(fontsize=18, loc='lower right')

    df_result["pred_class"] = (df_result[pred_col1]>=best_thresh1).astype(np.int16)#(df_result[f"pred_{seq}sag"]>=best_thresh1).astype(np.int16)
    report = metrics.classification_report(df_result['target'],
                                        df_result['pred_class'],
                                        #target_names=CLASS_LABELS,
                                        output_dict=True)
    df_report = pd.DataFrame(report)
    display(df_report.T)
    def specificity_score(y_true, y_pred):
        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).flatten()
        return tn / (tn + fp)
    print(f'specificity :{specificity_score(df_result["target"].values,df_result["pred_class"].values)}')

    return df_report.T, specificity_score(df_result["target"].values,df_result["pred_class"].values)