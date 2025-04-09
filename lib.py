from datasets import Dataset, load_dataset
from loguru import logger
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def get_main_dataset() -> Dataset:
    main_dataset_name = "BanglaLLM/bangla_math_by_Ashrafur"

    logger.info("Loading main dataset from HF Hub")
    logger.info(f"Dataset Name: {main_dataset_name}")

    return load_dataset(main_dataset_name, token=os.getenv("HUGGING_FACE_HUB_TOKEN"))


def apply_conversation_format(example: dict) -> dict:
    user = example["problem"]
    model = example["solution"]

    # there are some examples where solution is none
    if not model:
        text = user
        problem, solution = text.split("### সমাধান:")

        user = problem
        model = "### সমাধান: \n\n" + solution

    conversations = [
        {"role": "user", "content": user},
        {"role": "model", "content": model},
    ]

    return {"conversations": conversations}


def create_formatted_dataset(dataset: Dataset) -> Dataset:
    logger.info("Creating formatted dataset from existing dataset")
    logger.info(f"Dataset size: {len(dataset)}")

    formatted_dataset = dataset.map(apply_conversation_format)
    logger.success(f"Formatted dataset size: {len(formatted_dataset)}")

    return formatted_dataset


def upload_dataset(dataset: Dataset) -> None:
    HF_TOKEN = os.getenv("HUGGING_FACE_HUB_TOKEN")
    assert HF_TOKEN is not None, logger.error(
        "No Hugging Face Hub token found. Please set it in the .env file."
    )

    logger.info("Uploading dataset to Hugging Face Hub...")
    dataset.push_to_hub(
        repo_id="shawon/bangla-math-chat",
        private=False,
        token=HF_TOKEN,
    )
    logger.success("Dataset uploaded successfully!")
