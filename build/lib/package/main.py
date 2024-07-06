from package.improved_scraper import handle_db, get_board
import os

def main():
    board_link = input("Link of the Pinterest board whose images you wish to extract: ")
    folder = input("Folder path for the images, if the folder does not exist it will be creates: ")
    name = input("The images would be named 'imagename_i.img', choose 'imagename': ")

    if not os.path.exists(folder):
        os.makedirs(folder)

    title, new_elements = get_board(board_link, folder)
    print(f"Table name: {title}")
    handle_db(title, new_elements, name, folder)

if "__name__" == "__main__":
    main()