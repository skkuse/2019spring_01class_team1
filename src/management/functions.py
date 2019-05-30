import pandas as pd
import numpy as np
import glob
import os
import torch
import torch.nn.functional as F
from torch import nn
from torchvision import datasets, transforms, models

def excel_to_data(path):
    filelist = glob.glob(path+"/*.xlsx")
    df = pd.read_excel(filelist[0], header=1)
    return [{ k:v for k,v in m.items() if pd.notnull(v)} for m in df.to_dict(orient='rows')]
    
    
    
def img_classification(image_path):
    print (os.getcwd())
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.load("/home/ubuntu/workspace/src/management/classification_model",map_location=device)
    model.eval()
    transform = transforms.Compose([transforms.Resize((224,224)),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                               ])
    validation_dataset = datasets.ImageFolder("/home/ubuntu/workspace"+image_path, transform=transform)
    validation_loader = torch.utils.data.DataLoader(validation_dataset, batch_size = 20, shuffle=True)
    
    classes = ('가방', '긴바지','단화','맨투맨|후드집업','반바지','반팔티','블라우스','스니커즈','스웨터','아우터','치마|스커트','하이힐')
    
    dataiter = iter(validation_loader)
    images, _ = dataiter.next()
    images = images.to(device)
    # labels = labels.to(device)
    output = model(images)
    _, preds = torch.max(output, 1)
    imglist = glob.glob("/home/ubuntu/workspace"+image_path+"/images/*.*")
    return [(img, classes[preds[idx].item()]) for img, idx in zip(imglist ,range(len(preds)))]

    
    