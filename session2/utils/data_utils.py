from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data import DataLoader
from torchvision import datasets
import numpy as np

def prepare_dataloader(datadir, train_transforms, test_transforms, dataloader_args, valid_size=0.30):
    
    # create dataset from image folder
    train_data = datasets.ImageFolder(datadir,  transform=train_transforms)
    test_data = datasets.ImageFolder(datadir, transform=test_transforms)

    print(f'Total data: {len(train_data)}\n')

    # splitting dataset into training and validate part 
    num_train = len(train_data)
    indices = list(range(num_train))
    split = int(np.floor(valid_size * num_train))
    np.random.shuffle(indices)    # shuffling the ids for randomness

    # prepare train and test ids and respective samplers
    train_idx, test_idx = indices[split:], indices[:split]
    train_sampler = SubsetRandomSampler(train_idx)
    test_sampler = SubsetRandomSampler(test_idx)
    print(f'Training size: {len(train_idx)}')
    print(f'Testing size: {len(test_idx)}')

    # prepare dataloader using sampler
    trainloader = DataLoader(train_data, sampler=train_sampler, **dataloader_args)
    testloader = DataLoader(test_data, sampler=test_sampler, **dataloader_args)
    return trainloader, testloader