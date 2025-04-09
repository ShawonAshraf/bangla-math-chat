from lib import create_formatted_dataset, upload_dataset, get_main_dataset


def main() -> None:
    main_dataset = get_main_dataset()
    formatted_dataset = create_formatted_dataset(main_dataset)
    upload_dataset(formatted_dataset)


if __name__ == "__main__":
    main()
