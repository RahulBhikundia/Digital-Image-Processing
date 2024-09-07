from PIL import Image, ImageChops
import matplotlib.pyplot as plt
def compare_images(image1_path, image2_path):
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # find the difference
    diff = ImageChops.difference(img1, img2)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(img1)
    axes[0].set_title('Image 1')
    axes[0].axis('off')

    axes[1].imshow(img2)
    axes[1].set_title('Image 2')
    axes[1].axis('off')

    axes[2].imshow(diff)
    axes[2].set_title('Difference')
    axes[2].axis('off')

    plt.show()

    if diff.getbbox() is None:
        print("Images are identical.")
        return True
    else:
        print("Images are different.")
        return False


image1_path = 'Hut.jpg'
image2_path = 'newH.jpg'
result = compare_images(image1_path, image2_path)