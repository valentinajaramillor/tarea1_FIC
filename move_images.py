import os
import random
import shutil

# Define the paths to the original dataset and the new dataset folders
original_data_dir = './HW1'
new_data_dir = './Fotos_Entrega_1'

# Create a new dataset directory if it doesn't exist
if not os.path.exists(new_data_dir):
    os.makedirs(new_data_dir)

# Define the subfolders for train and test datasets
train_dir = os.path.join(new_data_dir, 'train')
test_dir = os.path.join(new_data_dir, 'test')

# Create train and test directories
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Define the subfolders for birds and other animals in train and test datasets
train_birds_dir = os.path.join(train_dir, 'Aves')
train_other_animals_dir = os.path.join(train_dir, 'Otros_Animales')
test_birds_dir = os.path.join(test_dir, 'Aves')
test_other_animals_dir = os.path.join(test_dir, 'Otros_Animales')

# Create subfolders for birds and other animals in train and test datasets
if not os.path.exists(train_birds_dir):
    os.makedirs(train_birds_dir)

if not os.path.exists(train_other_animals_dir):
    os.makedirs(train_other_animals_dir)

if not os.path.exists(test_birds_dir):
    os.makedirs(test_birds_dir)

if not os.path.exists(test_other_animals_dir):
    os.makedirs(test_other_animals_dir)

# Function to copy images from the original folders to the new folder structure
def copy_images(source_dir, target_train_dir, target_test_dir, split_ratio=0.8):
    image_files = os.listdir(source_dir)
    random.shuffle(image_files)
    split_index = int(len(image_files) * split_ratio)
    
    for filename in image_files[:split_index]:
        source_path = os.path.join(source_dir, filename)
        train_target_path = os.path.join(target_train_dir, filename)
        shutil.copyfile(source_path, train_target_path)
        
    for filename in image_files[split_index:]:
        source_path = os.path.join(source_dir, filename)
        test_target_path = os.path.join(target_test_dir, filename)
        shutil.copyfile(source_path, test_target_path)

# Copy bird images to train and test folders
copy_images(os.path.join(original_data_dir, 'Aves'), train_birds_dir, test_birds_dir)

# Copy other animal images to train and test folders
for folder in ['Artiodactyla', 'Carnivora', 'Cingulata', 'Pilosa', 'Rodentia']:
    source_folder = os.path.join(original_data_dir, folder)
    copy_images(source_folder, train_other_animals_dir, test_other_animals_dir)

print("Data split and organization complete.")
