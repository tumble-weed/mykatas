import torch
import torchvision.transforms.functional as TF
import random

# Define your batch of image tensors
batch_images = torch.randn((8, 3, 224, 224))  # Example batch

# Function to apply the same random rotation to a batch of images
def rotate_batch(batch_images, degrees):
    angle = random.uniform(-degrees, degrees)
    return torch.stack([TF.rotate(img, angle) for img in batch_images])

rotated_images = rotate_batch(batch_images, 15)

print(rotated_images.shape)  # Should still be (8, 3, 224, 224)
