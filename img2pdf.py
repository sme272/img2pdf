#!/bin/python3.8
import os
import sys
from PIL import Image
import argparse


def recursive_compile(path):
    image_list = []
    for file in os.listdir(path):
        if os.path.isdir(file):
            new_path = os.path.join(path, file)
            image_list.extend(recursive_compile(new_path))
        elif file.lower().endswith(".jpg") or file.lower().endswith(".png"):
            file = os.path.join(path, file)
            img = Image.open(file)
            img = img.convert("RGB")
            image_list.append(img)

    return image_list


def compile(path):
    image_list = []
    for file in os.listdir(path):
        if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
            img = Image.open(file)
            img = img.convert("RGB")
            image_list.append(img)

    return image_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compiles all pdf's in a folder to a pdf"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively compiles all images in all subfolders into a pdf",
    )
    parser.add_argument("pdf_name")
    args = parser.parse_args()

    if args.recursive:
        image_list = recursive_compile("./")
    else:
        image_list = compile("./")

    if not args.pdf_name.endswith(".pdf"):
        args.pdf_name += ".pdf"

    if len(image_list) > 1:
        image_list[0].save(args.pdf_name, save_all=True, append_images=image_list[1:])
    elif len(image_list) == 1:
        image_list[0].save(args.pdf_name, save_all=True)
