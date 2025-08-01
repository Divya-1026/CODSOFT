import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from PIL import Image
import matplotlib.pyplot as plt
import os

resnet = ResNet50(weights='imagenet')
model = Model(inputs=resnet.input, outputs=resnet.get_layer('avg_pool').output)

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = model.predict(img_array)
    return features

def generate_dummy_caption(features):
    return "A photo of a dog running on the grass."

def main():
    img_path = "example.jpg"  
    if not os.path.exists(img_path):
        print("Image file not found. Please add an image named 'example.jpg'")
        return

    features = extract_features(img_path)

    caption = generate_dummy_caption(features)

    img = Image.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.title("Caption: " + caption)
    plt.show()

if __name__ == "__main__":
    main()
