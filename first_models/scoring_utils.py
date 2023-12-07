from sklearn.metrics import recall_score, precision_score, roc_auc_score, roc_curve, auc, f1_score, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to obtain profit from a loans set, it's predictions and the ground truth.
def get_profit (X: pd.DataFrame, y_true: pd.DataFrame, y_pred: pd.DataFrame) -> float:
    # Initialize an empty list to store profits for each sample
    profits = []
    
    for index, row in X.iterrows():
        if y_pred[index] == 0 and y_true[index] == 0:
            profit = 0.05 * row['GrAppv']
        elif y_pred[index] == 0 and y_true[index] == 1:
            profit = -0.15 * row['GrAppv']
        else:
            profit = 0  # If conditions don't match, profit is zero
        profits.append(profit)
    
    # Return the accumulated profit for all samples
    return sum(profits)

def get_best_kernels (results: pd.DataFrame) -> pd.DataFrame:
    """Returns a dataframe with the results, along with a kernel column

    Args:
        results (pd.DataFrame): Dataframe from scikit.search.cv_results
    Returns:
        pd.Dataframe: The cleaned and sorted results.
    """
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values(by=["rank_test_score"])
    results_df = results_df.set_index(
        results_df["params"].apply(lambda x: "_".join(str(val) for val in x.values()))
    ).rename_axis("kernel") # We create a field called kernel that encodes a model hyperparams.
    return results_df[["params", "mean_test_score", 'mean_fit_time']]

def get_metrics (y_true, y_pred, name: str) -> float:
    """Returns the metric dataframe for a prediction and a ground truth.

    Args:
        y_pred (any): Predictions.
        y_true (_type_): True Labels.

    Returns:
        float: The metrics dataframe.
    """
    metrics= [
        recall_score(y_true, y_pred),
        precision_score(y_true, y_pred),
        roc_auc_score(y_true, y_pred),
        f1_score(y_true, y_pred)
    ]

    metrics_df = pd.DataFrame(
        [metrics], 
        columns = ['Recall', 'Precision', 'ROC', 'F1'], 
        index=[name]
    )

    return metrics_df

def get_roc_plot (y_true, y_pred, name: str):
    """_summary_

    Args:
        y_pred (_type_): _description_
        y_true (_type_): _description_
        name (str): _description_
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    roc_auc = auc(fpr, tpr)

    # Plotting the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='black', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'{name} ROC curve')
    plt.legend(loc='lower right')
    plt.show()

def get_confusion_matrix (y_true, y_pred, name: str):
    cm = confusion_matrix(y_true, y_pred)

    # Create a heatmap using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=['no', 'yes'], yticklabels=['no', 'yes'])
    plt.xlabel('Predicted Default')
    plt.ylabel('Actual Default')
    plt.title(f'{name} Confusion Matrix')
    plt.show()