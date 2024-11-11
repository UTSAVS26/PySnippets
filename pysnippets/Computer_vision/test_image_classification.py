from PIL import Image
import torch # type: ignore
import torchvision.transforms as transforms # type: ignore
from torchvision import models # type: ignore

def load_image(image_path):
    """Load and preprocess an image for model inference"""
    # Load image
    image = Image.open(image_path)
    
    # Define preprocessing steps
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    # Preprocess image
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)
    
    return input_batch

def predict_image(model, image_tensor, class_names):
    """Make prediction on preprocessed image"""
    # Set model to evaluation mode
    model.eval()
    
    # Move input to device if GPU available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    image_tensor = image_tensor.to(device)
    
    with torch.no_grad():
        output = model(image_tensor)
        
    # Get probabilities
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    
    # Get top 5 predictions
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    
    results = []
    for i in range(5):
        results.append({
            'category': class_names[top5_catid[i]],
            'probability': float(top5_prob[i])
        })
    
    return results

def main():
    # Load pretrained model
    model = models.resnet50(pretrained=True)
    
    # Load ImageNet class names
    with open('imagenet_classes.txt', 'r') as f:
        class_names = [line.strip() for line in f.readlines()]
    
    # Example usage
    image_path = 'path/to/your/image.jpg'
    input_batch = load_image(image_path)
    predictions = predict_image(model, input_batch, class_names)
    
    # Print results
    print("\nTop 5 predictions:")
    for pred in predictions:
        print(f"{pred['category']}: {pred['probability']:.4f}")

if __name__ == "__main__":
    main()