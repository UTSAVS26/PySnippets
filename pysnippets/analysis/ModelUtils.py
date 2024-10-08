import time
import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, precision_recall_curve
import matplotlib.pyplot as plt
import seaborn as sns
import psutil

class ModelUtils:

    @staticmethod
    def calculate_inference_speed(model, input_tensor, device='cpu', iterations=100):
        """
        Function to calculate the inference speed of a model.
        """
        model.to(device)
        input_tensor = input_tensor.to(device)
        model.eval()  # Set the model to evaluation mode

        # Warm up the model
        with torch.no_grad():
            _ = model(input_tensor)

        # Timing the inference
        start_time = time.time()
        with torch.no_grad():
            for _ in range(iterations):
                _ = model(input_tensor)
        end_time = time.time()

        avg_inference_time = (end_time - start_time) / iterations
        print(f"Average inference time per input: {avg_inference_time:.6f} seconds")
        return avg_inference_time

    @staticmethod
    def calculate_common_metrics(y_true, y_pred):
        """
        Function to calculate accuracy, precision, recall, F1-score, and confusion matrix.
        """
        acc = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted')
        recall = recall_score(y_true, y_pred, average='weighted')
        f1 = f1_score(y_true, y_pred, average='weighted')
        cm = confusion_matrix(y_true, y_pred)

        print(f"Accuracy: {acc:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-score: {f1:.4f}")
        print(f"Confusion Matrix:\n{cm}")

        return acc, precision, recall, f1, cm

    @staticmethod
    def calculate_model_size(model):
        """
        Function to calculate the size of the model in terms of memory usage.
        """
        param_size = 0
        for param in model.parameters():
            param_size += param.nelement() * param.element_size()

        buffer_size = 0
        for buffer in model.buffers():
            buffer_size += buffer.nelement() * buffer.element_size()

        total_size = (param_size + buffer_size) / (1024 ** 2)  # Convert to MB
        print(f"Model size: {total_size:.2f} MB")
        return total_size

    @staticmethod
    def model_summary(model):
        """
        Function to generate a summary of the model's parameters (layers, total parameters, trainable vs non-trainable).
        """
        num_params = sum(p.numel() for p in model.parameters())
        num_trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        num_non_trainable_params = num_params - num_trainable_params

        print(f"Number of layers: {len(list(model.children()))}")
        print(f"Total parameters: {num_params}")
        print(f"Trainable parameters: {num_trainable_params}")
        print(f"Non-trainable parameters: {num_non_trainable_params}")
        
        return {
            "layers": len(list(model.children())),
            "total_params": num_params,
            "trainable_params": num_trainable_params,
            "non_trainable_params": num_non_trainable_params
        }

    @staticmethod
    def plot_learning_curve(train_acc, val_acc, train_loss, val_loss):
        """
        Function to plot learning curves for training and validation accuracy/loss over time.
        """
        epochs = range(1, len(train_acc) + 1)

        plt.figure(figsize=(12, 5))

        # Plot accuracy
        plt.subplot(1, 2, 1)
        plt.plot(epochs, train_acc, label='Training Accuracy')
        plt.plot(epochs, val_acc, label='Validation Accuracy')
        plt.title('Accuracy over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()

        # Plot loss
        plt.subplot(1, 2, 2)
        plt.plot(epochs, train_loss, label='Training Loss')
        plt.plot(epochs, val_loss, label='Validation Loss')
        plt.title('Loss over Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_precision_recall_curve(y_true, y_scores):
        """
        Function to plot the precision-recall curve, which is useful for imbalanced datasets.
        """
        precision, recall, _ = precision_recall_curve(y_true, y_scores)

        plt.figure(figsize=(8, 6))
        plt.plot(recall, precision, marker='.', label='Precision-Recall Curve')
        plt.title('Precision-Recall Curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.legend()
        plt.grid(True)
        plt.show()
