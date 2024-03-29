 #!/usr/bin/env python3
from genericpath import isfile
import os
import json
#----------------------------------------

def createTimeline(year_dict):

    # get the date and title from the user to populate the json file
    date = input(">> Input date in the format (1998-10-10/yyyy-mm-dd):\n   date: ")
    print("-----------------------")
    title = input(">> Input title for the timeline:\n   title: ")
    print("-----------------------")
    milestone = input(">> Mark this event as a Milestone?\n   Milestone(True/False): ")


    print("[+] Entered Date: ", date)
    print("[+] Entered Title: ", title)
    print("[+] Milestone: ", milestone)
    print("-----------------------")

    # json file to populate data
    timeline_file = "./timeline.json"
    # current working directory for the task
    working_dir = "./cron@daily"
    # github url to fetch the timeline markdown file
    github_url = "https://raw.githubusercontent.com/dikkyryan/daily-progress/main/cron@daily/"

    
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]

    # the file that needs to be created
    file_name = f"{day}-{year_dict.get(month)}-{year}.md"
    # the complete file url for public access
    file_url = f"{github_url}{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}.md"

    # json object with data from the user
    if(milestone == "True"):
        timeline_obj = {
            "date": date,
            "title": title,
            "milestone": True,
            "url": file_url
        }
    else:
        timeline_obj = {
            "date": date,
            "title": title,
            "milestone": False,
            "url": file_url
        }

    # open json file to get the file contents(json list)
    json_file = open(timeline_file)
    data = json.load(json_file)

    # insert new json object into existing list of json objects
    data.insert(0, timeline_obj)
    file_exist = False

    if(os.path.isdir(f"{working_dir}/{year}") == False):
        print(f"[!] {working_dir}/{year} : does not exists, creating directory and timeline markdown...")
        os.mkdir(f"{working_dir}/{year}")
        os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}")
        file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name}", "x")
        file.close()
    else:
        if(os.path.isdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}") == False):
            print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)} : does not exists, creating directory and timeline markdown...")
            os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}")
            file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name}", "x")
            file.close()
        else:
            if(os.path.isfile(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name}") == False):
                print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name} : does not exists, creating timeline markdown...")
                file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name}", "x")
                file.close()
            else:
                print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)}/{file_name} : file already exists.")
                file_exist = True
    
    if(file_exist == False):
        with open(timeline_file, 'w') as json_out:
            json.dump(data, json_out, indent=4)
            print("-----------------------")
            print("[!] Timeline entry addition successful")
            print("-----------------------")
            json_out.close()


def createPost(year_dict):
    # get the post name, date, tags and description from the user
    post_title = input(">> Input the post title: \n   post title: ")
    post_date = input(">> Input date in the format (1998-10-10/yyyy-mm-dd): \n   date: ")
    post_tags = list(map(str, input(">> Input the tags for the post, separated by commas: \n   tags: ").split(',')))
    post_description = input(">> Input the post description: \n   description: ")
    print("-----------------------")
    
    # json file to populate data
    postslist_file = "./posts.json"
    # current working directory for the task
    working_dir = "./posts"
    # github url to fetch the posts file
    github_url = "https://raw.githubusercontent.com/dikkyryan/daily-progress/main/posts/"

    year = post_date.split('-')[0]
    month = post_date.split('-')[1]
    day = post_date.split('-')[2]

    # the file that needs to be created
    file_name = f"{day}-{year_dict.get(month)}-{year}.md"
    # the complete file url for public access
    file_url = f"{github_url}{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{day}-{year_dict.get(month)}-{year}.md"

    # open json file to get the file contents(json list)
    json_file = open(postslist_file)
    data = json.load(json_file)

    # json object with data from user
    post_obj = {
        "postno": len(data) + 1,
        "title": post_title,
        "date": post_date,
        "url": file_url,
        "tags": post_tags,
        "description": post_description
    }

    # insert new json object into existing list of json objects
    data.insert(0, post_obj)
    file_exist = False

    if(os.path.isdir(f"{working_dir}/{year}") == False):
        print(f"[!] {working_dir}/{year} : does not exists, creating directory and post markdown...")
        os.mkdir(f"{working_dir}/{year}")
        os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}")
        os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}")
        file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name}", "x")
        file.close()
    else:
        if(os.path.isdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}") == False):
            print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)} : does not exists, creating directory and post markdown...")
            os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}")
            os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}")
            file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name}", "x")
            file.close()
        else:
            if(os.path.isdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}") == False):
                print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year} : does not exists, creating directory and post markdown...")
                os.mkdir(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}")
                file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name}", "x")
                file.close()
            else:
                if(os.path.isfile(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name}") == False):
                    print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name} : does not exists, creating post markdown...")
                    file = open(f"{working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name}", "x")
                    file.close()
                else:
                    print(f"[!] {working_dir}/{year}/{month}-{year_dict.get(month)}/{day}-{year_dict.get(month)}-{year}/{file_name} : file already exists.")
                    file_exist = True
    
    if(file_exist == False):
        with open(postslist_file, 'w') as json_out:
            json.dump(data, json_out, indent=4)
            print("-----------------------")
            print("[!] Post entry addition successful")
            print("-----------------------")
            json_out.close()

def createTheme():
    # get the theme name from the user
    theme_name = input(">> Input theme name: \n   theme name: ")
    print("-----------------------")
    
    themelist_file = "./themelist.json"
    working_dir = "./themes"
    github_url = "https://raw.githubusercontent.com/dikkyryan/daily-progress/main/themes/"
    
    theme_file = f"{theme_name}.json"
    theme_url = f"{github_url}{theme_file}"

    theme_obj = {
        "theme": theme_name,
        "url": theme_url
    }

    # open json file to get the file contents(json list)
    json_file = open(themelist_file)
    data = json.load(json_file)
    data.append(theme_obj)
    
    if(os.path.isfile(f"{working_dir}/{theme_file}") == False):
        print(f"[!] {theme_file} does not exists. Creating file...")
        file = open(f"{working_dir}/{theme_file}", "x")
        file.close()

        with open(themelist_file, 'w') as json_out:
            json.dump(data, json_out, indent=4)
            json_out.close()
            print("-----------------------")
            print("[!] Theme entry addition successful")
            print("-----------------------")
    else:
        print(f"[!] {theme_file} : file already exists. Try giving new name to the theme.")
        main()

def main():
    year_dict = { 
        '01': 'january', 
        '02': 'february', 
        '03': 'march', 
        '04': 'april',
        '05': 'may',
        '06': 'june',
        '07': 'july',
        '08': 'august',
        '09': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december' 
        }

    print("\n>> Select function: \n   1. Create Timeline\n   2. Create post\n   3. Create Theme\n")
    choice = input("\nSelection: ")
    print("-----------------------")

    if(int(choice) == 1):
        createTimeline(year_dict)
    elif(int(choice) == 2):
        createPost(year_dict)
    elif(int(choice) == 3):
        createTheme()
    else:
        print("[-] Please enter valid selection.")
        main()


if __name__ == "__main__":
    main()
